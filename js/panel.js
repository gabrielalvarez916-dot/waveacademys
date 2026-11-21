// Guardia de los paneles: deja pasar solo a quien tiene sesión y el rol correcto.
(async function () {
  var rol = document.body.dataset.rol;

  var actual = await Wave.sb.auth.getSession();
  var sesion = actual.data.session;
  if (!sesion) { location.replace('/ingresar.html'); return; }

  var perfil = null;
  try { perfil = await Wave.getProfile(sesion.user.id); } catch (e) { /* queda null */ }

  if (!perfil || perfil.is_suspended) {
    await Wave.sb.auth.signOut();
    location.replace('/ingresar.html');
    return;
  }

  // Si debe cambiar la clave, o este panel no es el de su rol, lo manda a donde corresponde
  if (perfil.must_change_password || rol.split(',').indexOf(perfil.role) < 0) {
    location.replace(Wave.destino(perfil));
    return;
  }

  document.getElementById('saludo').textContent = 'Hola, ' + (perfil.full_name || 'bienvenido/a');
  document.getElementById('btn-salir').addEventListener('click', function () { Wave.salir(); });
  // Alumnos de familias con la cuota vencida más allá de los días de gracia (solo si tesorería activó el bloqueo)
  if (perfil.role === 'student') {
    try {
      var bl = await Wave.sb.rpc('alumno_bloqueado');
      if (bl.data === true) {
        document.body.innerHTML = '<main style="min-height:100vh;display:grid;place-items:center;padding:24px;background:#D7F0E9;font-family:Nunito,system-ui,sans-serif;text-align:center"><div style="max-width:460px;background:#fff;border-radius:24px;padding:32px"><h1 style="margin:0 0 10px;color:#253638">Acceso en pausa</h1><p style="color:#4B6062;line-height:1.5">La cuota de tu familia está pendiente. Pedile a tu mamá, papá o tutor que cargue el comprobante de pago en la sección Pagos y se reactiva apenas lo confirmemos.</p><button id="btn-salir-bl" style="margin-top:14px;min-height:44px;padding:0 22px;border-radius:12px;border:2px solid #087E83;background:#fff;color:#087E83;font:inherit;font-weight:800;cursor:pointer">Salir</button></div></main>';
        document.getElementById('btn-salir-bl').addEventListener('click', function () { Wave.salir(); });
        return;
      }
    } catch (e) { /* si falla la consulta, no se bloquea a nadie */ }
  }
  document.body.classList.add('listo');
})();
