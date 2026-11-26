# Primaria (26/11/2026): textos que copiaban la clase y tarjetas incompletas, reescritos.
import json
def ed(m,fn):
  f='contenido/medio/%s/%s.json'%(m,m.split('/')[1]); M=json.load(open(f,encoding='utf-8')); fn(M); json.dump(M,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
def tema(M,n,i,defi=None,lista=None):
  t=M['niveles'][n]['leccion']['temas'][i]
  for b in t['explicacion']:
    if b['tipo']=='definicion' and defi: b['texto']=defi
    if b['tipo']=='lista' and lista: b['items']=lista
def card(M,n,i,d): M['niveles'][n]['leccion']['recuerda'][i]['definicion']=d
ed('matematica-1/mision-9',lambda M:tema(M,'1',0,'SI <b>SACAMOS</b> COSAS DE UN GRUPO, EL GRUPO QUEDA MÁS CHICO.',['TENÍAS 5 CARAMELOS Y TE COMISTE 2.','CONTÁ LOS QUE TODAVÍA ESTÁN: ESOS SON LOS QUE <b>QUEDAN</b>.']))
ed('matematica-1/mision-12',lambda M:card(M,'4',1,'SON DIEZ BOLSITAS DE DIEZ CARAMELOS CADA UNA.'))
def m2_1(M):
  tema(M,'1',1,'CUANDO LLEGAMOS AL 100, LA CUENTA SIGUE: <b>101, 102, 103…</b>',['UNA CAJA DE 100 Y 4 SUELTOS: 104.','EL 109 Y UNO MÁS: 110.'])
  tema(M,'3',0,'CONTAR <b>DE 10 EN 10</b> ES AGREGAR UN PAQUETE ENTERO POR VEZ.',['130 → 140 → 150 → 160.','SOLO SE MUEVE LA CIFRA DEL MEDIO.'])
ed('matematica-2/mision-1',m2_1)
ed('matematica-2/mision-2',lambda M:card(M,'3',0,'ES LO QUE SE JUNTA CON CINCO CAJAS DE CIEN.'))
ed('matematica-2/mision-4',lambda M:card(M,'4',0,'PRIMERO BUSCAMOS LAS CENTENAS EN LA RECTA Y DESPUÉS AVANZAMOS.'))
def m2_13(M):
  card(M,'2',0,'ES SUMAR SIEMPRE EL MISMO NÚMERO, UNO DETRÁS DEL OTRO.')
  M['niveles']['4']['leccion']['temas'][0]['ejercicio']={'motor':'primeros_x','p':{'modo':'mult','que':'signo'}}
ed('matematica-2/mision-13',m2_13)
def m2_15(M):
  tema(M,'1',0,'MULTIPLICAR <b>POR 10</b> ES ARMAR VARIOS PAQUETES DE 10 IGUALES.',['3 PAQUETES: 10, 20, 30.','3 × 10 = 30: AL 3 LE PONEMOS <b>UN 0</b> A LA DERECHA.'])
  card(M,'4',1,'CONTESTAMOS LA PREGUNTA CON UNA ORACIÓN COMPLETA Y EL NÚMERO.')
ed('matematica-2/mision-15',m2_15)
def m3_2(M):
  tema(M,'1',0,'PARA SABER CUÁL ES MAYOR, EMPEZAMOS POR LOS <b>MILES</b>.',['EL QUE TIENE MÁS MILES ES EL MAYOR.','SI TIENEN LOS MISMOS MILES, MIRAMOS LAS CENTENAS, Y ASÍ HACIA LA DERECHA.'])
  tema(M,'3',1,'AL 3.999 LE SUMAMOS 1 Y SE COMPLETA UN MIL: <b>4.000</b>.',['EL QUE VA ANTES DEL 7.000 ES EL 6.999.','A VECES SE MUEVEN MUCHAS CIFRAS A LA VEZ.'])
  tema(M,'4',0,'EN LA RECTA, CADA MARCA GRANDE ES <b>1.000</b> MÁS QUE LA ANTERIOR.',['EL 0 ESTÁ A LA IZQUIERDA Y EL 10.000 AL FINAL.','MÁS A LA DERECHA, MÁS GRANDE.','6.400 QUEDA ENTRE EL 6.000 Y EL 7.000.'])
ed('matematica-3/mision-2',m3_2)
