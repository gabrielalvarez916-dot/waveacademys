(async function () {
  var form = document.getElementById('form-clave');
  var boton = document.getElementById('btn-guardar');
  var mensaje = document.getElementById('mensaje');

  function mostrarError(texto) {
    mensaje.textContent = texto;
    mensaje.hidden = false;
  }

  function cargando(si) {
    boton.disabled = si;
    boton.textContent = si ? 'Guardando…' : 'Guardar y continuar';
  }

  document.getElementById('btn-salir').addEventListener('click', function () { Wave.salir(); });

  // Solo puede estar acá quien tiene la sesión abierta y todavía debe cambiar la clave
  var actual = await Wave.sb.auth.getSession();
  var sesion = actual.data.session;
  if (!sesion) { location.replace('/index.html'); return; }

  var perfil = null;
  try { perfil = await Wave.getProfile(sesion.user.id); } catch (e) { /* queda null */ }

  if (!perfil || perfil.is_suspended) {
    await Wave.sb.auth.signOut();
    location.replace('/index.html');
    return;
  }

  if (!perfil.must_change_password) {
    location.replace(Wave.destino(perfil));
    return;
  }

  document.body.classList.add('listo');

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    mensaje.hidden = true;

    var nueva = form.nueva.value;
    var repetir = form.repetir.value;

    if (nueva.length < 8) {
      mostrarError('La contraseña debe tener al menos 8 caracteres.');
      return;
    }
    if (nueva !== repetir) {
      mostrarError('Las dos contraseñas no coinciden.');
      return;
    }

    cargando(true);

    var cambio = await Wave.sb.auth.updateUser({ password: nueva });
    if (cambio.error) {
      cargando(false);
      var codigo = cambio.error.code || '';
      if (codigo === 'same_password') {
        mostrarError('Elegí una contraseña distinta a la inicial.');
      } else if (codigo === 'weak_password') {
        mostrarError('Esa contraseña es muy fácil de adivinar. Probá con otra.');
      } else {
        mostrarError('No pudimos cambiar la contraseña. Probá de nuevo.');
      }
      return;
    }

    var marca = await Wave.sb
      .from('profiles')
      .update({ must_change_password: false })
      .eq('id', sesion.user.id);

    if (marca.error) {
      cargando(false);
      mostrarError('No pudimos guardar el cambio. Probá de nuevo.');
      return;
    }

    perfil.must_change_password = false;
    location.replace(Wave.destino(perfil));
  });
})();
