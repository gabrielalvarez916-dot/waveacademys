// Helpers compartidos (van dentro de cada HTML y también los usa el validador en Node)
const fmt=n=>String(n).replace(/\B(?=(\d{3})+(?!\d))/g,".");
const gcd=(a,b)=>b?gcd(b,a%b):Math.abs(a);
const lcm=(a,b)=>a/gcd(a,b)*b;
const R_=(a,b)=>a+Math.floor(Math.random()*(b-a+1));
const clamp=(x,min,max)=>{x=parseInt(String(x).replace(/\D/g,""),10);return isNaN(x)?min:Math.max(min,Math.min(max,x));};
const pw=(a,e)=>{let r=1;for(let i=0;i<e;i++)r*=a;return r;};
const fr=(n,d)=>d===1?fmt(n):`<span class="fr"><i>${fmt(n)}</i><i>${fmt(d)}</i></span>`;
