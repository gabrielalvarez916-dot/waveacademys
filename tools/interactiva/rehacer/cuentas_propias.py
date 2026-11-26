# 26/11/2026: las cuentas de ejemplo de la lección no pueden ser las mismas del PDF del nivel. Se cambian por cuentas propias.
import json
R={
('matematica-1/mision-10','1'):[('2,5 = 25/10 = 5/2','3,5 = 35/10 = 7/2')],
('matematica-1/mision-14','4'):[('el 25 % significa 25 de cada 100, es decir 25/100 = 1/4','el 40 % significa 40 de cada 100, es decir 40/100 = 2/5'),('25 % = 25/100 = 1/4','40 % = 40/100 = 2/5')],
('matematica-1/mision-2','1'):[('48 + 27 = 27 + 48 = 75','56 + 19 = 19 + 56 = 75'),('36 + 25 + 75 = 36 + 100 = 136','43 + 64 + 36 = 43 + 100 = 143'),('45 + 30 = 75 → 75 − 30 = 45 y 75 − 45 = 30','52 + 29 = 81 → 81 − 29 = 52 y 81 − 52 = 29')],
('matematica-1/mision-4','1'):[('24 ÷ 4 × 2 = 6 × 2 = 12.','30 ÷ 5 × 3 = 6 × 3 = 18.')],
('matematica-1/mision-6','3'):[('91 = 7 × 13','119 = 7 × 17')],
('matematica-1/mision-7','2'):[('12 y 18: 6 × 36 = 216 = 12 × 18.','8 y 20: 4 × 40 = 160 = 8 × 20.'),('6 × 36 = 12 × 18 = 216','4 × 40 = 8 × 20 = 160')],
('matematica-1/mision-8','2'):[('para 18/24, MCD(18, 24) = 6, y queda 3/4','para 20/28, MCD(20, 28) = 4, y queda 5/7'),('18/24 = 3/4 (dividido 6).','20/28 = 5/7 (dividido 4).'),('18/24 = 3/4','20/28 = 5/7')],
('matematica-1/mision-9','1'):[('23/6 = 3 5/6','17/5 = 3 2/5')],
('matematica-1/mision-9','3'):[('3/4 ÷ 2/5 = 3/4 × 5/2 = 15/8','2/3 ÷ 4/7 = 2/3 × 7/4 = 14/12 = 7/6'),('3/4 ÷ 2/5 = 15/8','2/3 ÷ 4/7 = 7/6')],
('medio/matematica-1/mision-12','1'):[('20 + 30','40 + 50'),('2 + 3 = 5','4 + 5 = 9'),('5 BOLSITAS DE 10 SON 50.','9 BOLSITAS DE 10 SON 90.')],
('medio/matematica-1/mision-12','2'):[('70 − 20','90 − 30'),('7 − 2 = 5','9 − 3 = 6'),('QUEDAN 5 BOLSITAS: 50.','QUEDAN 6 BOLSITAS: 60.')],
('medio/matematica-1/mision-15','3'):[('20 + 3','30 + 2'),('CERCA DE 20','CERCA DE 30')],
('medio/matematica-1/mision-6','4'):[('40 + 7 = 47','60 + 5 = 65')],
('medio/matematica-2/mision-10','1'):[('576 − 234 = 342','687 − 352 = 335'),('576 − 234: EL 576','687 − 352: EL 687'),('576 − 234','687 − 352')],
('medio/matematica-2/mision-10','2'):[('865 − 432 = 433','978 − 546 = 432'),('579 − 274 = 305','698 − 395 = 303')],
('medio/matematica-2/mision-10','3'):[('EN 352 − 128: 2 − 8 NO ALCANZA','EN 461 − 237: 1 − 7 NO ALCANZA')],
('medio/matematica-2/mision-10','4'):[('463 − 247 = 226: 226 + 247 = 473','582 − 365 = 227: 227 + 365 = 592'),('224 + 128 = 352','224 + 237 = 461'),('226 + 247 ≠ 463','227 + 365 ≠ 582')],
('medio/matematica-2/mision-11','2'):[('450 − 320 = 130','680 − 450 = 230')],
('medio/matematica-2/mision-11','3'):[('500 − 350 = 150','700 − 450 = 250')],
('medio/matematica-2/mision-12','1'):[('30 + 40 = 40 + 30','20 + 60 = 60 + 20')],
('medio/matematica-2/mision-12','2'):[('37 + 3 = 40','46 + 4 = 50'),('40 + 25 = 65','50 + 23 = 73')],
('medio/matematica-2/mision-12','3'):[('25 + 25 = 50','35 + 35 = 70'),('25 + 26 = 51','35 + 36 = 71')],
('medio/matematica-2/mision-12','4'):[('25 + 15 = 40 Y 40 − 15 = 25','35 + 15 = 50 Y 50 − 15 = 35')],
('medio/matematica-2/mision-15','3'):[('24 × 10 = 240','36 × 10 = 360'),('24 × 10 NO ES 2410','36 × 10 NO ES 3610')],
('medio/matematica-2/mision-5','2'):[('465 = 400 + 60 + 5','738 = 700 + 30 + 8'),('708 = 700 + 8','605 = 600 + 5')],
('medio/matematica-2/mision-6','2'):[('$200, $100 Y $50: 200, 300, 350','$500, $200 Y $20: 500, 700, 720')],
('medio/matematica-2/mision-7','2'):[('6 + 4 = 10, ENTONCES 60 + 40 = 100','3 + 7 = 10, ENTONCES 30 + 70 = 100'),('70 + 30 = 100','80 + 20 = 100')],
('medio/matematica-2/mision-8','1'):[('800 − 300: 8 − 3 = 5, SON 500','900 − 400: 9 − 4 = 5, SON 500'),('47 − 5 = 42','68 − 6 = 62')],
('medio/matematica-2/mision-8','2'):[('100 − 70: 80, 90, 100','100 − 60: 70, 80, 90, 100'),('500 − 300: 400, 500','700 − 500: 600, 700')],
('medio/matematica-2/mision-8','3'):[('365 − 42: 60 − 40 Y 5 − 2','478 − 53: 70 − 50 Y 8 − 3')],
('medio/matematica-2/mision-9','1'):[('EN 234 + 52, EL 5 VA DEBAJO DEL 3','EN 316 + 72, EL 7 VA DEBAJO DEL 1')],
('medio/matematica-2/mision-9','2'):[('342 + 125 = 467','431 + 254 = 685')],
('medio/matematica-2/mision-9','3'):[('147 + 235 = 382','258 + 136 = 394')],
('medio/matematica-2/mision-9','4'):[('298 + 405: CERCA DE 300 + 400 = 700','397 + 502: CERCA DE 400 + 500 = 900')],
('medio/matematica-3/mision-1','2'):[('2.000 + 300 + 5','4.000 + 600 + 2')],
('medio/matematica-3/mision-3','2'):[('3.608 = 3.000 + 600 + 8','5.704 = 5.000 + 700 + 4')],
('medio/matematica-3/mision-5','2'):[('3.000 + 700 + 70 + 7','4.000 + 800 + 60 + 9')],
('medio/matematica-3/mision-5','4'):[('300 Y 700 FORMAN 1.000','400 Y 600 FORMAN 1.000')],
}
def reemplazar(x,pares):
  for a,b in pares: x=x.replace(a,b)
  return x
for (m,n),pares in R.items():
  f='contenido/%s/%s.json'%(m,m.split('/')[-1]); M=json.load(open(f,encoding='utf-8')); L=M['niveles'][n]['leccion']; antes=json.dumps(L,ensure_ascii=False)
  for t in L['temas']:
    for b in t['explicacion']:
      if b.get('texto'): b['texto']=reemplazar(b['texto'],pares)
      if b.get('items'): b['items']=[reemplazar(x,pares) for x in b['items']]
  for r in L['recuerda']:
    for k in ('definicion','ejemplo'): r[k]=reemplazar(r.get(k,''),pares)
  if json.dumps(L,ensure_ascii=False)==antes: print('SIN CAMBIO',m,n)
  json.dump(M,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
