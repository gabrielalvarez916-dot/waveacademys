// Motor común: mismo comportamiento que el archivo de raíces (selector, Otro ejercicio, Auto, flechas, puntitos)
const $=id=>document.getElementById(id);
let mode=SPEC.modes[0].id,v=null,step=0,timer=null,M=null;
const mdef=()=>SPEC.modes.find(m=>m.id===mode);
function render(){
  M=SPEC.build(mode,v);
  window.__M=M;window.__v=v;window.__mode=mode;
  const S=M.S,T_=S.length;
  if(step>T_-1)step=T_-1;
  $("note").innerHTML=S[step].h;
  const cell=(k,c,t)=>step>=k?`<div class="d ${step===k?"on":""}" style="--c:${c}">${t}</div>`:`<div class="d ph"></div>`;
  let g=`<div class="big">${M.T}${step>=M.rs?M.end:""}</div><div class="tbl"><div class="h">cuenta</div><div class="h">resultado</div>`;
  S.forEach((o,k)=>{if(o.row)g+=cell(k,o.c,o.row[0])+cell(k,o.c,o.row[1]);});
  g+=`</div>`;
  const lines=S.map((o,k)=>step>=k&&o.l?`<div class="l ${k===T_-1?"res":(k===step?"cur":"")}">${o.l}</div>`:"").join("");
  $("work").innerHTML=g+`<div class="lines">${lines}</div>`;
  $("prev").disabled=step===0;$("next").disabled=step===T_-1;
  $("again").classList.toggle("show",$("next").disabled);
  $("dots").innerHTML=Array.from({length:T_},(_,k)=>`<i class="${k===step?"a":""}"></i>`).join("");
}
function readRaw(){const o={};SPEC.inputs.forEach(i=>o[i.id]=$("in_"+i.id).value);return o;}
function setVals(raw){
  v=SPEC.norm(mode,raw);
  SPEC.inputs.forEach(i=>$("in_"+i.id).value=v[i.id]);
  step=0;stop();render();
}
function setMode(m){mode=m;$("left").innerHTML=mdef().left;setVals(mdef().def);}
function go(d){const T_=M.S.length;step=Math.max(0,Math.min(T_-1,step+d));render();if(step===T_-1)stop();}
function stop(){if(timer){clearInterval(timer);timer=null;}$("auto").textContent="Auto";}
$("next").onclick=()=>{stop();go(1)};
$("prev").onclick=()=>{stop();go(-1)};
$("rnd").onclick=()=>setVals(SPEC.rand(mode,v));
$("rnd2").onclick=()=>$("rnd").click();
if($("mode")){
  $("mode").onchange=e=>setMode(e.target.value);
  $("mode").addEventListener("change",()=>$("mode").parentNode.classList.add("seen"));
}
$("auto").onclick=()=>{
  if(timer){stop();return;}
  if(step===M.S.length-1){step=0;render();}
  $("auto").textContent="Pausa";timer=setInterval(()=>go(1),3200);
};
SPEC.inputs.forEach(i=>{
  const el=$("in_"+i.id);
  el.addEventListener("input",e=>{e.target.value=e.target.value.replace(/\D/g,"");});
  el.addEventListener("change",()=>setVals(readRaw()));
});
document.addEventListener("keydown",e=>{
  if(e.target.tagName==="INPUT"||e.target.tagName==="SELECT")return;
  if(e.key==="ArrowRight"){stop();go(1)}
  if(e.key==="ArrowLeft"){stop();go(-1)}
});
setMode(SPEC.modes[0].id);
