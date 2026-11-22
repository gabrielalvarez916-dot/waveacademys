// Panel de familias: navegación y sección Altas.
(function () {
  var sb = Wave.sb;
  var vista = document.getElementById('vista');
  var enlaces = document.querySelectorAll('.nav-familia a');

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  // "Nivel Medio · Año 3" (el Nivel Inicial tiene un único año y se muestra solo)
  function etiquetaAnio(g) {
    var nivel = g.levels ? g.levels.name : '';
    if (!nivel || nivel === g.name) return g.name;
    return nivel + ' · ' + g.name;
  }

  var PAISES = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'España', 'Estados Unidos', 'Guatemala', 'Honduras', 'México', 'Nicaragua', 'Panamá', 'Paraguay', 'Perú', 'Puerto Rico', 'República Dominicana', 'Uruguay', 'Venezuela', 'Otro'];
  var PAIS_FAM = null; // país de la familia: Argentina paga en pesos (Mercado Pago); otro país, en dólares (PayPal)

  // ---------- País de la familia: se pregunta una vez, apenas entra ----------
  function preguntarPais(obligatorio) {
    return new Promise(function (listo) {
      var el = document.createElement('div');
      el.className = 'fp-fondo';
      el.innerHTML = '<div class="fp-caja" role="dialog" aria-modal="true" aria-labelledby="fp-t">' +
        '<h2 id="fp-t">¿En qué país viven?</h2>' +
        '<p>Así te mostramos los precios y la forma de pago que te corresponden: en pesos con Mercado Pago si viven en la Argentina, o en dólares con PayPal si viven en otro país.</p>' +
        '<select id="fp-pais" aria-label="País">' + PAISES.map(function (p) { return '<option' + (p === (PAIS_FAM || 'Argentina') ? ' selected' : '') + '>' + p + '</option>'; }).join('') + '</select>' +
        '<p class="fp-err" id="fp-err" hidden></p>' +
        '<div class="fp-acc">' + (obligatorio ? '' : '<button type="button" class="fp-cancelar" id="fp-no">Cancelar</button>') +
        '<button type="button" class="boton" id="fp-ok">Guardar</button></div></div>';
      document.body.appendChild(el);
      el.querySelector('#fp-ok').addEventListener('click', async function () {
        var v = el.querySelector('#fp-pais').value, b = this;
        b.disabled = true;
        var r = await sb.rpc('set_family_pais', { p_pais: v });
        if (r.error) { var e = el.querySelector('#fp-err'); e.textContent = 'No se pudo guardar. Probá de nuevo.'; e.hidden = false; b.disabled = false; return; }
        var antes = PAIS_FAM; PAIS_FAM = v; el.remove();
        try { localStorage.setItem('wave_neutro', v !== 'Argentina' ? '1' : '0'); } catch (x) {}
        if (v !== 'Argentina' && window.WaveNeutro) WaveNeutro.activar();          // interfaz en español neutro
        else if (antes && antes !== 'Argentina' && window.WaveNeutro && WaveNeutro.activo) return location.reload(); // vuelve al voseo
        listo(v);
      });
      var no = el.querySelector('#fp-no'); if (no) no.addEventListener('click', function () { el.remove(); listo(null); });
    });
  }
  async function asegurarPais() {
    try {
      var ses = await sb.auth.getSession();
      var f = await sb.from('families').select('pais').eq('profile_id', ses.data.session.user.id).maybeSingle();
      if (f.data) { PAIS_FAM = f.data.pais; if (!PAIS_FAM) await preguntarPais(true); }
    } catch (e) {}
  }

  // ---------- WhatsApp de contacto: se pide una vez (el correo ya es el usuario) ----------
  function preguntarContacto() {
    return new Promise(function (listo) {
      var el = document.createElement('div');
      el.className = 'fp-fondo';
      el.innerHTML = '<div class="fp-caja" role="dialog" aria-modal="true" aria-labelledby="fc-t">' +
        '<h2 id="fc-t">¿A qué WhatsApp te avisamos?</h2>' +
        '<p>Por acá te avisamos de reuniones, turnos y cambios. Los avisos también te llegan al correo con el que ingresás.</p>' +
        '<input id="fc-tel" type="tel" autocomplete="tel" maxlength="30" placeholder="+54 9 11 1234 5678" aria-label="WhatsApp">' +
        '<p class="fp-err" id="fc-err" hidden></p>' +
        '<div class="fp-acc"><button type="button" class="boton" id="fc-ok">Guardar</button></div></div>';
      document.body.appendChild(el);
      el.querySelector('#fc-ok').addEventListener('click', async function () {
        var b = this, er = el.querySelector('#fc-err'); b.disabled = true; er.hidden = true;
        var r = await sb.rpc('set_family_contacto', { p_phone: el.querySelector('#fc-tel').value });
        if (r.error) { er.textContent = r.error.message; er.hidden = false; b.disabled = false; return; }
        el.remove(); listo();
      });
    });
  }
  async function asegurarContacto() {
    try {
      var ses = await sb.auth.getSession();
      var f = await sb.from('families').select('phone').eq('profile_id', ses.data.session.user.id).maybeSingle();
      if (f.data && !(f.data.phone || '').trim()) await preguntarContacto();
    } catch (e) {}
  }

  // ---------- Datos ----------
  async function cargarDatos() {
    var ses = await sb.auth.getSession();
    var uid = ses.data.session.user.id;

    var fam = await sb.from('families').select('id').eq('profile_id', uid).maybeSingle();
    if (fam.error) throw fam.error;
    if (!fam.data) throw new Error('Sin familia');

    var res = await Promise.all([
      sb.from('subscriptions').select('id, student_id, status').eq('family_id', fam.data.id),
      sb.from('students')
        .select('id, first_name, last_name, grade_id, created_at, trayectos_apoyo, apoyos, grades(name, levels(name)), profiles!students_profile_id_fkey(email)')
        .eq('family_id', fam.data.id)
        .order('created_at', { ascending: true }),
      sb.from('grades').select('id, year_number, name, levels(name, position)'),
      sb.from('trayectos_apoyo').select('clave, nombre, descripcion').order('orden'),
      sb.from('test_aprendizaje').select('student_id, fecha, trayectos').order('fecha', { ascending: false }),
      sb.from('adaptaciones_apoyo').select('clave, trayecto, texto, texto_familia, lista, orden').order('orden')
    ]);
    res.forEach(function (r) { if (r.error) throw r.error; });

    var cupos = (res[0].data || []).filter(function (s) {
      return !s.student_id && (s.status === 'active' || s.status === 'past_due');
    }).length;

    var anios = (res[2].data || []).slice().sort(function (a, b) {
      var pa = a.levels ? a.levels.position : 0, pb = b.levels ? b.levels.position : 0;
      return pa - pb || a.year_number - b.year_number;
    });

    return { cupos: cupos, hijos: res[1].data || [], anios: anios, trayectos: res[3].data || [], tests: res[4].data || [], adaptaciones: res[5].data || [], famId: fam.data.id };
  }

  // La función devuelve el motivo del error en el cuerpo de la respuesta
  async function mensajeDeError(err) {
    try {
      if (err && err.context && typeof err.context.json === 'function') {
        var cuerpo = await err.context.json();
        if (cuerpo && cuerpo.error) return cuerpo.error;
      }
    } catch (e) { /* cae al mensaje genérico */ }
    return 'No se pudo dar de alta al estudiante. Intentá de nuevo.';
  }

  // ---------- Altas ----------
  function pintarCredenciales(cont, c, nombre) {
    cont.innerHTML =
      '<section class="cred" aria-live="polite">' +
        '<h2>¡' + esc(nombre) + ' ya está dado/a de alta!</h2>' +
        '<p>Guardá estos datos: son los que va a usar para ingresar. Al entrar por primera vez le va a pedir que cambie la contraseña.</p>' +
        '<div class="cred-fila"><div><small>Usuario</small><b>' + esc(c.username) + '</b></div>' +
          '<button type="button" class="cred-copiar" data-copiar="' + esc(c.username) + '">Copiar</button></div>' +
        '<div class="cred-fila"><div><small>Contraseña inicial</small><b>' + esc(c.initial_password) + '</b></div>' +
          '<button type="button" class="cred-copiar" data-copiar="' + esc(c.initial_password) + '">Copiar</button></div>' +
        '<button type="button" class="cred-cerrar" data-cerrar>Listo, ya los guardé</button>' +
      '</section>';

    cont.onclick = function (ev) {
      var btn = ev.target.closest('[data-copiar]');
      if (btn) {
        var texto = btn.getAttribute('data-copiar');
        var ok = function () { btn.textContent = '¡Copiado!'; setTimeout(function () { btn.textContent = 'Copiar'; }, 1500); };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(texto).then(ok, function () {});
        }
        return;
      }
      if (ev.target.closest('[data-cerrar]')) cont.innerHTML = '';
    };
  }

  function pintarAltas(cont, d) {
    var sinCupo = d.cupos < 1;

    var cupos =
      '<div class="cupos' + (sinCupo ? ' sin' : '') + '">' +
        '<div><span class="cupos-rotulo">Cupos disponibles</span><span class="cupos-valor">' + d.cupos + '</span></div>' +
        '<p class="cupos-txt">' + (sinCupo
          ? 'No tenés suscripciones pagas libres. Para dar de alta a un hijo, primero abonás su suscripción en Facturación.'
          : 'Cada cupo corresponde a una suscripción paga y se usa al dar de alta a un hijo.') + '</p>' +
      '</div>';

    var opciones = '<option value="" disabled selected>Elegí el año</option>' +
      d.anios.map(function (g) { return '<option value="' + esc(g.id) + '">' + esc(etiquetaAnio(g)) + '</option>'; }).join('');

    var dis = sinCupo ? ' disabled' : '';
    var form =
      '<form class="alta-form" id="alta-form" novalidate>' +
        '<h2>Dar de alta a un hijo</h2>' +
        '<p class="bajada">Completá sus datos y le creamos el usuario para ingresar a su aula.</p>' +
        '<div class="alta-grilla">' +
          '<div class="campo"><label for="a-nombre">Nombre</label><input id="a-nombre" type="text" autocomplete="off" maxlength="60" placeholder="Nombre"' + dis + '></div>' +
          '<div class="campo"><label for="a-apellido">Apellido</label><input id="a-apellido" type="text" autocomplete="off" maxlength="60" placeholder="Apellido"' + dis + '></div>' +
          '<div class="campo"><label for="a-nac">Fecha de nacimiento</label><input id="a-nac" type="date"' + dis + '></div>' +
          '<div class="campo"><label for="a-dni">DNI</label><input id="a-dni" type="text" inputmode="numeric" autocomplete="off" maxlength="15" placeholder="Número de documento"' + dis + '></div>' +
          '<div class="campo ancho"><label for="a-anio">Año que cursa</label><select id="a-anio"' + dis + '>' + opciones + '</select></div>' +
          '<div class="campo ancho"><label for="a-pais">País donde vive</label><select id="a-pais"' + dis + '>' +
            PAISES.map(function (p) { return '<option' + (p === (PAIS_FAM || 'Argentina') ? ' selected' : '') + '>' + p + '</option>'; }).join('') +
          '</select><small class="ayuda">Si vive fuera de la Argentina, las clases y los PDF le llegan en español neutro latinoamericano.</small></div>' +
        '</div>' +
        '<p class="mensaje" id="a-error" hidden></p>' +
        '<button class="boton" type="submit" id="a-enviar"' + dis + '>Dar de alta</button>' +
      '</form>';

    var lista = d.hijos.length
      ? '<h2 class="vista-subtitulo">Tus hijos</h2><div class="hijos">' + d.hijos.map(function (h) {
          var ini = (h.first_name || '?').charAt(0) + (h.last_name || '').charAt(0);
          var usuario = h.profiles && h.profiles.email ? h.profiles.email : '';
          return '<div class="hijo"><div class="hijo-ini">' + esc(ini.toUpperCase()) + '</div>' +
            '<div class="hijo-info"><b>' + esc(h.first_name + ' ' + h.last_name) + '</b>' +
            '<span>' + esc(h.grades ? etiquetaAnio(h.grades) : '') + '</span>' +
            (usuario ? '<span>' + esc(usuario) + '</span>' : '') +
            testResumen(h, d) +
            '</div></div>';
        }).join('') + '</div>'
      : '';

    cont.innerHTML = testAvisos(d) + cupos + '<div id="cred"></div>' + form + lista;

    cont.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-test]');
      if (!b) return;
      var h = d.hijos.filter(function (x) { return x.id === b.getAttribute('data-test'); })[0];
      if (h) abrirTest({ id: h.id, nombre: h.first_name }, d, async function () { await vistaAltas(); });
    });

    var f = document.getElementById('alta-form');
    var err = document.getElementById('a-error');
    var btn = document.getElementById('a-enviar');

    function mostrarError(t) { err.textContent = t; err.hidden = false; }

    f.addEventListener('submit', async function (ev) {
      ev.preventDefault();
      if (sinCupo) return;
      err.hidden = true;

      var nombre = document.getElementById('a-nombre').value.trim();
      var apellido = document.getElementById('a-apellido').value.trim();
      var nac = document.getElementById('a-nac').value;
      var dni = document.getElementById('a-dni').value.trim();
      var anio = document.getElementById('a-anio').value;
      var pais = (document.getElementById('a-pais') || {}).value || 'Argentina';

      if (!nombre || !apellido || !anio) { mostrarError('Completá nombre, apellido y el año que cursa.'); return; }
      if (nac && nac > new Date().toISOString().slice(0, 10)) { mostrarError('La fecha de nacimiento no puede ser futura.'); return; }

      btn.disabled = true; btn.textContent = 'Dando de alta…';
      var r = await sb.functions.invoke('create-student', {
        body: { first_name: nombre, last_name: apellido, birth_date: nac || null, document_number: dni || null, grade_id: anio, pais: pais }
      });

      if (r.error || !r.data || r.data.error) {
        mostrarError(r.error ? await mensajeDeError(r.error) : ((r.data && r.data.error) || 'No se pudo dar de alta. Intentá de nuevo.'));
        btn.disabled = false; btn.textContent = 'Dar de alta';
        return;
      }

      // El test "Cómo aprende tu hijo" es obligatorio: se hace antes de mostrar el usuario y la contraseña
      var datosAlta = r.data;
      var dNuevo = { trayectos: d.trayectos, adaptaciones: d.adaptaciones, famId: d.famId, tests: [], hijos: [] };
      abrirTest({ id: datosAlta.student_id, nombre: nombre }, dNuevo, async function () {
        await vistaAltas();
        var credCont = document.getElementById('cred');
        if (credCont) {
          pintarCredenciales(credCont, datosAlta, nombre);
          credCont.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }, true);
    });
  }


  // ---------- Test "Cómo aprende tu hijo": define el trayecto y los ajustes de cada alumno ----------
  var T_AREAS = ['lectura', 'foco', 'anticipacion', 'numero', 'desafio'];
  var T_PREG = [
    ['lectura', 'Al leer un texto, ¿va muy despacio, se saltea palabras o pierde el renglón?'],
    ['foco', '¿Le cuesta sostener la atención en una tarea más de unos pocos minutos?'],
    ['anticipacion', '¿Se incomoda o se altera cuando cambia la rutina o pasa algo que no estaba previsto?'],
    ['numero', '¿Le cuesta entender cuánto es una cantidad, comparar números o estimar?'],
    ['desafio', '¿Aprende un tema nuevo bastante más rápido de lo esperable para su edad?'],
    ['lectura', '¿Evita leer en voz alta o se pone nervioso cuando tiene que hacerlo?'],
    ['foco', '¿Se distrae con ruidos, objetos o pensamientos y pierde el hilo de lo que estaba haciendo?'],
    ['anticipacion', '¿Necesita saber con anticipación qué va a pasar y cuánto va a durar una actividad?'],
    ['numero', '¿Se confunde con los signos, el orden de los números o las cuentas, aunque lo haya practicado?'],
    ['desafio', '¿Se aburre o se frustra cuando le piden repetir algo que ya sabe?'],
    ['lectura', '¿Entiende mucho mejor cuando alguien le lee el texto que cuando lo lee solo?'],
    ['foco', '¿Deja las tareas a medias o empieza otra cosa antes de terminar la primera?'],
    ['anticipacion', '¿Se confunde con consignas que pueden entenderse de más de una manera, como "contame con tus palabras"?'],
    ['numero', '¿Le cuesta recordar tablas, horas, fechas o cuentas simples sin ayuda?'],
    ['desafio', '¿Hace preguntas profundas o pide ir más allá de lo que le enseñan?'],
    ['lectura', '¿Se cansa o se frustra con textos largos, aunque entienda las ideas?'],
    ['foco', '¿Se le olvidan los pasos o lo que tenía que hacer, aunque se lo hayas explicado recién?'],
    ['anticipacion', '¿Le cuesta empezar una actividad nueva si no sabe exactamente qué se espera de él?'],
    ['numero', '¿Evita o se angustia ante actividades con números?'],
    ['desafio', '¿Termina las tareas mucho antes que los demás y se queda sin nada que hacer?']
  ];
  var T_OPC = [['Nunca', 0], ['A veces', 1], ['Seguido', 2], ['Casi siempre', 3]];
  var T_UMBRAL = { lectura: 6, foco: 6, anticipacion: 6, numero: 6, desafio: 7 };
  var T_DIAG = { lectura: /dislex|lectura|lector/, foco: /tdah|tda\b|atencion|hiperact|deficit/, anticipacion: /\btea\b|autis|asperger|espectro/, numero: /discalcul|calculo/, desafio: /alta.?capacidad|sobredot|superdot|talento|precoz/ };
  var T_AJUSTES = {
    lectura: { letra: 1, sinCrono: true, deAUna: true },
    foco: { deAUna: true, sinCrono: true, comprobar: true, sinAnim: true },
    anticipacion: { sinCrono: true, sinAnim: true, comprobar: true },
    numero: { sinCrono: true, comprobar: true },
    desafio: {}
  };
  var T_ETIQ = { letra: 'Letra más grande', sinCrono: 'Sin cronómetro en las actividades', deAUna: 'Una consigna por vez', comprobar: 'Comprobar cada respuesta', sinAnim: 'Menos animación' };

  function sinTilde(t) { return String(t || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }

  function calcularTest(resp, diag) {
    var pts = {}, d = sinTilde(diag), bonus = {};
    T_AREAS.forEach(function (a) { pts[a] = 0; });
    T_PREG.forEach(function (q, i) { pts[q[0]] += Number(resp[i]) || 0; });
    T_AREAS.forEach(function (a) { bonus[a] = d && T_DIAG[a].test(d) ? 2 : 0; });
    var cand = T_AREAS.filter(function (a) { return pts[a] + bonus[a] >= T_UMBRAL[a]; })
      .sort(function (x, y) { return (pts[y] + bonus[y]) - (pts[x] + bonus[x]) || bonus[y] - bonus[x] || T_AREAS.indexOf(x) - T_AREAS.indexOf(y); });
    var ajustes = {};
    cand.slice(0, 2).forEach(function (a) {
      Object.keys(T_AJUSTES[a]).forEach(function (k) { ajustes[k] = k === 'letra' ? Math.max(ajustes[k] || 0, T_AJUSTES[a][k]) : T_AJUSTES[a][k]; });
    });
    return { puntajes: pts, trayectos: cand.slice(0, 2), ajustes: ajustes, muchas: cand.length >= 3 };
  }

  function fechaCorta(iso) { var f = new Date(iso); return f.getDate() + '/' + (f.getMonth() + 1) + '/' + f.getFullYear(); }
  function ultimoTest(d, id) { return (d.tests || []).filter(function (t) { return t.student_id === id; })[0] || null; }
  function pasaron6Meses(iso) { var l = new Date(iso); l.setMonth(l.getMonth() + 6); return l < new Date(); }
  function nombreTrayecto(d, c) { var t = (d.trayectos || []).filter(function (x) { return x.clave === c; })[0]; return t ? t.nombre : c; }

  function adaptacionesDe(d, trayectos) { return (d.adaptaciones || []).filter(function (a) { return trayectos.indexOf(a.trayecto) >= 0; }); }
  function adaptacionesHtml(d, c) {
    var xs = adaptacionesDe(d, [c]).filter(function (a) { return a.lista && (a.texto_familia || a.texto); });
    if (!xs.length) return '';
    return '<ul class="tst-ad">' + xs.map(function (a) {
      return '<li><span class="tst-ck" aria-hidden="true">✓</span>' + esc(a.texto_familia || a.texto) + '</li>';
    }).join('') + '</ul>';
  }

  function testResumen(h, d) {
    var t = ultimoTest(d, h.id);
    if (!t) return '<span class="test-estado pend">Falta hacer el test “Cómo aprende tu hijo”</span><button type="button" class="boton-mini" data-test="' + esc(h.id) + '">Hacer el test</button>';
    var tr = (t.trayectos || []).length ? t.trayectos.map(function (c) { return nombreTrayecto(d, c); }).join(' + ') : 'Convencional';
    return '<span class="test-estado">Test del ' + fechaCorta(t.fecha) + ' · Trayecto: <b>' + esc(tr) + '</b>' + (pasaron6Meses(t.fecha) ? ' · <em>pasaron más de 6 meses, conviene repetirlo</em>' : '') + '</span>' +
      '<button type="button" class="boton-mini" data-test="' + esc(h.id) + '">Repetir el test</button>';
  }

  function testAvisos(d) {
    var out = [];
    (d.hijos || []).forEach(function (h) {
      var t = ultimoTest(d, h.id);
      if (!t) out.push('<div class="test-aviso">Falta el test <b>Cómo aprende tu hijo</b> de ' + esc(h.first_name) + '. Es obligatorio para dejar su recorrido bien armado. <button type="button" class="boton-mini" data-test="' + esc(h.id) + '">Hacerlo ahora</button></div>');
      else if (pasaron6Meses(t.fecha)) out.push('<div class="test-aviso">Pasaron más de 6 meses del último test de ' + esc(h.first_name) + '. Conviene repetirlo. <button type="button" class="boton-mini" data-test="' + esc(h.id) + '">Repetir el test</button></div>');
    });
    return out.join('');
  }

  function abrirTest(hijo, d, alTerminar, obligatorio) {
    var fondo = document.createElement('div');
    fondo.className = 'tst-fondo';
    document.body.appendChild(fondo);
    document.body.style.overflow = 'hidden';
    var resp = {}, diag = '';
    function cerrar() { fondo.remove(); document.body.style.overflow = ''; if (alTerminar) alTerminar(); }

    function pintarPreguntas(error) {
      fondo.innerHTML = '<div class="tst-caja" role="dialog" aria-label="Cómo aprende ' + esc(hijo.nombre) + '">' +
        (obligatorio ? '' : '<button type="button" class="tst-x" data-t="salir" aria-label="Cerrar">✕</button>') +
        '<h2>Cómo aprende ' + esc(hijo.nombre) + '</h2>' +
        '<p class="tst-intro">Respondé pensando en cómo es <b>hoy</b>, no en un diagnóstico. No hay respuestas buenas ni malas: con esto armamos su recorrido. Son 20 preguntas.</p>' +
        T_PREG.map(function (q, i) {
          return '<fieldset class="tst-preg' + (error && resp[i] === undefined ? ' falta' : '') + '"><legend><span>' + (i + 1) + '.</span> ' + esc(q[1]) + '</legend><div class="tst-opc">' +
            T_OPC.map(function (o) { return '<label><input type="radio" name="tq' + i + '" value="' + o[1] + '"' + (resp[i] === o[1] ? ' checked' : '') + '><span>' + o[0] + '</span></label>'; }).join('') + '</div></fieldset>';
        }).join('') +
        '<div class="tst-diag"><label for="tst-d"><b>¿Tiene algún diagnóstico?</b> <small>(opcional)</small></label>' +
          '<p>Si lo tiene, escribilo. Lo guardamos para poder armar mejores adaptaciones. Lo ven solo la familia, el equipo de Wave y su tutor, nunca el alumno.</p>' +
          '<textarea id="tst-d" rows="2" maxlength="300" placeholder="Por ejemplo: dislexia, TDAH… o dejalo vacío">' + esc(diag) + '</textarea></div>' +
        (error ? '<p class="mensaje">Faltan respuestas: respondé todas las preguntas marcadas.</p>' : '') +
        '<button type="button" class="boton" data-t="ver">Ver resultado</button></div>';
    }

    async function verResultado() {
      var res = calcularTest(resp, diag);
      var fam = d.famId;
      var ins = await sb.from('test_aprendizaje').insert({
        student_id: hijo.id, family_id: fam, respuestas: resp, puntajes: res.puntajes,
        diagnostico: diag || null, trayectos: res.trayectos, ajustes: res.ajustes
      }).select('id').single();
      var testId = ins.data ? ins.data.id : null;
      var tr = res.trayectos, nom = esc(hijo.nombre);
      var lista = tr.length ? tr.map(function (c) {
        var t = (d.trayectos || []).filter(function (x) { return x.clave === c; })[0] || { nombre: c, descripcion: '' };
        return '<div class="tst-tray"><b>' + esc(t.nombre) + '</b><p>' + esc(t.descripcion) + '</p>' +
          '<h4>Qué va a encontrar ' + nom + ' en Wave</h4>' + adaptacionesHtml(d, c) + '</div>';
      }).join('') : (function () { var t = (d.trayectos || []).filter(function (x) { return x.clave === 'convencional'; })[0]; return '<div class="tst-tray"><b>Convencional</b><p>' + esc(t ? t.descripcion : 'Recorrido estándar de Wave.') + '</p></div>'; })();
      var conApoyo = tr.length > 0;
      fondo.innerHTML = '<div class="tst-caja" role="dialog">' +
        '<h2>' + (conApoyo ? 'Armamos un recorrido pensado para ' + nom : 'El recorrido de ' + nom) + '</h2>' +
        (conApoyo
          ? '<p class="tst-intro">Gracias por contarnos cómo aprende ' + nom + '. Con tus respuestas preparamos ' + (tr.length > 1 ? 'una combinación de dos recorridos' : 'un recorrido') + ' para que estudiar le resulte más tranquilo y más fácil.</p>' +
            '<p class="tst-reco"><b>Te recomendamos seguirlo</b>, porque es lo que mejor se ajusta a lo que nos contaste. Igual es <b>totalmente opcional</b>: vos decidís, y lo podés cambiar o desactivar cuando quieras.</p>'
          : '<p class="tst-intro">Según tus respuestas, ' + nom + ' puede seguir el recorrido estándar de Wave. Si más adelante notás que algo le cuesta, podés repetir el test y sumar apoyos.</p>') +
        lista +
        (res.muchas ? '<p class="tst-nota">Notamos que hay varias áreas que le cuestan. Además de esto, te sugerimos hablar con Dirección o con su tutor, así armamos un acompañamiento a su medida.</p>' : '') +
        (conApoyo ? '<p class="tst-intro">Si lo aceptás, queda todo listo en el panel de ' + nom + ' y empieza a verlo desde su próxima sesión. Y siempre tiene a mano la lectura en voz alta de los PDF, el dictado por voz y la letra más grande.</p>' : '') +
        '<div class="tst-acc">' +
          (conApoyo ? '<button type="button" class="boton" data-t="aplicar">Sí, quiero este recorrido para ' + nom + '</button>' +
            '<button type="button" class="boton-mini tst-sec" data-t="conv">Prefiero el recorrido estándar</button>'
            : '<button type="button" class="boton" data-t="conv">Dejar el recorrido estándar</button>') +
          '<button type="button" class="tst-luego" data-t="luego">Lo decido después</button>' +
        '</div></div>';
      fondo._res = res; fondo._testId = testId;
    }

    async function aplicar(btn, conv) {
      var res = fondo._res;
      if (conv) res = { trayectos: [], ajustes: {} };
      var txtBtn = btn.textContent; btn.disabled = true; btn.textContent = 'Guardando…';
      var cur = await sb.from('students').select('apoyos').eq('id', hijo.id).maybeSingle();
      var apoyos = Object.assign({}, (cur.data && cur.data.apoyos) || {}, res.ajustes);
      var claves = adaptacionesDe(d, res.trayectos).map(function (a) { return a.clave; });
      var u = await sb.from('students').update({ trayectos_apoyo: res.trayectos, apoyos: apoyos, adaptaciones: claves }).eq('id', hijo.id);
      if (fondo._testId) await sb.from('test_aprendizaje').update({ aplicado: !u.error }).eq('id', fondo._testId);
      if (u.error) { btn.disabled = false; btn.textContent = txtBtn; alert('No se pudo guardar. Probá de nuevo.'); return; }
      cerrar();
    }

    fondo.addEventListener('change', function (ev) {
      var r = ev.target.closest && ev.target.closest('input[type=radio]');
      if (r) { resp[Number(r.name.slice(2))] = Number(r.value); var fs = r.closest('fieldset'); if (fs) fs.classList.remove('falta'); }
    });
    fondo.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-t]');
      if (!b) return;
      var a = b.getAttribute('data-t');
      if (a === 'salir') { fondo.remove(); document.body.style.overflow = ''; }
      else if (a === 'ver') {
        var ta = fondo.querySelector('#tst-d'); diag = ta ? ta.value.trim() : '';
        if (T_PREG.some(function (_, i) { return resp[i] === undefined; })) { pintarPreguntas(true); var f = fondo.querySelector('.falta'); if (f) f.scrollIntoView({ block: 'center' }); return; }
        b.disabled = true; verResultado();
      }
      else if (a === 'aplicar') aplicar(b, false);
      else if (a === 'conv') aplicar(b, true);
      else if (a === 'luego') { fondo.remove(); document.body.style.overflow = ''; if (alTerminar) alTerminar(); }
    });
    pintarPreguntas(false);
  }

  async function vistaAltas() {
    vista.innerHTML = '<a class="mf-banner" href="#propuesta"><span class="mf-banner-k">Nuestra propuesta</span>' +
      '<b>Cómo enseñamos en Wave y por qué</b><span class="mf-banner-ir">Leer el manifiesto →</span></a>' +
      '<h1 class="vista-titulo">Altas</h1><div id="altas"></div>';
    var cont = document.getElementById('altas');
    cont.innerHTML = '<div class="vacio">Cargando…</div>';
    try {
      pintarAltas(cont, await cargarDatos());
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar esta sección. Probá recargar la página.</div>';
    }
  }

  // ---------- Progreso ----------
  function colorSeguro(c) {
    return /^#[0-9a-fA-F]{6}$/.test(c || '') ? c : '#6366F1';
  }

  // "Hoy, 20:43" · "Ayer, 09:10" · "Hace 3 días" · "Todavía no ingresó"
  function textoConexion(iso) {
    if (!iso) return 'Todavía no ingresó';
    var f = new Date(iso);
    if (isNaN(f.getTime())) return 'Sin datos';
    var ahora = new Date();
    var d0 = new Date(ahora.getFullYear(), ahora.getMonth(), ahora.getDate());
    var d1 = new Date(f.getFullYear(), f.getMonth(), f.getDate());
    var dias = Math.round((d0 - d1) / 86400000);
    var hora = String(f.getHours()).padStart(2, '0') + ':' + String(f.getMinutes()).padStart(2, '0');
    if (dias <= 0) return 'Hoy, ' + hora;
    if (dias === 1) return 'Ayer, ' + hora;
    if (dias < 7) return 'Hace ' + dias + ' días';
    return f.toLocaleDateString('es-AR', { day: 'numeric', month: 'short', year: 'numeric' });
  }

  async function cargarProgreso() {
    var res = await Promise.all([
      sb.from('students')
        .select('id, first_name, last_name, created_at, grades(name, levels(name)), profiles!students_profile_id_fkey(last_seen_at)')
        .order('created_at', { ascending: true }),
      sb.rpc('family_progress')
    ]);
    res.forEach(function (r) { if (r.error) throw r.error; });

    var porHijo = {};
    (res[1].data || []).forEach(function (r) {
      (porHijo[r.student_id] = porHijo[r.student_id] || []).push(r);
    });

    return (res[0].data || []).map(function (h) {
      var materias = (porHijo[h.id] || []).map(function (r) {
        return {
          nombre: r.subject_name, color: colorSeguro(r.color), orden: r.subject_position,
          total: r.total_topics, hechas: r.done_topics,
          suma: Number(r.score_sum), notas: r.score_count,
          promedio: r.score_count ? Math.round(Number(r.score_sum) / r.score_count) : null
        };
      }).sort(function (a, b) { return a.orden - b.orden; });

      var total = 0, hechas = 0, suma = 0, notas = 0;
      materias.forEach(function (m) { total += m.total; hechas += m.hechas; suma += m.suma; notas += m.notas; });

      return {
        id: h.id, nombre: h.first_name + ' ' + h.last_name,
        anio: h.grades ? etiquetaAnio(h.grades) : '',
        conexion: h.profiles ? h.profiles.last_seen_at : null,
        materias: materias,
        pct: total ? Math.round((hechas / total) * 100) : 0,
        promedio: notas ? Math.round(suma / notas) : null
      };
    });
  }

  function pintarProgreso(cont, hijos) {
    if (!hijos.length) {
      cont.innerHTML = '<div class="vacio">Todavía no diste de alta a ningún hijo. Cuando lo hagas, acá vas a ver cómo avanza.</div>';
      return;
    }

    cont.innerHTML = hijos.map(function (h) {
      var ini = h.nombre.split(' ').map(function (p) { return p.charAt(0); }).slice(0, 2).join('').toUpperCase();

      var filas = h.materias.map(function (m) {
        var pct = m.total ? Math.round((m.hechas / m.total) * 100) : 0;
        return '<div class="pm-fila" style="--c:' + m.color + '">' +
          '<div class="pm-cab"><span class="pm-nombre">' + esc(m.nombre) + '</span>' +
            '<span class="pm-prom"><small>Promedio</small><b>' + (m.promedio == null ? '—' : m.promedio + '%') + '</b></span></div>' +
          '<div class="pm-barra" role="progressbar" aria-label="Progreso en ' + esc(m.nombre) + '" aria-valuemin="0" aria-valuemax="100" aria-valuenow="' + pct + '"><span style="width:' + pct + '%"></span></div>' +
          '<div class="pm-pie"><span>' + m.hechas + ' de ' + m.total + (m.total === 1 ? ' tema' : ' temas') + '</span><b>' + pct + '%</b></div>' +
        '</div>';
      }).join('');

      return '<section class="pr-hijo">' +
        '<div class="pr-hero">' +
          '<div class="pr-hero-top"><div class="hijo-ini pr-ini">' + esc(ini) + '</div>' +
            '<div><h2>' + esc(h.nombre) + '</h2><span class="pr-anio">' + esc(h.anio) + '</span></div></div>' +
          '<div class="pr-stats">' +
            '<div class="pr-stat"><small>Última conexión</small><b>' + esc(textoConexion(h.conexion)) + '</b></div>' +
            '<div class="pr-stat"><small>Progreso</small><b>' + h.pct + '%</b></div>' +
            '<div class="pr-stat"><small>Promedio general</small><b>' + (h.promedio == null ? '—' : h.promedio + '%') + '</b></div>' +
          '</div>' +
        '</div>' +
        '<div class="pr-materias">' +
          (filas || '<div class="vacio">Todavía no tiene materias habilitadas.</div>') +
        '</div>' +
      '</section>';
    }).join('');
  }

  // Registro de las prácticas diarias de apoyo (cálculo y lectura) de cada hijo
  async function pintarPracticas(cont) {
    var desde = new Date(Date.now() - 30 * 86400000).toISOString().slice(0, 10);
    var r = await Promise.all([
      sb.from('students').select('id, first_name'),
      sb.from('practica_lectura').select('student_id, dia, nivel, total, bien, dificiles, ppm').gte('dia', desde).order('created_at', { ascending: false }).limit(200),
      sb.from('practica_calculo').select('student_id, dia, nivel, correctas, total').gte('dia', desde).order('dia', { ascending: false }).limit(200)
    ]);
    var lec = r[1].data || [], cal = r[2].data || [];
    if (!lec.length && !cal.length) return;
    var NIV = ['', 'palabras cortas', 'palabras más largas', 'frases cortas', 'frases más largas', 'texto corto', 'texto de un párrafo'];
    var html = '<section class="prog-practicas"><h2>Práctica de apoyo (últimos 30 días)</h2>';
    (r[0].data || []).forEach(function (h) {
      var L = lec.filter(function (x) { return x.student_id === h.id; }), C = cal.filter(function (x) { return x.student_id === h.id; });
      if (!L.length && !C.length) return;
      html += '<div class="prog-pr-hijo"><h3>' + esc(h.first_name) + '</h3>';
      if (L.length) {
        var dif = {}; L.slice(0, 6).forEach(function (x) { (x.dificiles || []).forEach(function (w) { dif[w] = (dif[w] || 0) + 1; }); });
        var ppms = L.filter(function (x) { return x.ppm; }).map(function (x) { return Math.round(x.ppm); });
        html += '<p><b>Lectura:</b> ' + L.length + (L.length === 1 ? ' práctica' : ' prácticas') + '. Nivel actual: ' + (NIV[L[0].nivel] || L[0].nivel) + '. Última: ' + L[0].bien + ' de ' + L[0].total + ' bien leídos' +
          (ppms.length ? '. Palabras por minuto (de la más vieja a la más nueva): ' + ppms.slice(0, 8).reverse().join(' → ') : '') + '.' +
          (Object.keys(dif).length ? ' Les cuestan: ' + esc(Object.keys(dif).slice(0, 8).join(', ')) + '.' : '') + '</p>';
      }
      if (C.length) html += '<p><b>Cálculo:</b> ' + C.length + (C.length === 1 ? ' día' : ' días') + ' de práctica. Último: ' + C[0].correctas + ' aciertos de ' + C[0].total + ', nivel ' + C[0].nivel + '.</p>';
      html += '</div>';
    });
    cont.insertAdjacentHTML('beforeend', html + '<p class="prog-pr-nota">La lectura se registra con el reconocimiento de voz del navegador: es una guía y puede equivocarse. La medición formal la hace el tutor.</p></section>');
  }

  async function vistaProgreso() {
    vista.innerHTML = '<h1 class="vista-titulo">Progreso</h1><div id="progreso"></div>';
    var cont = document.getElementById('progreso');
    cont.innerHTML = '<div class="vacio">Cargando…</div>';
    try {
      pintarProgreso(cont, await cargarProgreso());
      try { await pintarPracticas(cont); } catch (e2) { /* sin registro de prácticas */ }
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar el progreso. Probá recargar la página.</div>';
    }
  }

  // ---------- Programación (una por cada hijo, igual a la del panel estudiante) ----------
  var DIAS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'];

  var P = {
    mate: '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h.01M12 12h.01M16 12h.01M8 16h.01M12 16h.01M16 16h.01"/>',
    lengua: '<path d="M2 4h7a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H2zM22 4h-7a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h8z"/>',
    natural: '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.1-6C9.5 14.5 12 13 13 12"/>',
    fisica: '<circle cx="12" cy="12" r="1.5"/><ellipse cx="12" cy="12" rx="10" ry="4"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(120 12 12)"/>',
    quimica: '<path d="M9 3h6M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2h12.4a1.5 1.5 0 0 0 1.3-2L14 9V3"/><path d="M7.5 15h9"/>',
    historia: '<path d="M3 21h18M5 21V10M9 21V10M15 21V10M19 21V10M2 10l10-6 10 6z"/>',
    geografia: '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20z"/>',
    ingles: '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/>',
    arte: '<path d="M12 22a10 10 0 1 1 10-10c0 3-2 4-4 4h-2a2 2 0 0 0-1.5 3.3c.6.7.4 2.7-2.5 2.7z"/><path d="M7.5 11h.01M10.5 7h.01M15.5 8h.01"/>',
    bienestar: '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7z"/>',
    ciudadania: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
    economia: '<path d="M3 17l6-6 4 4 8-8"/><path d="M14 7h7v7"/>',
    tecnologia: '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    oficios: '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
    proyecto: '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5M9 18h6M10 22h4"/>'
  };

  var REGLAS = [
    ['fisico', 'quimica'], ['quimic', 'quimica'], ['fisic', 'fisica'],
    ['biolog', 'natural'], ['naturales', 'natural'],
    ['sociales', 'historia'], ['histor', 'historia'],
    ['geograf', 'geografia'], ['ingles', 'ingles'],
    ['matemat', 'mate'], ['lengua', 'lengua'], ['literatura', 'lengua'],
    ['arte', 'arte'], ['bienestar', 'bienestar'],
    ['ciudadan', 'ciudadania'], ['filosof', 'ciudadania'],
    ['econom', 'economia'], ['tecnolog', 'tecnologia'],
    ['oficio', 'oficios'], ['taller', 'oficios'], ['proyecto', 'proyecto']
  ];

  function iconoMateria(nombre) {
    var n = String(nombre || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
    var clave = 'lengua';
    for (var i = 0; i < REGLAS.length; i++) {
      if (n.indexOf(REGLAS[i][0]) !== -1) { clave = REGLAS[i][1]; break; }
    }
    return '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + P[clave] + '</svg>';
  }

  function fechaLarga(d) {
    return d.toLocaleDateString('es-AR', { day: 'numeric', month: 'long', year: 'numeric' });
  }
  function fechaCorta(d) {
    return d.toLocaleDateString('es-AR', { day: 'numeric', month: 'short', year: 'numeric' });
  }
  function textoLecciones(n) { return n + (n === 1 ? ' lección' : ' lecciones'); }

  // Día en que se terminan los temas que faltan, siguiendo el programa (de lunes a viernes)
  // Se cuentan 40 semanas activas por año (hay vacaciones y feriados): el calendario real es 52/40 más largo
  var FACTOR_CALENDARIO = 52 / 40;

  // Inicio (primer ingreso) + plazo elegido = fecha objetivo
  function fechaObjetivo(inicio, meses) {
    if (!inicio || !meses) return null;
    var f = new Date(inicio);
    f.setMonth(f.getMonth() + meses);
    f.setHours(12, 0, 0, 0);
    return isNaN(f.getTime()) ? null : f;
  }

  function fechaFin(restantes, porDia) {
    var hoy = new Date();
    hoy.setHours(12, 0, 0, 0);
    var d = new Date(hoy);
    for (var i = 0; i < 3650; i++) {
      var wd = d.getDay();
      if (wd >= 1 && wd <= 5) {
        restantes -= porDia[wd];
        if (restantes <= 0) return new Date(hoy.getTime() + (d - hoy) * FACTOR_CALENDARIO);
      }
      d.setDate(d.getDate() + 1);
    }
    return null;
  }

  function semanasDeRetraso(fin, limite) {
    return Math.ceil((fin - limite) / 86400000 / 7);
  }

  var COLS_PROG = 'id, weekday, subject_id, lessons_target, position';

  async function cargarProgramaciones() {
    var ses = await sb.auth.getSession();
    var uid = ses.data.session.user.id;

    var res = await Promise.all([
      sb.from('students')
        .select('id, first_name, last_name, created_at, started_at, target_months, grades(name, levels(name))')
        .order('created_at', { ascending: true }),
      sb.rpc('family_progress'),
      sb.from('study_schedule').select('student_id, ' + COLS_PROG).order('position'),
      sb.from('subject_load_config').select('subject_id, lessons_total'),
      sb.from('student_subject_progress').select('student_id, subject_id, completed_lessons')
    ]);
    res.slice(0, 4).forEach(function (r) { if (r.error) throw r.error; });

    var lecciones = {};
    (res[3].data || []).forEach(function (x) { lecciones[x.subject_id] = x.lessons_total; });

    var hechasDe = {};
    (res[4].data || []).forEach(function (r) {
      (hechasDe[r.student_id] = hechasDe[r.student_id] || {})[r.subject_id] = r.completed_lessons;
    });

    var cursosDe = {}, filasDe = {};
    (res[1].data || []).forEach(function (r) {
      (cursosDe[r.student_id] = cursosDe[r.student_id] || []).push({
        id: r.subject_id, nombre: r.subject_name, color: colorSeguro(r.color), orden: r.subject_position,
        total: r.total_topics, completas: r.done_topics
      });
    });
    (res[2].data || []).forEach(function (f) {
      (filasDe[f.student_id] = filasDe[f.student_id] || []).push(f);
    });

    var hijos = (res[0].data || []).map(function (h) {
      return {
        id: h.id, nombre: h.first_name + ' ' + h.last_name, primerNombre: h.first_name,
        anio: h.grades ? etiquetaAnio(h.grades) : '',
        iniciado: h.started_at, meses: h.target_months,
        finAnio: null, lecciones: lecciones, hechasLecc: hechasDe[h.id] || {},
        cursos: (cursosDe[h.id] || []).sort(function (a, b) { return a.orden - b.orden; }),
        filas: filasDe[h.id] || []
      };
    });
    return { hijos: hijos, uid: uid };
  }

  // Programación de un hijo: dibuja y edita sobre su propio contenedor
  function crearProgramacion(cont, hijo, uid) {
    var prog = { cursos: hijo.cursos, filas: hijo.filas, ocupado: false };

    function cursoPorId(id) {
      return prog.cursos.filter(function (c) { return c.id === id; })[0];
    }

    // Fecha objetivo = primer ingreso + semanas que pide la tabla del año con la programación semanal:
    // lecciones del año de cada materia ÷ lecciones por semana (manda la materia que más tarda)
    function recalcularObjetivo() {
      hijo.finAnio = null;
      if (!hijo.iniciado || !hijo.meses) return;
      var semanas = 0;
      prog.cursos.forEach(function (c) {
        var total = hijo.lecciones[c.id];
        if (!total) return;
        var sem = 0;
        prog.filas.forEach(function (f) { if (f.subject_id === c.id) sem += f.lessons_target; });
        if (sem > 0) semanas = Math.max(semanas, Math.ceil(total / sem));
      });
      if (!semanas) { hijo.finAnio = fechaObjetivo(hijo.iniciado, hijo.meses); return; }
      var f = new Date(hijo.iniciado);
      f.setHours(12, 0, 0, 0);
      if (isNaN(f.getTime())) return;
      f.setDate(f.getDate() + Math.round(semanas * 7 * FACTOR_CALENDARIO));
      hijo.finAnio = f;
    }

    function trayectoria() {
      var finAnio = hijo.finAnio;
      var filasCursos = [], finGlobal = null, sinProgramar = [], restantesTotal = 0, hayLecciones = false;

      prog.cursos.forEach(function (c) {
        var porDia = [0, 0, 0, 0, 0, 0], semanal = 0;
        prog.filas.forEach(function (f) {
          if (f.subject_id === c.id) { porDia[f.weekday] += f.lessons_target; semanal += f.lessons_target; }
        });
        var tot = hijo.lecciones[c.id] || 0;
        var hechasL = hijo.hechasLecc[c.id] || 0;
        var restantes = Math.max(0, tot - hechasL);
        var r = { curso: c, tot: tot, hechas: hechasL, restantes: restantes, semanal: semanal, estado: '', clase: 'neutro', texto: '' };

        if (tot === 0) {
          r.texto = 'Todavía no tiene lecciones cargadas';
        } else {
          hayLecciones = true;
          restantesTotal += restantes;
          if (restantes === 0) {
            r.estado = 'Completada'; r.clase = 'ok';
          } else if (semanal === 0) {
            r.texto = 'No está en la programación'; r.clase = 'atraso';
            sinProgramar.push(c.nombre);
          } else {
            var fin = fechaFin(restantes, porDia);
            if (!fin) {
              r.texto = 'Con este ritmo falta muchísimo: conviene sumar lecciones por semana'; r.clase = 'atraso';
            } else {
              if (!finGlobal || fin > finGlobal) finGlobal = fin;
              r.texto = 'Termina el ' + fechaLarga(fin) + ' · ' + textoLecciones(semanal) + ' por semana';
              if (finAnio && fin > finAnio) {
                r.estado = 'Necesita ' + semanasDeRetraso(fin, finAnio) + ' sem. más'; r.clase = 'atraso';
              } else {
                r.estado = 'A tiempo'; r.clase = 'ok';
              }
            }
          }
        }
        filasCursos.push(r);
      });

      return { filas: filasCursos, finGlobal: finGlobal, sinProgramar: sinProgramar,
               restantesTotal: restantesTotal, hayLecciones: hayLecciones };
    }

    function htmlHero(t) {
      var finAnio = hijo.finAnio;
      var hoy = new Date();
      hoy.setHours(12, 0, 0, 0);
      var nota = t.sinProgramar.length
        ? '<p class="tray-nota">Falta programar: ' + esc(t.sinProgramar.join(', ')) + '.</p>' : '';

      if (!t.hayLecciones) {
        return '<div class="tray-hero"><p class="tray-vacio">Todavía no hay lecciones cargadas en sus materias. ' +
          'Cuando las haya, acá vas a ver cuándo terminaría el año con este programa.</p></div>';
      }
      if (t.restantesTotal === 0) {
        return '<div class="tray-hero ok"><b class="tray-fecha">¡Completó todas las lecciones del año!</b></div>';
      }
      if (!t.finGlobal) {
        return '<div class="tray-hero atraso"><b class="tray-fecha">Programá sus materias para calcular cuándo termina</b>' + nota + '</div>';
      }

      var atrasado = finAnio && t.finGlobal > finAnio;
      var pill = '';
      if (finAnio) {
        pill = atrasado
          ? '<span class="tray-pill atraso">+' + semanasDeRetraso(t.finGlobal, finAnio) + ' semanas más que la fecha objetivo</span>'
          : '<span class="tray-pill ok">Llega a tiempo</span>';
      }

      var linea = '';
      if (finAnio && finAnio > hoy) {
        var pos = Math.min(100, Math.max(0, ((t.finGlobal - hoy) / (finAnio - hoy)) * 100));
        linea = '<div class="tray-linea"><div class="tray-relleno" style="width:' + pos.toFixed(1) + '%"></div>' +
          '<span class="tray-pin" style="left:' + pos.toFixed(1) + '%"></span></div>' +
          '<div class="tray-extremos"><span>Hoy</span><span>Fecha objetivo · ' + esc(fechaCorta(finAnio)) + '</span></div>';
      }

      return '<div class="tray-hero ' + (atrasado ? 'atraso' : 'ok') + '">' +
        '<div class="tray-hero-top"><div><span class="tray-etiqueta">Terminaría el año el</span>' +
        '<b class="tray-fecha">' + esc(fechaLarga(t.finGlobal)) + '</b></div>' + pill + '</div>' +
        linea +
        '<p class="tray-faltan">Le faltan <b>' + textoLecciones(t.restantesTotal) + '</b> en total.' +
        (atrasado ? ' Para llegar a la fecha objetivo, pueden sumar lecciones por día.' : '') + '</p>' + nota + '</div>';
    }

    // Fecha objetivo de finalización: la elige solo la familia
    function htmlMeta(t) {
      var OPC = [[12, 'Un año'], [18, 'Año y medio'], [24, 'Dos años']];
      var botones = OPC.map(function (o) {
        var sel = hijo.meses === o[0];
        return '<button type="button" class="meta-btn' + (sel ? ' sel' : '') + '" data-a="plazo" data-m="' + o[0] + '" aria-pressed="' + sel + '">' + o[1] + '</button>';
      }).join('');

      var estado;
      if (!hijo.iniciado) {
        estado = 'El plazo empieza a correr cuando ' + esc(hijo.primerNombre) + ' ingrese por primera vez.';
      } else if (!hijo.meses || !hijo.finAnio) {
        estado = 'Elegí un plazo para ver si llega a tiempo.';
      } else {
        estado = 'Fecha objetivo: <b>' + esc(fechaLarga(hijo.finAnio)) + '</b> · contando desde su primer ingreso (' + esc(fechaCorta(new Date(hijo.iniciado))) + '), según las lecciones de cada materia del año y la programación semanal.';
        var hoy = new Date();
        var semanas = ((hijo.finAnio - hoy) / 86400000 / 7) / FACTOR_CALENDARIO;
        if (t.restantesTotal > 0) {
          if (semanas <= 0) {
            estado += ' <b>El plazo ya venció.</b>';
          } else {
            var necesario = t.restantesTotal / semanas;
            var programado = 0;
            t.filas.forEach(function (r) { if (r.restantes > 0) programado += r.semanal; });
            estado += ' Para llegar a tiempo necesita unos <b>' + necesario.toLocaleString('es-AR', { maximumFractionDigits: 1 }) +
              ' lecciones por semana</b> en total; hoy tiene programados <b>' + programado + '</b>.';
          }
        }
      }

      return '<section class="meta">' +
        '<div><span class="meta-rot">Fecha objetivo de finalización</span>' +
        '<p class="meta-preg">¿En cuánto tiempo querés que ' + esc(hijo.primerNombre) + ' termine el año completo?</p></div>' +
        '<div class="meta-opc" role="group" aria-label="Plazo">' + botones + '</div>' +
        '<div class="meta-acciones"><button type="button" class="meta-reset" data-a="restablecer">Restablecer programación recomendada</button></div>' +
        '<p class="meta-estado">' + estado + '</p></section>';
    }

    function pintar() {
      recalcularObjetivo();
      var hoySemana = new Date().getDay();

      var dias = DIAS.map(function (nombre, i) {
        var wd = i + 1;
        var delDia = prog.filas.filter(function (f) { return f.weekday === wd; })
          .sort(function (a, b) { return a.position - b.position; });
        var usadas = {}, suma = 0;
        delDia.forEach(function (f) { usadas[f.subject_id] = true; suma += f.lessons_target; });

        var items = delDia.map(function (f) {
          var c = cursoPorId(f.subject_id);
          if (!c) return '';
          return '<div class="prog-item" style="--c:' + c.color + '">' +
            '<button type="button" class="prog-x" data-a="quitar" data-id="' + f.id + '" aria-label="Quitar ' + esc(c.nombre) + '">×</button>' +
            '<span class="prog-ico">' + iconoMateria(c.nombre) + '</span>' +
            '<b class="prog-nombre">' + esc(c.nombre) + '</b>' +
            '<div class="prog-cant">' +
            '<button type="button" data-a="menos" data-id="' + f.id + '" aria-label="Una lección menos">−</button>' +
            '<span><strong>' + f.lessons_target + '</strong> ' + (f.lessons_target === 1 ? 'lección' : 'lecciones') + '</span>' +
            '<button type="button" data-a="mas" data-id="' + f.id + '" aria-label="Una lección más">+</button>' +
            '</div></div>';
        }).join('');

        var libres = prog.cursos.filter(function (c) { return !usadas[c.id]; });
        var agregar = libres.length
          ? '<div class="prog-add"><button type="button" class="prog-add-btn" data-a="menu">+ Agregar materia</button>' +
            '<div class="prog-menu" hidden>' + libres.map(function (c) {
              return '<button type="button" data-a="agregar" data-dia="' + wd + '" data-mat="' + c.id + '">' +
                '<i style="background:' + c.color + '"></i>' + esc(c.nombre) + '</button>';
            }).join('') + '</div></div>'
          : '';

        return '<section class="dia' + (hoySemana === wd ? ' hoy' : '') + '">' +
          '<header class="dia-cab"><h2>' + nombre + '</h2>' +
          (hoySemana === wd ? '<span class="dia-hoy">Hoy</span>' : '') +
          '<small>' + (suma ? textoLecciones(suma) : 'Sin lecciones') + '</small></header>' +
          '<div class="dia-cuerpo">' + items + agregar + '</div></section>';
      }).join('');

      var t = trayectoria();
      var filasT = t.filas.map(function (r) {
        var c = r.curso;
        var pct = r.tot ? Math.min(100, Math.round((r.hechas / r.tot) * 100)) : 0;
        var info = r.texto || (r.restantes === 0 ? 'Sin lecciones pendientes' : '');
        return '<div class="tray-fila" style="--c:' + c.color + '">' +
          '<span class="tray-ico">' + iconoMateria(c.nombre) + '</span>' +
          '<div class="tray-info"><b>' + esc(c.nombre) + '</b>' +
          (info ? '<span>' + esc(info) + '</span>' : '') +
          (r.tot ? '<div class="tray-mini"><span style="width:' + pct + '%"></span></div>' : '') + '</div>' +
          (r.estado ? '<span class="tray-estado ' + r.clase + '">' + esc(r.estado) + '</span>' : '') +
          '</div>';
      }).join('');

      cont.innerHTML =
        htmlMeta(t) +
        '<div class="semana">' + dias + '</div>' +
        '<h3 class="vista-subtitulo">Trayectoria</h3>' +
        htmlHero(t) +
        '<div class="tray-lista">' + filasT + '</div>';
    }

    function filaPorId(id) {
      return prog.filas.filter(function (f) { return String(f.id) === String(id); })[0];
    }

    async function guardar(fn) {
      if (prog.ocupado) return;
      prog.ocupado = true;
      try { await fn(); }
      catch (e) { alert('No pudimos guardar el cambio. Probá de nuevo.'); }
      prog.ocupado = false;
      pintar();
    }

    async function cambiarCantidad(id, delta) {
      var f = filaPorId(id);
      if (!f) return;
      var n = Math.max(1, Math.min(20, f.lessons_target + delta));
      if (n === f.lessons_target) return;
      var r = await sb.from('study_schedule').update({ lessons_target: n, updated_by: uid })
        .eq('id', f.id).select('id');
      if (r.error || !r.data.length) throw (r.error || new Error('sin permiso'));
      f.lessons_target = n;
    }

    async function quitarFila(id) {
      var r = await sb.from('study_schedule').delete().eq('id', id).select('id');
      if (r.error || !r.data.length) throw (r.error || new Error('sin permiso'));
      prog.filas = prog.filas.filter(function (f) { return String(f.id) !== String(id); });
    }

    async function elegirPlazo(meses) {
      var r = await sb.rpc('set_student_target', { p_student: hijo.id, p_months: meses });
      if (r.error) throw r.error;
      hijo.meses = meses;
      // La base rearma la programación recomendada para el nuevo plazo
      await recargarFilas();
    }

    async function agregarFila(dia, materiaId) {
      var pos = prog.filas.filter(function (f) { return f.weekday === dia; }).length;
      var r = await sb.from('study_schedule').insert({
        student_id: hijo.id, weekday: dia, subject_id: materiaId,
        lessons_target: 1, position: pos, updated_by: uid
      }).select(COLS_PROG);
      if (r.error) throw r.error;
      prog.filas = prog.filas.concat(r.data);
    }

    // Trae de nuevo la programación guardada
    async function recargarFilas() {
      var r = await sb.from('study_schedule').select(COLS_PROG).eq('student_id', hijo.id).order('position');
      if (r.error) throw r.error;
      prog.filas = r.data || [];
    }

    // Programa recomendado: lo arma la base según la carga de cada materia y el plazo elegido
    async function armarProgramaRecomendado() {
      var r = await sb.rpc('apply_recommended_schedule', { p_student: hijo.id });
      if (r.error) throw r.error;
      await recargarFilas();
    }

    async function restablecer() {
      if (prog.filas.length && !confirm('Se reemplaza la programación actual por la recomendada. ¿Seguimos?')) return;
      await armarProgramaRecomendado();
    }

    cont.addEventListener('click', function (ev) {
      var b = ev.target.closest('button[data-a]');
      if (!b || b.getAttribute('data-a') !== 'menu') {
        cont.querySelectorAll('.prog-menu').forEach(function (m) { m.hidden = true; });
      }
      if (!b) return;
      var a = b.getAttribute('data-a');
      var id = b.getAttribute('data-id');
      if (a === 'menu') {
        var menu = b.nextElementSibling;
        var abrir = menu.hidden;
        cont.querySelectorAll('.prog-menu').forEach(function (m) { m.hidden = true; });
        menu.hidden = !abrir;
      }
      else if (a === 'mas') guardar(function () { return cambiarCantidad(id, 1); });
      else if (a === 'menos') guardar(function () { return cambiarCantidad(id, -1); });
      else if (a === 'quitar') guardar(function () { return quitarFila(id); });
      else if (a === 'plazo') {
        var meses = Number(b.getAttribute('data-m'));
        if (meses === hijo.meses) return;
        if (prog.filas.length && !confirm('Al cambiar el plazo, la programación se reemplaza por la recomendada para ese plazo. ¿Seguimos?')) return;
        guardar(function () { return elegirPlazo(meses); });
      }
      else if (a === 'restablecer') guardar(restablecer);
      else if (a === 'agregar') {
        var dia = Number(b.getAttribute('data-dia'));
        var mat = b.getAttribute('data-mat');
        guardar(function () { return agregarFila(dia, mat); });
      }
    });

    return {
      iniciar: async function () {
        if (!prog.filas.length && prog.cursos.length) {
          try { await armarProgramaRecomendado(); } catch (e) { /* queda vacío y se agrega a mano */ }
        }
        pintar();
      }
    };
  }

  async function vistaProgramacion() {
    vista.innerHTML = '<h1 class="vista-titulo">Programación</h1><div id="programacion"></div>';
    var cont = document.getElementById('programacion');
    cont.innerHTML = '<div class="vacio">Cargando…</div>';
    try {
      var d = await cargarProgramaciones();
      if (!d.hijos.length) {
        cont.innerHTML = '<div class="vacio">Todavía no diste de alta a ningún hijo. Cuando lo hagas, acá vas a armar su programación.</div>';
        return;
      }
      cont.innerHTML = d.hijos.map(function (h, i) {
        var ini = h.nombre.split(' ').map(function (p) { return p.charAt(0); }).slice(0, 2).join('').toUpperCase();
        return '<section class="pg-hijo">' +
          '<div class="pg-cab"><div class="hijo-ini">' + esc(ini) + '</div>' +
          '<div><h2>' + esc(h.nombre) + '</h2><span>' + esc(h.anio) + '</span></div></div>' +
          '<div id="prog-' + i + '">' +
            (h.cursos.length ? '' : '<div class="vacio">Todavía no tiene materias habilitadas.</div>') +
          '</div></section>';
      }).join('');

      for (var i = 0; i < d.hijos.length; i++) {
        var h = d.hijos[i];
        if (!h.cursos.length) continue;
        await crearProgramacion(document.getElementById('prog-' + i), h, d.uid).iniciar();
      }
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar la programación. Probá recargar la página.</div>';
    }
  }

  // ---------- Facturación (una suscripción de Mercado Pago por hijo) ----------
  var ESTADO_SUSC = {
    active: ['Activa', 'ok'],
    pending: ['Pendiente de activación', 'pend'],
    past_due: ['Pago pendiente', 'atraso'],
    suspended: ['Suspendida', 'atraso'],
    cancelled: ['Cancelada', 'neutro']
  };

  var ESTADO_PAGO = {
    approved: ['Pagado', 'ok'], authorized: ['Pagado', 'ok'],
    pending: ['En proceso', 'pend'], in_process: ['En proceso', 'pend'],
    rejected: ['Rechazado', 'atraso'], charged_back: ['Contracargo', 'atraso'],
    cancelled: ['Cancelado', 'neutro'], refunded: ['Reembolsado', 'neutro']
  };

  function dinero(n, moneda) {
    if (n == null || Number(n) === 0) return '—';
    try {
      return new Intl.NumberFormat('es-AR', { style: 'currency', currency: moneda || 'ARS',
        minimumFractionDigits: 0, maximumFractionDigits: 2 }).format(Number(n));
    } catch (e) {
      return '$ ' + Number(n).toLocaleString('es-AR');
    }
  }

  function fechaODash(v) {
    if (!v) return '—';
    var d = new Date(v);
    return isNaN(d.getTime()) ? '—' : fechaCorta(d);
  }

  function htmlPagos(pagos) {
    if (!pagos || !pagos.length) {
      return '<p class="fa-sin-pagos">Todavía no hay pagos registrados.</p>';
    }
    return '<ul class="fa-hist">' + pagos.map(function (p) {
      var e = ESTADO_PAGO[p.status] || ['Otro', 'neutro'];
      return '<li><span class="fa-h-fecha">' + esc(fechaODash(p.paid_at || p.created_at)) + '</span>' +
        '<b class="fa-h-monto">' + esc(dinero(p.amount, 'ARS')) + '</b>' +
        '<span class="fa-pill ' + e[1] + '">' + esc(e[0]) + '</span></li>';
    }).join('') + '</ul>';
  }

  function htmlSuscripcion(s) {
    var est = ESTADO_SUSC[s.status] || [String(s.status || ''), 'neutro'];
    var aviso = '';
    if (s.status === 'past_due') {
      aviso = '<p class="fa-aviso atraso">No pudimos cobrar la última cuota.' +
        (s.grace_until ? ' Tenés hasta el <b>' + esc(fechaLarga(new Date(s.grace_until))) + '</b> para regularizarlo.' : '') + '</p>';
    } else if (s.status === 'suspended') {
      aviso = '<p class="fa-aviso atraso">La suscripción está suspendida.</p>';
    } else if (s.status === 'cancelled') {
      aviso = '<p class="fa-aviso">Suscripción cancelada' + (s.cancelled_at ? ' el ' + esc(fechaODash(s.cancelled_at)) : '') + '.</p>';
    } else if (s.status === 'pending') {
      aviso = '<p class="fa-aviso">Todavía no se confirmó el primer pago.</p>';
    }
    var cobra = s.status === 'active' || s.status === 'past_due';
    return '<div class="fa-top"><span class="fa-pill ' + est[1] + '">' + esc(est[0]) + '</span></div>' +
      '<div class="fa-datos">' +
        '<div class="fa-dato"><small>Monto mensual</small><b>' + esc(dinero(s.amount, s.currency)) + '</b></div>' +
        '<div class="fa-dato"><small>Próximo cobro</small><b>' + esc(cobra ? fechaODash(s.next_payment_date) : '—') + '</b></div>' +
        '<div class="fa-dato"><small>Último pago</small><b>' + esc(fechaODash(s.last_payment_at)) + '</b></div>' +
      '</div>' + aviso +
      '<h3 class="fa-sub">Historial de pagos</h3>' + htmlPagos(s.payments);
  }

  // ---------- Pagar: matrícula anual y nuevas suscripciones (precios de la tabla tarifas, vía mp-cobros) ----------
  var NOMBRE_NIVEL = { inicial: 'Nivel Inicial', medio: 'Nivel Medio', avanzado: 'Nivel Avanzado' };
  var NOMBRE_MOD = { libre: 'Libre', guiada: 'Guiada', completa: 'Completa', personalizada: 'Personalizada' };
  var ORDEN_NIVEL = ['inicial', 'medio', 'avanzado'], ORDEN_MOD = ['libre', 'guiada', 'completa', 'personalizada'];
  function usd(n) { return 'US$ ' + Number(n).toLocaleString('es-AR', { maximumFractionDigits: 2 }); }

  async function cargarCompra() {
    var box = document.getElementById('fa-compra');
    if (!box) return;
    box.innerHTML = '<div class="vacio">Cargando precios…</div>';
    var r = await sb.functions.invoke('mp-cobros', { body: { action: 'precios' } });
    if (r.error || !r.data || r.data.error) { box.innerHTML = ''; return; }
    var P = r.data, m = P.matricula, arg = (PAIS_FAM || 'Argentina') === 'Argentina';
    var porNivel = {};
    (P.tarifas || []).forEach(function (t) { (porNivel[t.nivel] = porNivel[t.nivel] || []).push(t); });
    var niveles = ORDEN_NIVEL.filter(function (n) { return porNivel[n]; });
    box.innerHTML =
      '<p class="fa-pais">País: <b>' + esc(PAIS_FAM || 'Argentina') + '</b> · ' + (arg ? 'pagás en pesos con Mercado Pago' : 'pagás en dólares con PayPal') +
        ' · <button type="button" class="fa-link" id="fa-cambiar-pais">Cambiar</button></p>' +
      '<section class="fa-card"><h2>Matrícula ' + (m.anio || new Date().getFullYear()) + '</h2>' +
        (m.pagada ? '<p class="fa-aviso">✓ La matrícula ' + (m.anio || '') + ' ya está paga.</p>'
          : arg ? '<p class="fa-intro">' + esc(dinero(m.monto_ars, 'ARS')) + ' por año, en hasta ' + m.cuotas_max + ' cuotas con tarjeta' + (m.anticipada ? ' (precio por pago antes de febrero)' : '') + '.</p>' +
              '<button type="button" class="boton fa-boton" id="fa-pagar-mat">Pagar con Mercado Pago</button>'
            : '<p class="fa-intro">' + esc(usd(m.monto_usd * RECARGO_PAYPAL)) + ' por año, en un pago (incluye 5% de costo de gestión del pago internacional)' + (m.anticipada ? ' (precio por pago antes de febrero)' : '') + '.</p>' +
              '<button type="button" class="boton fa-boton fa-pp" id="fa-pagar-mat-pp">Pagar con PayPal</button>') +
      '</section>' +
      '<section class="fa-card"><h2>Sumar una suscripción</h2>' +
        '<p class="fa-intro">Cada hijo necesita una suscripción mensual del nivel que va a cursar. Elegí el nivel y la modalidad:</p>' +
        '<div class="fa-compra"><select id="fa-nivel" aria-label="Nivel">' + niveles.map(function (n) { return '<option value="' + n + '">' + NOMBRE_NIVEL[n] + '</option>'; }).join('') + '</select>' +
        '<select id="fa-mod" aria-label="Modalidad"></select></div>' +
        '<p class="fa-precio" id="fa-precio"></p>' +
        (arg ? '<button type="button" class="boton fa-boton" id="fa-pagar-sus">Pagar con Mercado Pago</button>'
          : '<button type="button" class="boton fa-boton fa-pp" id="fa-pagar-sus-pp">Pagar con PayPal</button>') +
        '<p class="fa-aviso" id="fa-err" hidden></p>' +
      '</section>';
    var selN = document.getElementById('fa-nivel'), selM = document.getElementById('fa-mod'), precio = document.getElementById('fa-precio'), err = document.getElementById('fa-err');
    function tarifa() { return (porNivel[selN.value] || []).filter(function (t) { return t.modalidad === selM.value; })[0]; }
    function mods() {
      var ts = (porNivel[selN.value] || []).slice().sort(function (a, b) { return ORDEN_MOD.indexOf(a.modalidad) - ORDEN_MOD.indexOf(b.modalidad); });
      selM.innerHTML = ts.map(function (t) { return '<option value="' + t.modalidad + '">' + NOMBRE_MOD[t.modalidad] + '</option>'; }).join('');
      verPrecio();
    }
    function verPrecio() { var t = tarifa(); precio.innerHTML = !t ? '' : arg ? '<b>' + esc(dinero(t.cuota_mensual_ars, 'ARS')) + ' por mes</b>' : '<b>' + esc(usd(t.cuota_mensual_usd * RECARGO_PAYPAL)) + ' por mes</b> <small>(incluye 5% de costo de gestión del pago internacional)</small>'; }
    selN.addEventListener('change', mods); selM.addEventListener('change', verPrecio); mods();
    async function ir(body, btn, fn) {
      err.hidden = true; btn.disabled = true; var txt = btn.textContent; btn.textContent = 'Preparando el pago…';
      var x = await sb.functions.invoke(fn || 'mp-cobros', { body: body });
      if (x.error || !x.data || x.data.error || !x.data.url) {
        err.textContent = (x.data && x.data.error) || (x.error ? await mensajeDeError(x.error) : 'No se pudo preparar el pago.'); err.hidden = false;
        btn.disabled = false; btn.textContent = txt; return;
      }
      window.location.href = x.data.url;
    }
    var bs = document.getElementById('fa-pagar-sus'), bsp = document.getElementById('fa-pagar-sus-pp');
    if (bs) bs.addEventListener('click', function () { ir({ action: 'suscribir', nivel: selN.value, modalidad: selM.value }, this); });
    if (bsp) bsp.addEventListener('click', function () { ir({ action: 'suscribir', nivel: selN.value, modalidad: selM.value }, this, 'paypal'); });
    document.getElementById('fa-cambiar-pais').addEventListener('click', async function () { if (await preguntarPais(false)) cargarCompra(); });
    var bm = document.getElementById('fa-pagar-mat'), bmp = document.getElementById('fa-pagar-mat-pp');
    if (bm) bm.addEventListener('click', function () { ir({ action: 'matricula' }, this); });
    if (bmp) bmp.addEventListener('click', function () { ir({ action: 'matricula' }, this, 'paypal'); });
  }

  // Pagos: en Argentina, por transferencia; en otros países, suscripción y matrícula con PayPal (precio + 5%)
  function vistaPagos() {
    if (PAIS_FAM && PAIS_FAM !== 'Argentina') return vistaFacturacion();
    return WavePagos.vista(vista);
  }
  var RECARGO_PAYPAL = 1.05;
  async function vistaFacturacion() {
    vista.innerHTML = '<h1 class="vista-titulo">Pagos</h1><div id="facturacion"></div>';
    var cont = document.getElementById('facturacion');
    cont.innerHTML = '<div class="vacio">Cargando…</div>';
    try {
      var res = await Promise.all([
        sb.from('students')
          .select('id, first_name, last_name, created_at, grades(name, levels(name))')
          .order('created_at', { ascending: true }),
        sb.rpc('family_billing')
      ]);
      res.forEach(function (r) { if (r.error) throw r.error; });

      var hijos = res[0].data || [];
      var susc = res[1].data || [];
      var porHijo = {}, sueltas = [];
      susc.forEach(function (s) {
        if (s.student_id) porHijo[s.student_id] = s; else sueltas.push(s);
      });

      if (!hijos.length && !sueltas.length) {
        cont.innerHTML = '<div id="fa-compra"></div><div class="vacio">Todavía no tenés suscripciones. Cuando pagues una, acá vas a ver su estado y sus pagos.</div>';
        cargarCompra();
        return;
      }

      var total = 0, moneda = 'ARS';
      susc.forEach(function (s) {
        if ((s.status === 'active' || s.status === 'past_due') && s.amount) { total += Number(s.amount); moneda = s.currency || moneda; }
      });

      var html = '<p class="fa-intro">Cada hijo tiene su propia suscripción mensual de Mercado Pago.</p>';
      if (total > 0) {
        html += '<div class="fa-total"><small>Total mensual</small><b>' + esc(dinero(total, moneda)) + '</b></div>';
      }

      html += hijos.map(function (h) {
        var nombre = h.first_name + ' ' + h.last_name;
        var ini = nombre.split(' ').map(function (p) { return p.charAt(0); }).slice(0, 2).join('').toUpperCase();
        var s = porHijo[h.id];
        return '<section class="fa-card">' +
          '<div class="pg-cab"><div class="hijo-ini">' + esc(ini) + '</div>' +
          '<div><h2>' + esc(nombre) + '</h2><span>' + esc(h.grades ? etiquetaAnio(h.grades) : '') + '</span></div></div>' +
          (s ? htmlSuscripcion(s) : '<p class="fa-aviso">Todavía no tiene una suscripción asociada.</p>') +
        '</section>';
      }).join('');

      var libres = sueltas.filter(function (s) { return s.status === 'active' || s.status === 'past_due'; });
      if (libres.length) {
        html += '<section class="fa-card"><h2 class="fa-libre">Suscripciones sin hijo asignado</h2>' +
          '<p class="fa-aviso">Tenés ' + libres.length + (libres.length === 1 ? ' suscripción disponible' : ' suscripciones disponibles') +
          '. Podés usarla para dar de alta a un hijo en <a href="#altas">Altas</a>.</p></section>';
      }

      cont.innerHTML = '<div id="fa-compra"></div>' + html;
      cargarCompra();
    } catch (e) {
      cont.innerHTML = '<div class="vacio">No pudimos cargar la facturación. Probá recargar la página.</div>';
    }
  }

  // ---------- Tutorías mensuales (todas las modalidades) y oficios (Completa) ----------
  var MODS = { libre: 'Libre', guiada: 'Guiada', completa: 'Completa', personalizada: 'Personalizada' };
  function fechaTurno(v) {
    var d = new Date(v);
    return d.toLocaleDateString('es-AR', { weekday: 'long', day: 'numeric', month: 'long' }) + ' · ' + d.toLocaleTimeString('es-AR', { hour: '2-digit', minute: '2-digit' }) + ' h';
  }
  async function vistaTutorias() {
    vista.innerHTML = '<h1 class="vista-titulo">Turnos y tutorías</h1><section class="fa-card" id="tuf-dir"><div class="vacio">Cargando…</div></section><section class="fa-card" id="tuf-ind"></section><div id="tuf"><div class="vacio">Cargando…</div></div>';
    var cont = document.getElementById('tuf');
    var h = await sb.from('students').select('id, first_name, last_name, grade_id, trayecto_clave').order('created_at');
    if (h.error) { cont.innerHTML = '<div class="vacio">No pudimos cargar los datos.</div>'; return; }
    pintarDireccion(document.getElementById('tuf-dir'), h.data);
    if (window.WaveTutInd) WaveTutInd.pintar(document.getElementById('tuf-ind'), (PAIS_FAM || 'Argentina') !== 'Argentina');
    if (!h.data.length) { cont.innerHTML = '<div class="vacio">Todavía no diste de alta a ningún hijo.</div>'; return; }
    var TOPES = (await sb.rpc('tutorias_por_mes')).data || {};
    var partes = await Promise.all(h.data.map(async function (a) {
      var t = await sb.rpc('mi_tutor', { p_student: a.id });
      var info = (t.data && t.data[0]) || { modalidad: 'libre', nombre: null };
      return { a: a, mod: info.modalidad, tutor: info.nombre };
    }));
    cont.innerHTML = partes.map(function (p) {
      var a = p.a, nombre = a.first_name + ' ' + a.last_name;
      var html = '<section class="fa-card" data-alu="' + a.id + '"><h2>' + esc(nombre) + '</h2><span class="tu-sub">Modalidad ' + esc(MODS[p.mod] || p.mod) + '</span>';
      html += '<p class="fa-intro">' + (p.tutor ? 'Su tutor es <b>' + esc(p.tutor) + '</b>. Tiene ' + (TOPES[p.mod] || 2) + ' tutorías por mes para consultar dudas.' : 'Todavía no tiene tutor asignado: te avisamos apenas lo tenga.') + '</p>' +
        '<div class="tuf-mis"></div>' + (p.tutor ? '<div class="tuf-reservar"></div>' : '');
      if (p.mod === 'completa' || p.mod === 'personalizada') html += '<h3 class="fa-sub">Oficios</h3><div class="tuf-oficios"></div>';
      return html + '</section>';
    }).join('');
    partes.forEach(function (p) {
      var card = cont.querySelector('[data-alu="' + p.a.id + '"]');
      pintarMisTutorias(card, p.a.id);
      if (p.tutor) pintarReserva(card, p.a.id);
      if (p.mod === 'completa' || p.mod === 'personalizada') pintarOficios(card, p.a);
    });
  }
  var AVISO_LLAMADA = '<p class="fa-aviso">La videollamada se abre en el navegador o en la app Jitsi Meet, sin crear cuenta. Si te pide que esperes al moderador, es que todavía no entró: pasás apenas se conecte.</p>';
  var MOTIVOS = ['Inscripción', 'Pagos y facturación', 'Aprendizaje de mi hijo/a', 'Otro'];
  async function pintarDireccion(box, hijos) {
    var r = await Promise.all([sb.rpc('mis_turnos_direccion'), sb.rpc('turnos_direccion', { p_dias: 21 })]);
    var ts = r[0].data || [], slots = r[1].data || [], ahora = Date.now();
    var prox = ts.filter(function (t) { return t.estado === 'reservada' && new Date(t.fin).getTime() > ahora; }).reverse();
    var pasadas = ts.filter(function (t) { return t.estado !== 'reservada'; }).slice(0, 3);
    var html = '<h2>Hablar con dirección</h2><p class="fa-intro">¿Tenés una consulta sobre la inscripción, los pagos o cómo va tu hijo/a? Pedí un turno de videollamada con la dirección de la escuela.</p>';
    if (prox.length) html += '<h3 class="fa-sub">Tus turnos</h3>' + prox.map(function (t) {
      return '<div class="tuf-turno"><b>' + esc(fechaTurno(t.inicio)) + '</b> · ' + esc(t.motivo) + (t.tema ? ' · ' + esc(t.tema) : '') +
        '<div class="fa-botones"><a class="boton fa-boton" href="' + esc(t.link) + '" target="_blank" rel="noopener">Entrar a la videollamada</a>' +
        '<button type="button" class="tu-link" data-reagendar="' + t.id + '">Reagendar</button>' +
        '<button type="button" class="tu-link" data-cancelar="' + t.id + '">Cancelar</button></div></div>';
    }).join('') + AVISO_LLAMADA;
    if (pasadas.length) html += '<h3 class="fa-sub">Últimos turnos</h3>' + pasadas.map(function (t) {
      return '<p class="tu-tema"><b>' + esc(fechaTurno(t.inicio)) + ' · ' + esc(t.motivo) + ':</b> ' + (t.estado === 'ausente' ? 'no te conectaste.' : esc(t.notas || 'realizado.')) + '</p>';
    }).join('');
    if (prox.length >= 2) html += '<p class="fa-aviso">Ya tenés 2 turnos pedidos. Cuando pase uno, podés pedir otro.</p>';
    else if (!slots.length) html += '<p class="fa-aviso">No hay turnos libres con dirección en las próximas 3 semanas. Volvé a mirar en unos días.</p>';
    else {
      var porDia = {};
      slots.forEach(function (s) { var k = new Date(s.inicio).toLocaleDateString('es-AR', { weekday: 'long', day: 'numeric', month: 'long' }); (porDia[k] = porDia[k] || []).push(s); });
      html += '<h3 class="fa-sub">Pedir un turno</h3>' +
        '<div class="tuf-campos"><select class="tuf-motivo"><option value="">Motivo…</option>' + MOTIVOS.map(function (m) { return '<option>' + m + '</option>'; }).join('') + '</select>' +
        (hijos.length ? '<select class="tuf-hijo"><option value="">Sobre la familia en general</option>' + hijos.map(function (a) { return '<option value="' + a.id + '">Sobre ' + esc(a.first_name) + '</option>'; }).join('') + '</select>' : '') + '</div>' +
        Object.keys(porDia).slice(0, 10).map(function (d) {
          return '<p class="tuf-dia">' + esc(d) + '</p><div class="tu-slots">' + porDia[d].map(function (s) {
            return '<button type="button" class="tu-slot" data-ini="' + esc(s.inicio) + '">' + new Date(s.inicio).toLocaleTimeString('es-AR', { hour: '2-digit', minute: '2-digit' }) + '</button>';
          }).join('') + '</div>';
        }).join('') +
        '<input class="tuf-tema" maxlength="500" placeholder="Contanos brevemente tu consulta (opcional)">' +
        '<button type="button" class="boton fa-boton" data-reservar disabled>Pedir turno</button><p class="fa-aviso tuf-err" hidden></p>';
    }
    box.innerHTML = html;
    var elegido = null;
    box.onclick = async function (ev) {
      var b;
      if ((b = ev.target.closest('[data-reagendar]'))) {
        return WaveCal.reagendarFamilia({ id: b.getAttribute('data-reagendar'), tipo: 'direccion' }, function () { pintarDireccion(box, hijos); });
      }
      if ((b = ev.target.closest('[data-cancelar]'))) {
        if (!confirm('¿Cancelar este turno con dirección?')) return;
        var x = await sb.rpc('cancelar_tutoria', { p_id: b.getAttribute('data-cancelar') });
        if (x.error) { alert(x.error.message); return; }
        return pintarDireccion(box, hijos);
      }
      if ((b = ev.target.closest('.tu-slot'))) {
        box.querySelectorAll('.tu-slot').forEach(function (s) { s.classList.toggle('on', s === b); });
        elegido = b.getAttribute('data-ini'); box.querySelector('[data-reservar]').disabled = false; return;
      }
      if ((b = ev.target.closest('[data-reservar]')) && elegido) {
        var err = box.querySelector('.tuf-err'), motivo = box.querySelector('.tuf-motivo').value, hijo = box.querySelector('.tuf-hijo');
        if (!motivo) { err.textContent = 'Elegí el motivo de la consulta.'; err.hidden = false; return; }
        b.disabled = true;
        var y = await sb.rpc('reservar_direccion', { p_inicio: elegido, p_motivo: motivo, p_detalle: box.querySelector('.tuf-tema').value || null, p_student: (hijo && hijo.value) || null });
        if (y.error) { err.textContent = y.error.message; err.hidden = false; b.disabled = false; return; }
        pintarDireccion(box, hijos);
      }
    };
  }
  async function pintarMisTutorias(card, alu) {
    var box = card.querySelector('.tuf-mis');
    var r = await sb.rpc('mis_tutorias', { p_student: alu });
    var ts = (r.data || []), ahora = Date.now();
    var prox = ts.filter(function (t) { return t.estado === 'reservada' && new Date(t.fin).getTime() > ahora; }).reverse();
    var pasadas = ts.filter(function (t) { return t.estado !== 'reservada'; }).slice(0, 3);
    box.innerHTML = (prox.length ? '<h3 class="fa-sub">Próximas tutorías</h3>' + prox.map(function (t) {
        return '<div class="tuf-turno"><b>' + esc(fechaTurno(t.inicio)) + '</b>' + (t.tema ? ' · ' + esc(t.tema) : '') +
          '<div class="fa-botones"><a class="boton fa-boton" href="' + esc(t.link) + '" target="_blank" rel="noopener">Entrar a la videollamada</a>' +
          '<button type="button" class="tu-link" data-reagendar="' + t.id + '">Reagendar</button>' +
          '<button type="button" class="tu-link" data-cancelar="' + t.id + '">Cancelar</button></div></div>';
      }).join('') + AVISO_LLAMADA : '') +
      (pasadas.length ? '<h3 class="fa-sub">Últimas tutorías</h3>' + pasadas.map(function (t) {
        return '<p class="tu-tema"><b>' + esc(fechaTurno(t.inicio)) + ':</b> ' + (t.estado === 'ausente' ? 'no se conectó.' : esc(t.notas_tutor || 'realizada.')) + '</p>';
      }).join('') : '');
    box.onclick = async function (ev) {
      var rg = ev.target.closest('[data-reagendar]');
      if (rg) return WaveCal.reagendarFamilia({ id: rg.getAttribute('data-reagendar'), tipo: 'tutoria', student: alu }, function () { pintarMisTutorias(card, alu); pintarReserva(card, alu); });
      var b = ev.target.closest('[data-cancelar]'); if (!b) return;
      if (!confirm('¿Cancelar esta tutoría?')) return;
      var x = await sb.rpc('cancelar_tutoria', { p_id: b.getAttribute('data-cancelar') });
      if (x.error) { alert(x.error.message); return; }
      pintarMisTutorias(card, alu); pintarReserva(card, alu);
    };
  }
  async function pintarReserva(card, alu) {
    var box = card.querySelector('.tuf-reservar');
    var r = await sb.rpc('turnos_disponibles', { p_student: alu, p_dias: 21 });
    var slots = r.data || [];
    if (!slots.length) { box.innerHTML = '<p class="fa-aviso">No hay turnos libres en las próximas 3 semanas. Volvé a mirar en unos días.</p>'; return; }
    var porDia = {};
    slots.forEach(function (s) { var k = new Date(s.inicio).toLocaleDateString('es-AR', { weekday: 'long', day: 'numeric', month: 'long' }); (porDia[k] = porDia[k] || []).push(s); });
    box.innerHTML = '<h3 class="fa-sub">Reservar una tutoría</h3>' +
      Object.keys(porDia).slice(0, 10).map(function (d) {
        return '<p class="tuf-dia">' + esc(d) + '</p><div class="tu-slots">' + porDia[d].map(function (s) {
          return '<button type="button" class="tu-slot" data-ini="' + esc(s.inicio) + '">' + new Date(s.inicio).toLocaleTimeString('es-AR', { hour: '2-digit', minute: '2-digit' }) + '</button>';
        }).join('') + '</div>';
      }).join('') +
      '<input class="tuf-tema" maxlength="300" placeholder="¿Qué dudas quiere consultar? (opcional)">' +
      '<button type="button" class="boton fa-boton" data-reservar disabled>Reservar turno</button><p class="fa-aviso tuf-err" hidden></p>';
    var elegido = null, btn = box.querySelector('[data-reservar]');
    box.onclick = async function (ev) {
      var s = ev.target.closest('.tu-slot');
      if (s) { box.querySelectorAll('.tu-slot').forEach(function (x) { x.classList.toggle('on', x === s); }); elegido = s.getAttribute('data-ini'); btn.disabled = false; return; }
      if (ev.target.closest('[data-reservar]') && elegido) {
        btn.disabled = true;
        var x = await sb.rpc('reservar_tutoria', { p_student: alu, p_inicio: elegido, p_tema: box.querySelector('.tuf-tema').value || null });
        if (x.error) { var e = box.querySelector('.tuf-err'); e.textContent = x.error.message; e.hidden = false; btn.disabled = false; return; }
        pintarMisTutorias(card, alu); pintarReserva(card, alu);
      }
    };
  }
  async function pintarOficios(card, a) {
    var box = card.querySelector('.tuf-oficios');
    var r = await Promise.all([
      sb.from('subjects').select('id, name, eleccion, oficio_clave').eq('grade_id', a.grade_id).not('eleccion', 'is', null).order('name'),
      sb.from('student_talleres').select('subject_id').eq('student_id', a.id),
      sb.from('app_settings').select('value').eq('key', 'talleres_por_anio').maybeSingle()
    ]);
    var ofs = r[0].data || [];
    if (!ofs.length) { box.innerHTML = '<p class="fa-intro">Los oficios empiezan en el Nivel Avanzado.</p>'; return; }
    var elegidos = (r[1].data || []).map(function (x) { return x.subject_id; });
    var max = (r[2].data && r[2].data.value && r[2].data.value.cantidad) || 2;
    var trayecto = ofs[0].eleccion === 'trayecto';
    box.innerHTML = '<p class="fa-intro">' + (trayecto ? 'Elegí el oficio que va a cursar este año.' : 'Elegí hasta ' + max + ' talleres para este año.') + '</p>' +
      '<div class="tu-slots">' + ofs.map(function (o) {
        var on = trayecto ? o.oficio_clave === a.trayecto_clave : elegidos.indexOf(o.id) >= 0;
        return '<button type="button" class="tu-slot' + (on ? ' on' : '') + '" data-of="' + o.id + '" data-on="' + (on ? 1 : 0) + '">' + esc(o.name.replace(/^Taller: /, '')) + '</button>';
      }).join('') + '</div><p class="fa-aviso tuf-err" hidden></p>';
    box.onclick = async function (ev) {
      var b = ev.target.closest('[data-of]'); if (!b) return;
      var x = await sb.rpc('elegir_oficio', { p_student: a.id, p_subject: b.getAttribute('data-of'), p_elegir: b.getAttribute('data-on') !== '1' });
      if (x.error) { var e = box.querySelector('.tuf-err'); e.textContent = x.error.message; e.hidden = false; return; }
      var h2 = await sb.from('students').select('trayecto_clave').eq('id', a.id).maybeSingle();
      if (h2.data) a.trayecto_clave = h2.data.trayecto_clave;
      pintarOficios(card, a);
    };
  }

  // ---------- Secciones que vienen después ----------
  function proximamente(titulo) {
    return function () {
      vista.innerHTML = '<h1 class="vista-titulo">' + titulo + '</h1>' +
        '<div class="proximamente">Estamos armando esta sección. Muy pronto vas a encontrarla acá.</div>';
    };
  }

  // ---------- Nuestra propuesta (manifiesto) ----------
  function vistaPropuesta() {
    vista.innerHTML = '<article class="manifiesto"><p class="mf-k">Nuestra propuesta</p>' +
      '<h1 class="mf-titulo">Cómo enseñamos en Wave Academy</h1>' + (window.MANIFIESTO_HTML || '') + '</article>';
  }

  var VISTAS = {
    propuesta: vistaPropuesta,
    altas: vistaAltas,
    progreso: vistaProgreso,
    programacion: vistaProgramacion,
    pagos: vistaPagos,
    facturacion: vistaPagos,
    tutorias: vistaTutorias,
    juana: function () { if (window.WaveJuana) WaveJuana.vista(vista); }
  };

  function ruta() {
    var nombre = (location.hash || '#altas').slice(1);
    if (!VISTAS[nombre]) nombre = 'altas';
    enlaces.forEach(function (a) {
      a.classList.toggle('activo', a.getAttribute('href') === '#' + nombre);
    });
    VISTAS[nombre]();
  }

  window.addEventListener('hashchange', ruta);
  asegurarPais().then(asegurarContacto).then(ruta);
})();
