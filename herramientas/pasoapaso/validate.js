// Uso: node validate.js out/archivo.html specs/archivo.js
// Abre el HTML en un navegador, prueba cada modo y compara con spec.truth() (cuenta por otro camino)
const fs=require('fs'),path=require('path'),vm=require('vm');
const {chromium}=require('playwright');
const [,, htmlPath, specPath, nStr]=process.argv;
const N=parseInt(nStr||'60',10);
const lib=fs.readFileSync(path.join(__dirname,'lib.js'),'utf8');
const SPEC=vm.runInContext(lib+'\n'+fs.readFileSync(specPath,'utf8')+'\n;SPEC',vm.createContext({}));
(async()=>{
  const b=await chromium.launch(),errs=[],fails=[];let checks=0;
  const p=await b.newPage({viewport:{width:1100,height:800}});
  p.on('pageerror',e=>errs.push(String(e)));
  p.on('console',m=>{if(m.type()==='error'&&!/fonts\.googleapis|ERR_/.test(m.text()))errs.push(m.text());});
  await p.goto('file://'+path.resolve(htmlPath));
  const state=()=>p.evaluate(()=>({v:window.__v,mode:window.__mode,res:window.__M.res,steps:window.__M.S.length,
    note:document.getElementById('note').textContent,big:document.getElementById('work').querySelector('.big').textContent}));
  const check=async(tag)=>{
    const s=await state();checks++;
    const t=SPEC.truth(s.mode,s.v);
    if(String(s.res)!==String(t))fails.push(`${tag} ${s.mode} ${JSON.stringify(s.v)}: pantalla=${s.res} correcto=${t}`);
    // recorrer todos los pasos
    for(let k=0;k<s.steps-1;k++){await p.click('#next');const n=await p.evaluate(()=>document.getElementById('note').textContent.trim());if(!n)fails.push(`${tag} nota vacía paso ${k+1}`);}
    const fin=await state();
    if(!/\d/.test(fin.big)||!fin.note.includes('Listo'))fails.push(`${tag} último paso sin resultado: ${fin.big}`);
    if(await p.evaluate(()=>document.getElementById('next').disabled)===false)fails.push(`${tag} next no se bloquea al final`);
    if(await p.evaluate(()=>!document.getElementById('again').classList.contains('show')))fails.push(`${tag} no aparece "otro ejercicio"`);
  };
  for(const m of SPEC.modes){
    if(SPEC.modes.length>1)await p.selectOption('#mode',m.id);
    await check(`[${m.id}] inicial`);
    for(let i=0;i<N;i++){await p.click('#rnd');await check(`[${m.id}] azar#${i}`);}
    // entradas raras escritas a mano
    const raros=[0,'',1,99,999,12345].map(x=>Object.fromEntries(SPEC.inputs.map(i=>[i.id,x])));
    for(const r of raros){
      for(const i of SPEC.inputs){await p.fill('#in_'+i.id,String(r[i.id]));}
      await p.dispatchEvent('#in_'+SPEC.inputs[SPEC.inputs.length-1].id,'change');
      await check(`[${m.id}] raro ${JSON.stringify(r)}`);
    }
  }
  // Auto y teclado
  await p.click('#rnd');await p.keyboard.press('ArrowRight');await p.keyboard.press('ArrowLeft');
  await p.click('#auto');await p.click('#auto');
  // celular
  await p.setViewportSize({width:375,height:800});
  const ov=await p.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth+1);
  if(ov)fails.push('desborde horizontal en 375px');
  const shot=path.resolve(htmlPath).replace('.html','.png');
  await p.setViewportSize({width:1100,height:900});await p.click('#rnd');
  await p.click('#next');await p.click('#next');await p.click('#next');
  await p.screenshot({path:shot});
  await b.close();
  console.log(`comprobaciones: ${checks} · fallas: ${fails.length} · errores JS: ${errs.length}`);
  fails.slice(0,15).forEach(f=>console.log('FALLA',f));errs.slice(0,5).forEach(e=>console.log('ERR',e));
  console.log('captura:',shot);
  process.exit(fails.length||errs.length?1:0);
})();
