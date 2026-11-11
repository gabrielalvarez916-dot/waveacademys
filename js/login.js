(async function () {
  var form = document.getElementById('form-login');
  var boton = document.getElementById('btn-ingresar');
  var mensaje = document.getElementById('mensaje');
  var cfg = window.WAVE_CONFIG;

  function mostrarError(texto) {
    mensaje.textContent = texto;
    mensaje.hidden = false;
  }

  function ocultarError() {
    mensaje.hidden = true;
    mensaje.textContent = '';
  }

  function cargando(si) {
    boton.disabled = si;
    boton.textContent = si ? 'Ingresando…' : 'Ingresar';
  }

  function traducir(error) {
    var codigo = error.code || '';
    var texto = (error.message || '').toLowerCase();
    if (codigo === 'invalid_credentials' || texto.indexOf('invalid login') !== -1) {
      return 'Usuario o contraseña incorrectos.';
    }
    if (codigo === 'email_not_confirmed') {
      return 'Tu cuenta todavía no está activada.';
    }
    if (error.status === 429 || codigo === 'over_request_rate_limit') {
      return 'Demasiados intentos. Esperá un momento y probá de nuevo.';
    }
    if (texto.indexOf('fetch') !== -1 || error.name === 'AuthRetryableFetchError') {
      return 'No hay conexión. Revisá tu internet y probá de nuevo.';
    }
    return 'No pudimos ingresar. Probá de nuevo en un rato.';
  }

  // Si ya tiene la sesión abierta, entra directo a su panel
  var actual = await Wave.sb.auth.getSession();
  if (actual.data.session) {
    try {
      var perfilActual = await Wave.getProfile(actual.data.session.user.id);
      if (perfilActual && !perfilActual.is_suspended) {
        location.replace(Wave.destino(perfilActual));
        return;
      }
    } catch (e) { /* sigue al formulario */ }
    await Wave.sb.auth.signOut();
  }

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    ocultarError();

    var usuario = form.usuario.value.trim().toLowerCase();
    var clave = form.clave.value;

    if (!usuario || !clave) {
      mostrarError('Escribí tu usuario y tu contraseña.');
      return;
    }

    // Los alumnos pueden escribir solo la primera parte (juanperez4821)
    if (usuario.indexOf('@') === -1) usuario += cfg.DOMINIO_ALUMNOS;

    cargando(true);

    var res = await Wave.sb.auth.signInWithPassword({ email: usuario, password: clave });
    if (res.error) {
      cargando(false);
      mostrarError(traducir(res.error));
      return;
    }

    try {
      var perfil = await Wave.getProfile(res.data.user.id);

      if (!perfil) {
        await Wave.sb.auth.signOut();
        cargando(false);
        mostrarError('Tu cuenta todavía no está lista. Avisale a la escuela.');
        return;
      }

      if (perfil.is_suspended) {
        await Wave.sb.auth.signOut();
        cargando(false);
        mostrarError('Tu cuenta está suspendida. Comunicate con la escuela.');
        return;
      }

      // Registra el último ingreso (si falla, no importa)
      Wave.sb.from('profiles')
        .update({ last_seen_at: new Date().toISOString() })
        .eq('id', res.data.user.id)
        .then(function () {}, function () {});

      location.replace(Wave.destino(perfil));
    } catch (err) {
      await Wave.sb.auth.signOut();
      cargando(false);
      mostrarError('No pudimos cargar tu cuenta. Probá de nuevo.');
    }
  });
})();
