// Uso: node assemble.js specs/archivo.js  → escribe out/MisionNN_Avanzado_MatematicaI_A_o1_<slug>.html
const fs=require('fs'),path=require('path'),vm=require('vm');
const dir=__dirname;
const specPath=path.resolve(process.argv[2]);
const lib=fs.readFileSync(path.join(dir,'lib.js'),'utf8');
const engine=fs.readFileSync(path.join(dir,'engine.js'),'utf8');
const spec=fs.readFileSync(specPath,'utf8');
const base=fs.readFileSync(path.join(dir,'base_raiz.html'),'utf8');

// CSS idéntico al del molde (paleta, tarjeta, selector, pulso, etc.) + fracciones
const css=base.match(/<style>([\s\S]*?)<\/style>/)[1]+
`.fr{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.1;margin:0 2px}
.fr i{font-style:normal;padding:0 4px}.fr i:first-child{border-bottom:2px solid currentColor}
`;

const ctx=vm.createContext({});
const S=vm.runInContext(lib+'\n'+spec+'\n;SPEC',ctx);
const pm=S.modes.length>1;
const ctrlInputs=S.inputs.map(i=>`<span><label for="in_${i.id}">${i.label}</label> <input class="n" id="in_${i.id}" inputmode="numeric" maxlength="${i.max||3}" aria-label="${i.label}"></span>`).join('\n        ');
const picker=pm?`<span class="pick"><label for="mode">👆 Elegí el tema:</label> <select id="mode" aria-label="Tema">
          ${S.modes.map(m=>`<option value="${m.id}">${m.label}</option>`).join('\n          ')}</select></span>`:'';

const html=`<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>${S.title} – Wave Academy’s</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800&display=swap">
<style>${css}</style>
</head>
<body>
<header class="top"><div class="in"><span class="brand">WAVE ACADEMY’S</span><span class="tag">Matemática</span></div></header>
<div class="wrap">
  <h1>${S.title}</h1>
  <p class="sub">${S.sub}</p>
  <div class="card">
    <div class="left" id="left"></div>
    <div class="scene" aria-live="polite">
      <div class="note" id="note"></div>
      <div class="ctrl">
        ${picker}
        ${ctrlInputs}
        <button class="txt" id="rnd" type="button">🔄 Otro ejercicio</button>
        <span class="sp"></span>
        <button class="txt" id="auto" type="button">Auto</button>
        <div class="nav">
          <button id="prev" type="button" aria-label="Paso anterior">◀</button>
          <button id="next" type="button" aria-label="Paso siguiente">▶</button>
        </div>
      </div>
      <div class="work" id="work"></div>
      <div id="again"><span>¡Terminaste este ejercicio! Probá con otro para practicar.</span><button class="txt" id="rnd2" type="button">🔄 Probar otro ejercicio</button></div>
      <div class="dots" id="dots"></div>
    </div>
  </div>
</div>
<script>
${lib}
${spec}
${engine}
</script>
</body>
</html>
`;
const name=`Mision${String(S.mision).padStart(2,'0')}_Avanzado_MatematicaI_A_o1_${S.slug}.html`;
const out=path.join(dir,'out',name);
fs.writeFileSync(out,html);
console.log(out);
