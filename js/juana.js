// Pestaña "Juana" del panel de la familia: informes semanales de seguimiento de cada estudiante.
(function () {
  var sb = Wave.sb;
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function dia(v) { return new Date(v + 'T12:00:00').toLocaleDateString('es-AR', { day: 'numeric', month: 'long' }); }

  async function vista(cont) {
    cont.innerHTML = '<h1 class="vista-titulo">Juana</h1><p class="fa-intro">Juana es quien acompaña el seguimiento de cada estudiante. Cada domingo a la noche prepara un informe breve con lo que avanzó, lo que mejor le fue y lo que le costó.</p><div id="ju-lista"><div class="vacio">Cargando…</div></div>';
    var r = await sb.from('seguimiento_informes').select('id,student_id,semana,texto,datos,leido_at,students(first_name,apodo)').order('semana', { ascending: false }).limit(40);
    var lista = document.getElementById('ju-lista');
    if (r.error) { lista.innerHTML = '<div class="vacio">No pudimos cargar los informes. Probá de nuevo en un rato.</div>'; return; }
    var inf = r.data || [];
    if (!inf.length) { lista.innerHTML = '<div class="vacio">Todavía no hay informes. El primero llega el próximo domingo a la noche.</div>'; return; }
    lista.innerHTML = inf.map(function (i, n) {
      var a = Array.isArray(i.students) ? i.students[0] : i.students, nombre = a ? (a.apodo || a.first_name) : 'Estudiante', d = i.datos || {};
      var chips = i.datos && !d.sin_actividad ? '<div class="ju-chips"><span>' + (d.lecciones_completadas || 0) + ' lecciones</span><span>' + (d.dias_activos || 0) + ' días activo</span>' + (d.promedio_actividades != null ? '<span>Promedio ' + esc(d.promedio_actividades) + '</span>' : '') + '</div>' : '';
      return '<section class="fa-card ju-informe' + (i.leido_at ? '' : ' nuevo') + '" data-id="' + esc(i.id) + '"><div class="pg-cab"><b>' + esc(nombre) + '</b> · semana del ' + esc(dia(d.desde || i.semana)) + ' al ' + esc(dia(d.hasta || i.semana)) + (i.leido_at ? '' : ' <span class="ju-nuevo">Nuevo</span>') + '</div>' + chips +
        '<p class="ju-texto">' + esc(i.texto || '').replace(/\n+/g, '<br>') + '</p></section>';
    }).join('');
    var sin = inf.filter(function (i) { return !i.leido_at; }).map(function (i) { return i.id; });
    if (sin.length) sb.from('seguimiento_informes').update({ leido_at: new Date().toISOString() }).in('id', sin).then(function () {});
  }
  window.WaveJuana = { vista: vista };
})();
