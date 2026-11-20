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
  if (perfil.must_change_password || perfil.role !== rol) {
    location.replace(Wave.destino(perfil));
    return;
  }

  document.getElementById('saludo').textContent = 'Hola, ' + (perfil.full_name || 'bienvenido/a');
  document.getElementById('btn-salir').addEventListener('click', function () { Wave.salir(); });
  document.body.classList.add('listo');
})();
