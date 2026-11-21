// Áreas que cubre cada tutor (para las tutorías individuales) y precio de la tutoría. Lo usan Administración y Dirección.
(function () {
  var sb = Wave.sb;
  var AREAS = { exactas: 'Exactas y Tecnología', humanidades: 'Humanidades', ingles: 'Inglés', creatividad: 'Creatividad y Vida' };
  var AYUDA = { exactas: 'Matemática, Ciencias Naturales, Tecnología, Economía', humanidades: 'Lengua, Ciencias Sociales, Ciudadanía', ingles: 'Inglés', creatividad: 'Arte, Bienestar, Oficios, Proyecto' };
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function casillas(clase, marcadas) {
    return Object.keys(AREAS).map(function (k) {
      return '<label title="' + esc(AYUDA[k]) + '" style="display:inline-flex;align-items:center;gap:5px;margin:2px 10px 2px 0;font-weight:600"><input type="checkbox" class="' + clase + '" value="' + k + '"' + ((marcadas || []).indexOf(k) >= 0 ? ' checked' : '') + '> ' + esc(AREAS[k]) + '</label>';
    }).join('');
  }
  function leer(raiz, clase) { return Array.prototype.map.call(raiz.querySelectorAll('input.' + clase + ':checked'), function (x) { return x.value; }); }

  async function panel(cont) {
    cont.innerHTML = '<div class="wv-vacio">Cargando…</div>';
    var res = await Promise.all([sb.rpc('tutores_con_areas'), sb.rpc('tutoria_individual_config')]);
    if (res[0].error) { cont.innerHTML = '<div class="wv-vacio">' + esc(res[0].error.message) + '</div>'; return; }
    var cfg = res[1].data || {}, tut = res[0].data || [];
    cont.innerHTML =
      '<h2 class="wv-sub" style="margin-top:24px">Áreas de cada tutor</h2>' +
      '<p class="wv-dato">Las tutorías individuales las atiende un tutor del área que elige el alumno. Marcá qué áreas cubre cada tutor (puede ser más de una). Si un área no tiene tutores, nadie puede pedir tutorías de esa área.</p>' +
      (tut.length ? '<div class="wv-alus">' + tut.map(function (t) {
        return '<div class="wv-alu" data-tutor="' + esc(t.id) + '"><div><div class="wv-nombre">' + esc(t.nombre || t.email) + '</div><div class="wv-dato">' + esc(t.email) + '</div></div>' +
          '<div style="flex:1">' + casillas('ar-' + t.id.slice(0, 8), t.areas) + '</div><div><button type="button" class="wv-btn" data-guardar="' + esc(t.id) + '">Guardar</button></div></div>';
      }).join('') + '</div>' : '<div class="wv-vacio">Todavía no hay tutores.</div>') +
      '<h2 class="wv-sub" style="margin-top:24px">Precio de la tutoría individual</h2>' +
      '<form id="wv-precio" class="wv-tut-form"><label>Pesos (Argentina) <input name="ars" type="number" min="1" step="1" required value="' + esc(cfg.precio_ars || '') + '"></label> ' +
      '<label>Dólares (otros países, sin el 5% de PayPal) <input name="usd" type="number" min="1" step="0.01" required value="' + esc(cfg.precio_usd || '') + '"></label> <button class="wv-btn" type="submit">Guardar precio</button></form>' +
      '<p class="wv-dato">Dura lo que dura el horario del tutor (normalmente 60 minutos). La familia tiene ' + esc(cfg.horas_para_pagar || 48) + ' horas para pagar; después el horario se libera.</p>';
    cont.onclick = async function (ev) {
      var b = ev.target.closest('[data-guardar]'); if (!b) return;
      var fila = b.closest('[data-tutor]'), id = b.getAttribute('data-guardar');
      b.disabled = true;
      var r = await sb.rpc('tutor_areas_guardar', { p_tutor: id, p_areas: leer(fila, 'ar-' + id.slice(0, 8)) });
      b.disabled = false; b.textContent = r.error ? 'Error' : '¡Guardado!';
      if (r.error) alert(r.error.message);
      setTimeout(function () { b.textContent = 'Guardar'; }, 1800);
    };
    cont.onsubmit = async function (ev) {
      ev.preventDefault(); var f = ev.target, b = f.querySelector('button'); b.disabled = true;
      var r = await sb.rpc('tutoria_individual_precio_guardar', { p_ars: +f.ars.value, p_usd: +f.usd.value });
      b.disabled = false; if (r.error) { alert(r.error.message); return; }
      b.textContent = '¡Guardado!'; setTimeout(function () { b.textContent = 'Guardar precio'; }, 1800);
    };
  }
  window.WaveAreas = { AREAS: AREAS, casillas: casillas, leer: leer, panel: panel };
})();
