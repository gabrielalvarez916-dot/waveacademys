/* Detecta que se publicó una versión nueva y la carga sin esperar.
   Compara los archivos con ?v= de esta página con los de la página publicada. */
(function () {
  function firma(html) {
    var m = html.match(/(?:src|href)="[^"]*\?v=\d+"/g) || [];
    return m.join('|');
  }
  var actual = null, aviso = false;

  function leerActual() {
    var out = [];
    document.querySelectorAll('script[src],link[rel="stylesheet"]').forEach(function (n) {
      var u = n.getAttribute('src') || n.getAttribute('href');
      if (u && /\?v=\d+$/.test(u)) out.push((n.getAttribute('src') ? 'src' : 'href') + '="' + u + '"');
    });
    return out.join('|');
  }

  function banner() {
    if (aviso) return;
    aviso = true;
    var d = document.createElement('div');
    d.setAttribute('role', 'status');
    d.style.cssText = 'position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:99999;background:#0b3b3c;color:#fff;padding:10px 16px;border-radius:999px;font:700 14px system-ui,sans-serif;box-shadow:0 4px 18px rgba(0,0,0,.25);display:flex;gap:12px;align-items:center';
    d.innerHTML = '<span>Hay una versión nueva</span><button type="button" style="background:#7fe0c4;color:#0b3b3c;border:0;border-radius:999px;padding:6px 14px;font:800 14px system-ui,sans-serif;cursor:pointer">Actualizar</button>';
    d.querySelector('button').onclick = function () { location.reload(); };
    document.body.appendChild(d);
  }

  async function revisar(recargarYa) {
    try {
      var r = await fetch(location.pathname + '?_=' + Date.now(), { cache: 'no-store' });
      if (!r.ok) return;
      var nueva = firma(await r.text());
      if (!nueva) return;
      if (actual === null) actual = leerActual();
      if (nueva !== actual) { if (recargarYa) location.reload(); else banner(); }
    } catch (e) { /* sin conexión: se reintenta */ }
  }

  window.addEventListener('load', function () { setTimeout(function () { revisar(true); }, 1500); });
  document.addEventListener('visibilitychange', function () { if (!document.hidden) revisar(true); });
  setInterval(function () { revisar(false); }, 60000);
})();
