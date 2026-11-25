// Misión 16 · L2 · Ecuaciones de la forma ax + b = c (selector: con suma / con resta)
const SPEC={
  mision:16, slug:'ecuaciones-de-la-forma-ax-b-c',
  title:'Ecuaciones de la forma ax + b = c',
  sub:'Despejamos la incógnita deshaciendo las operaciones en orden inverso',
  inputs:[{id:'a',label:'a',max:2},{id:'b',label:'b',max:2},{id:'c',label:'c',max:3}],
  modes:[
    {id:'mas',label:'ax + b = c',def:{a:3,b:5,c:20},
     left:`<p>Una <b>ecuación</b> es una igualdad con una incógnita (x). Resolverla es hallar el valor de x que la hace verdadera.</p><p>En <b>ax + b = c</b> a x primero lo multiplicaron por a y después le sumaron b. Para despejar, <b>deshacemos en orden inverso</b>: primero restamos b y después dividimos por a.</p><p>Ejemplo: 3x + 5 = 20 → 3x = 15 → x = 5.</p><p><b>Ojo:</b> lo que se hace de un lado se hace <b>en los dos miembros</b>.</p><p>Tocá el botón siguiente para avanzar, o escribí tus propios números.</p>`},
    {id:'menos',label:'ax − b = c',def:{a:4,b:7,c:21},
     left:`<p>En <b>ax − b = c</b> a x primero lo multiplicaron por a y después le restaron b. Para despejar, <b>deshacemos en orden inverso</b>: primero sumamos b y después dividimos por a.</p><p>Ejemplo: 4x − 7 = 21 → 4x = 28 → x = 7.</p><p><b>Ojo:</b> para deshacer una resta se suma, y se suma en los dos miembros.</p><p>Tocá el botón siguiente para avanzar, o escribí tus propios números.</p>`}],
  norm(mode,r){
    const a=clamp(r.a,2,12),b=clamp(r.b,1,30),c0=clamp(r.c,1,400);
    let x;
    if(mode==='mas')x=Math.max(1,Math.round((c0-b)/a));
    else x=Math.max(Math.ceil((b+1)/a),Math.round((c0+b)/a));
    x=Math.min(x,40);
    const c=mode==='mas'?a*x+b:a*x-b;
    return{a,b,c};
  },
  rand(mode,v){
    let o;
    do{const a=R_(2,12),b=R_(1,30),x=R_(1,20);
       o={a,b,c:mode==='mas'?a*x+b:Math.max(1,a*x-b)};
       o=SPEC.norm(mode,o);
    }while(o.a===v.a&&o.b===v.b&&o.c===v.c);
    return o;
  },
  truth(mode,v){return String((mode==='mas'?v.c-v.b:v.c+v.b)/v.a);},
  build(mode,v){
    const mas=mode==='mas',{a,b,c}=v,s=mas?'+':'−';
    const A=mas?c-b:c+b,x=A/a,T=`${a}x ${s} ${b} = ${c}`;
    const lado=mas?`${a}x + ${b} − ${b} = ${c} − ${b}`:`${a}x − ${b} + ${b} = ${c} + ${b}`;
    const izq=mas?`${a} × ${x} + ${b} = ${a*x} + ${b} = ${c}`:`${a} × ${x} − ${b} = ${a*x} − ${b} = ${c}`;
    const S=[
      {h:`Vamos a resolver <b>${T}</b>. Hay que encontrar el valor de x que hace verdadera la igualdad.`},
      {h:`Miramos qué le hicieron a x: primero la multiplicaron por <b>${a}</b> y después le ${mas?'sumaron':'restaron'} <b>${b}</b>. Para despejar, deshacemos <b>en orden inverso</b>: primero ${mas?'restamos':'sumamos'} ${b} y después dividimos por ${a}.`,
       row:[T,`a = ${a} · b = ${b} · c = ${c}`],c:205,l:T},
      {h:`Deshacemos ${mas?'la suma':'la resta'}: ${mas?'restamos':'sumamos'} <b>${b}</b> <b>en los dos miembros</b>. ${lado}, y queda <b>${a}x = ${A}</b>.`,
       row:[lado,`${a}x = ${A}`],c:35,l:`${a}x = ${A}`},
      {h:`Deshacemos la multiplicación: dividimos por <b>${a}</b> los dos miembros. ${a}x ÷ ${a} = ${A} ÷ ${a}, entonces <b>x = ${x}</b>.`,
       row:[`${A} ÷ ${a}`,`x = ${x}`],c:50,l:`x = ${A} ÷ ${a} = ${x}`},
      {h:`Comprobamos reemplazando x por ${x} en la ecuación original: ${izq}. ¡Da ${c}, igual que el segundo miembro!`,
       row:[izq,`${c} = ${c} ✓`],c:160,l:`${izq} ✓`},
      {h:`¡Listo! La solución de <b>${T}</b> es <b>x = ${x}</b>. Comprobación: al reemplazar x por ${x}, los dos miembros valen ${c}.`,
       row:[T,`x = ${x}`],c:280,l:`x = ${x}`}];
    return{T,end:` → x = ${x}`,rs:5,S,res:String(x)};
  }
};
