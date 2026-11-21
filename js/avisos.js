// Campanita de avisos para los paneles (admin, familia y tutor): reuniones nuevas, canceladas, reagendadas y recordatorios.
(function () {
  var sb = window.Wave && window.Wave.sb;
  var barra = document.querySelector('.barra-der');
  if (!sb || !barra) return;
  var DESTINO = { admin: '#agenda', tutor: '#agenda', family: '#tutorias' };

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function hace(v) {
    var m = Math.round((Date.now() - new Date(v).getTime()) / 60000);
    if (m < 1) return 'recién';
    if (m < 60) return 'hace ' + m + ' min';
    var h = Math.round(m / 60);
    if (h < 24) return 'hace ' + h + ' h';
    var d = Math.round(h / 24);
    return d === 1 ? 'ayer' : 'hace ' + d + ' días';
  }

  var btn = document.createElement('button');
  btn.type = 'button'; btn.className = 'av-campana'; btn.setAttribute('aria-label', 'Avisos'); btn.setAttribute('aria-expanded', 'false');
  btn.innerHTML = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg><span class="av-punto" hidden></span>';
  var panel = document.createElement('div');
  panel.className = 'av-panel'; panel.hidden = true; panel.setAttribute('role', 'region'); panel.setAttribute('aria-label', 'Avisos');
  barra.insertBefore(btn, barra.firstChild);
  document.body.appendChild(panel);

  var avisos = [];
  function pintar() {
    var sin = avisos.filter(function (a) { return !a.leida; }).length;
    var punto = btn.querySelector('.av-punto');
    punto.hidden = !sin; punto.textContent = sin > 9 ? '9+' : String(sin);
    btn.setAttribute('aria-label', sin ? 'Avisos: ' + sin + ' sin leer' : 'Avisos');
    panel.innerHTML = '<h2 class="av-titulo">Avisos</h2>' + (avisos.length ? avisos.map(function (a) {
      return '<a class="av-item' + (a.leida ? '' : ' nuevo') + '" href="' + (DESTINO[document.body.dataset.rol] || '#') + '"><b>' + esc(a.titulo) + '</b>' +
        '<span>' + esc(a.texto || '') + '</span><small>' + hace(a.created_at) + '</small></a>';
    }).join('') : '<p class="av-vacio">No tenés avisos por ahora.</p>');
  }
  async function cargar() {
    var r = await sb.from('notificaciones').select('id, titulo, texto, leida, created_at').order('created_at', { ascending: false }).limit(30);
    if (r.error) return;
    avisos = r.data || []; pintar();
  }
  async function abrir() {
    panel.hidden = !panel.hidden;
    btn.setAttribute('aria-expanded', panel.hidden ? 'false' : 'true');
    if (panel.hidden) return;
    var ids = avisos.filter(function (a) { return !a.leida; }).map(function (a) { return a.id; });
    if (ids.length) {
      // Se dejan marcados como "nuevos" mientras el panel está abierto y se marcan leídos en la base
      var r = await sb.from('notificaciones').update({ leida: true }).in('id', ids);
      if (!r.error) {
        var punto = btn.querySelector('.av-punto'); punto.hidden = true;
        avisos.forEach(function (a) { if (ids.indexOf(a.id) >= 0) a.leida = true; });
      }
    }
  }
  btn.addEventListener('click', function (ev) { ev.stopPropagation(); abrir(); });
  panel.addEventListener('click', function (ev) { if (ev.target.closest('.av-item')) { panel.hidden = true; btn.setAttribute('aria-expanded', 'false'); } });
  document.addEventListener('click', function (ev) { if (!panel.hidden && !panel.contains(ev.target)) { panel.hidden = true; btn.setAttribute('aria-expanded', 'false'); } });
  document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape') { panel.hidden = true; btn.setAttribute('aria-expanded', 'false'); } });

  sb.auth.getSession().then(function (s) {
    if (!s.data.session) return;
    cargar();
    setInterval(function () { if (!document.hidden && panel.hidden) cargar(); }, 60000);
  });
})();
