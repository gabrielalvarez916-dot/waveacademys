// Botón del "ojito" para mostrar u ocultar la contraseña.
(function () {
  document.querySelectorAll('.ojo').forEach(function (btn) {
    var input = btn.parentElement.querySelector('input');
    btn.addEventListener('click', function () {
      var mostrar = input.type === 'password';
      input.type = mostrar ? 'text' : 'password';
      btn.classList.toggle('viendo', mostrar);
      btn.setAttribute('aria-label', mostrar ? 'Ocultar contraseña' : 'Mostrar contraseña');
      input.focus();
    });
  });
})();
