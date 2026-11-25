// Misión 9 · L1 · Suma y resta de fracciones (selector: sumar / restar)
const SPEC={
  mision:9, slug:'suma-y-resta-de-fracciones',
  title:'Suma y resta de fracciones',
  sub:'Con distinto denominador: buscamos el común, convertimos y operamos',
  inputs:[
    {id:'n1',label:'1.ª fracción',max:2},{id:'d1',label:'÷',max:2},
    {id:'n2',label:'2.ª fracción',max:2},{id:'d2',label:'÷',max:2}],
  modes:[
    {id:'sum',label:'Sumar fracciones',def:{n1:1,d1:4,n2:2,d2:3},
     left:`<p>Para <b>sumar fracciones</b> con distinto denominador, primero las llevamos a un <b>denominador común</b>: el mínimo común múltiplo (mcm) de los denominadores.</p><p>Ejemplo: 1/4 + 2/3 → mcm(4, 3) = 12 → 3/12 + 8/12 = 11/12.</p><p><b>Ojo:</b> 1/4 + 2/3 no es 3/7. No se suman los numeradores con los numeradores ni los denominadores con los denominadores.</p><p>Tocá el botón siguiente para avanzar, o escribí tus propias fracciones.</p>`},
    {id:'res',label:'Restar fracciones',def:{n1:5,d1:6,n2:1,d2:4},
     left:`<p>Para <b>restar fracciones</b> con distinto denominador hacemos lo mismo que para sumar: las llevamos al <b>denominador común</b> y restamos solo los numeradores.</p><p>Ejemplo: 5/6 − 1/4 → mcm(6, 4) = 12 → 10/12 − 3/12 = 7/12.</p><p><b>Ojo:</b> 5/6 − 1/4 no es 4/2. El denominador común no se resta.</p><p>Tocá el botón siguiente para avanzar, o escribí tus propias fracciones.</p>`}],
  norm(mode,r){
    let n1=clamp(r.n1,1,20),d1=clamp(r.d1,2,12),n2=clamp(r.n2,1,20),d2=clamp(r.d2,2,12);
    if(d1===d2)d2=d2===12?11:d2+1;               // distinto denominador
    if(mode==='res'){
      if(n1*d2<n2*d1){[n1,n2]=[n2,n1];[d1,d2]=[d2,d1];}   // que el resultado sea positivo
      if(n1*d2===n2*d1)n1=Math.min(n1+1,20),n2=n2>1&&n1===20&&n1*d2===n2*d1?n2-1:n2;
    }
    return{n1,d1,n2,d2};
  },
  rand(mode,v){
    let o;
    do{const d1=R_(2,12);let d2=R_(2,12);
       o={n1:R_(1,Math.min(20,d1*2)),d1,n2:R_(1,Math.min(20,d2*2)),d2};
       o=SPEC.norm(mode,o);
    }while(o.n1===v.n1&&o.d1===v.d1&&o.n2===v.n2&&o.d2===v.d2);
    return o;
  },
  truth(mode,v){   // cuenta hecha por otro camino: denominadores multiplicados y simplificado al final
    const s=mode==='sum'?1:-1,num=v.n1*v.d2+s*v.n2*v.d1,den=v.d1*v.d2,g=gcd(num,den);
    return den/g===1?String(num/g):`${num/g}/${den/g}`;
  },
  build(mode,v){
    const sum=mode==='sum',op=sum?'+':'−',nom=sum?'suma':'resta';
    const {n1,d1,n2,d2}=v,m=lcm(d1,d2),f1=m/d1,f2=m/d2,A=n1*f1,B=n2*f2,R=sum?A+B:A-B,g=gcd(R,m),rn=R/g,rd=m/g;
    const T=`${fr(n1,d1)} ${op} ${fr(n2,d2)}`;
    const res=rd===1?String(rn):`${rn}/${rd}`;
    const end=` = ${rd===1?fmt(rn):fr(rn,rd)}`;
    const simp=g===1?`${fr(R,m)} ya es irreducible (el único número que divide a los dos es 1), así que no se simplifica.`
      :`${fr(R,m)}: el mayor número que divide a los dos es ${g}. Dividimos arriba y abajo entre ${g}: ${fr(R,m)} = <b>${rd===1?fmt(rn):fr(rn,rd)}</b>.`;
    const S=[
      {h:`Vamos a calcular <b>${T}</b>. Los denominadores (${d1} y ${d2}) son distintos, así que primero hay que llevar las dos fracciones a un denominador común.`},
      {h:`El denominador común es el <b>mcm(${d1}, ${d2}) = ${m}</b>. Es el menor número que es múltiplo de ${d1} y de ${d2}.`,
       row:[`mcm(${d1}, ${d2})`,String(m)],c:205,l:`mcm(${d1}, ${d2}) = ${m}`},
      {h:`Convertimos cada fracción. ${m} ÷ ${d1} = ${f1}, así que multiplicamos arriba y abajo por ${f1}: ${fr(n1,d1)} = <b>${fr(A,m)}</b>. Y ${m} ÷ ${d2} = ${f2}: ${fr(n2,d2)} = <b>${fr(B,m)}</b>.`,
       row:[`${fr(n1,d1)} = ${fr(A,m)}`,`${fr(n2,d2)} = ${fr(B,m)}`],c:35,l:`${fr(A,m)} ${op} ${fr(B,m)}`},
      {h:`Ahora los denominadores son iguales. ${sum?'Sumamos':'Restamos'} solo los numeradores y el denominador queda igual: ${A} ${op} ${B} = <b>${R}</b>.`,
       row:[`${A} ${op} ${B}`,`${R} (sobre ${m})`],c:50,l:`${fr(A,m)} ${op} ${fr(B,m)} = ${fr(R,m)}`},
      {h:`Simplificamos si se puede: ${simp}`,
       row:[`${fr(R,m)} ÷ ${g}`,rd===1?fmt(rn):fr(rn,rd)],c:160,l:`${fr(R,m)} = ${rd===1?fmt(rn):fr(rn,rd)}`},
      {h:`¡Listo! <b>${T} = ${rd===1?fmt(rn):fr(rn,rd)}</b>. Comprobación con la operación inversa: ${rd===1?fmt(rn):fr(rn,rd)} ${sum?'−':'+'} ${fr(n2,d2)} da ${fr(n1,d1)}, la primera fracción.`,
       row:[T,rd===1?fmt(rn):fr(rn,rd)],c:280,l:`${T} = ${rd===1?fmt(rn):fr(rn,rd)}`}];
    return{T,end,rs:5,S,res};
  }
};
