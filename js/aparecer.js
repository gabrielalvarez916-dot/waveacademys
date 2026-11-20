// Efectos al bajar: el contenido aparece suavemente y el menú queda fijo arriba.
(function () {
  var reducir = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- Menú fijo que aparece al bajar ----------
  var nav = document.querySelector('.cab nav');
  if (nav) {
    var logo = document.querySelector('.cab-logo');
    var ingresar = document.querySelector('.cab-acc a.btn');
    var barra = document.createElement('div');
    barra.className = 'barra-fija';
    if (logo) {
      var a = document.createElement('a');
      a.className = 'barra-logo'; a.href = '/';
      a.setAttribute('aria-label', 'Wave Academy, inicio');
      var img = logo.querySelector('img');
      if (img) { var i2 = document.createElement('img'); i2.src = img.getAttribute('src'); i2.alt = ''; a.appendChild(i2); }
      barra.appendChild(a);
    }
    var nav2 = nav.cloneNode(true);
    nav2.setAttribute('aria-label', 'Secciones (menú fijo)');
    barra.appendChild(nav2);
    if (ingresar) {
      var b = ingresar.cloneNode(true);
      b.removeAttribute('style'); b.classList.add('barra-ingresar');
      barra.appendChild(b);
    }
    document.body.appendChild(barra);
    var visible = false;
    function revisar() {
      var on = (window.pageYOffset || document.documentElement.scrollTop) > 280;
      if (on !== visible) { visible = on; barra.classList.toggle('on', on); }
    }
    window.addEventListener('scroll', revisar, { passive: true });
    revisar();
  }

  // ---------- Contenido que aparece a medida que se baja ----------
  if (reducir || !('IntersectionObserver' in window)) return;
  var SEL = '.manif-frase, .manif-giro, .manif .wrap > p, .principio, .caja, .cifra, .raya, .marco, .plat-fila, .nivel, .materia, .plan, .sec .h2, .sec .bajada, .cierre .wrap > div';
  var io = new IntersectionObserver(function (entradas) {
    entradas.forEach(function (e) {
      if (!e.isIntersecting) return;
      var el = e.target;
      io.unobserve(el);
      el.classList.add('vis');
      setTimeout(function () { el.classList.remove('rev', 'vis'); el.style.transitionDelay = ''; }, 1100);
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -6% 0px' });

  function escanear() {
    var lista = document.querySelectorAll(SEL);
    for (var n = 0; n < lista.length; n++) {
      var el = lista[n];
      if (el.dataset.rv || el.closest('.hero') || el.closest('.barra-fija')) continue;
      el.dataset.rv = '1';
      var hermanos = el.parentNode ? Array.prototype.indexOf.call(el.parentNode.children, el) : 0;
      el.style.transitionDelay = Math.min(hermanos, 3) * 80 + 'ms';
      el.classList.add('rev');
      io.observe(el);
    }
  }
  escanear();
  var t = null;
  new MutationObserver(function () { clearTimeout(t); t = setTimeout(escanear, 150); })
    .observe(document.body, { childList: true, subtree: true });
})();
