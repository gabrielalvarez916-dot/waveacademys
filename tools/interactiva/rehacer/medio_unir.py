# Primaria (26/11/2026): una pantalla que repite el ejemplo de otra del mismo nivel no es un saber nuevo:
# su idea pasa a la pantalla original (como un paso más de la lista). Si solo repite la práctica,
# se le da la práctica que corresponde a su propio ejemplo.
import json, glob, sys
def txt(t): 
  d=[b for b in t['explicacion'] if b['tipo']=='definicion']; return d[0]['texto'] if d else ''
cambios=0
for f in sorted(glob.glob('contenido/medio/matematica-*/mision-*/mision-*.json')):
  M=json.load(open(f,encoding='utf-8')); toc=False
  for n,N in M['niveles'].items():
    L=N.get('leccion')
    if not L: continue
    T=L['temas']; nuevo=[]
    for t in T:
      igual=[u for u in nuevo if u['ejemplo']==t['ejemplo']]
      if igual:
        u=igual[0]; lst=[b for b in u['explicacion'] if b['tipo']=='lista']
        if lst: lst[0]['items'].append(txt(t))
        else:
          par=[b for b in u['explicacion'] if b['tipo']=='parrafo']
          if par: par[0]['texto']+=' '+txt(t)
          else: u['explicacion'].append({'tipo':'lista','items':[txt(t)]})
        toc=True; cambios+=1; continue
      if any(u['ejercicio']==t['ejercicio'] for u in nuevo):
        ej=dict(t['ejemplo']); cand={'motor':t['ejercicio']['motor'],'p':dict(ej.get('p',{}))}
        if not any(u['ejercicio']==cand for u in nuevo): t['ejercicio']=cand; toc=True; cambios+=1
      nuevo.append(t)
    L['temas']=nuevo
  if toc:
    M['actualizar_preguntas']=M.get('actualizar_preguntas',False)
    json.dump(M,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('cambios',cambios)
