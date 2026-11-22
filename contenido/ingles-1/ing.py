# -*- coding: utf-8 -*-
"""Ayudas comunes de Inglés I (Nivel Avanzado, Año 1)."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "matematica-1", "mision-4"))
from base import *
SID = "57e6bf8d-21ed-4fdf-826e-7304097ae565"
RAIZ = os.path.join(AQUI, "..", "..", "tools", "clase", "lecciones")
def NV(obj,ver,secs,ec,ei,es,tip,ojo,res,glo,car,cn,rc,sol): return {"objetivo":obj,"vas_a_ver":ver,"secciones":secs,"ejemplo_completo":ec,"ejemplo_incompleto":ei,"ejemplo_solo":es,"tip":tip,"ojo":ojo,"resumen":res,"glosario":glo,"carpeta":car,"carpeta_nivel":cn,"respuestas_carpeta":rc,"soluciones":sol}
G=lambda *p:[{"palabra":a,"significado":b} for a,b in p]; RS=lambda *p:[{"titulo":a,"texto":b} for a,b in p]
FB=lambda p,h,e,**k:{"t":"fill_blank","p":p,"o":[],"r":{"huecos":h},"e":e,**k}
MS=lambda p,o,c,e,**k:{"t":"multi_select","p":p,"o":o,"r":{"correctas":c},"e":e,**k}
TT=lambda p,seg,tocar,e,**k:{"t":"tap_text","p":p,"o":{"segmentos":seg,"modo":"palabras"},"r":{"tocar":tocar},"e":e,**k}
KW=lambda p,ayuda,grupos,mini,e,**k:{"t":"keywords","p":p,"o":{"ayuda":ayuda},"r":{"grupos":grupos,"minimo":mini},"e":e,**k}
SA=lambda p,ac,e,**k:{"t":"short_answer","p":p,"o":{},"r":{"acepta":ac},"e":e,**k}
ORD=lambda p,des,orden,e,**k:{"t":"ordering","p":p,"o":des,"r":{"orden":orden},"e":e,**k}
CLF=lambda p,els,cats,m,e,**k:{"t":"classify","p":p,"o":{"elementos":els,"categorias":cats},"r":{"categorias":m},"e":e,**k}
MAT=lambda p,iz,de,e,**k:{"t":"matching","p":p,"o":{"izquierda":iz,"derecha":de},"r":{"pares":dict(zip(iz,de))},"e":e,**k}
# ---- escenas de la clase animada
RES=lambda v,items:{"t":"resumen","voz":v,"items":items,"fin":{"titulo":"¡CLASE TERMINADA!","sub":"Ahora, a practicar 🚀"}}
Q=lambda p,o,c,v:{"t":"pregunta","pregunta":p,"opciones":o,"correcta":c,"voz":v}
ER=lambda it,v:{"t":"errores","items":[{"mal":a,"bien":b} for a,b in it],"voz":v}
DEF=lambda w,t,e,v:{"t":"definicion","palabra":w,"texto":t,"emoji":e,"voz":v}
CMP=lambda a,b,s,v:{"t":"comparar","a":{"cab":a[0],"texto":a[1],"emoji":a[2]},"b":{"cab":b[0],"texto":b[1],"emoji":b[2]},"signo":s,"voz":v}
TB=lambda t,c,f,v:{"t":"tabla","titulo":t,"columnas":c,"filas":f,"voz":v}
CAU=lambda c,it,v:{"t":"causas","causa":{"txt":c[0],"emoji":c[1]},"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
CL=lambda cj,fi,v:{"t":"clasificar","cajas":[{"cab":a,"emoji":b} for a,b in cj],"fichas":[{"txt":a,"caja":b} for a,b in fi],"voz":v}
PA=lambda t,it,v:{"t":"pasos","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
AD=lambda a,d,v:{"t":"antesdespues","antes":{"cab":a[0],"emoji":a[1],"texto":a[2]},"despues":{"cab":d[0],"emoji":d[1],"texto":d[2]},"voz":v}
DA=lambda n,a,d,t,e,v:{"t":"dato","numero":n,"antes":a,"despues":d,"texto":t,"emoji":e,"voz":v}
RET=lambda tx,seg,resp,em,ti,sub,v:{"t":"reto","texto":tx,"segundos":seg,"respuesta":resp,"emoji":em,"titulo":ti,"sub":sub,"voz":v}
NOT=lambda ci,ti,ba,em,tt,sub,v:{"t":"noticia","cinta":ci,"titular":ti,"bajada":ba,"emoji":em,"titulo":tt,"sub":sub,"voz":v}
BQ=lambda t,it,v:{"t":"bloques","titulo":t,"items":[{"cab":a,"txt":b} for a,b in it],"voz":v}
LI=lambda t,ev,v:{"t":"linea","titulo":t,"eventos":[{"fecha":a,"txt":b,"emoji":c} for a,b,c in ev],"voz":v}
VE=lambda a,b,ia,ib,am,v:{"t":"venn","a":a,"b":b,"itemsA":ia,"itemsB":ib,"ambos":am,"voz":v}
FL=lambda t,it,v:{"t":"flujo","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
MZ=lambda t,c,v:{"t":"matriz","titulo":t,"celdas":[{"cab":a,"txt":b} for a,b in c],"voz":v}
CIC=lambda t,it,v:{"t":"ciclo","titulo":t,"items":[{"txt":a,"emoji":b} for a,b in it],"voz":v}
ZO=lambda it,v:{"t":"zoom","niveles":[{"emoji":a,"txt":b} for a,b in it],"voz":v}
SIS=lambda t,p,ent,sal,v:{"t":"sistema","titulo":t,"proceso":{"txt":p[0],"emoji":p[1]},"entradas":[{"tipo":a,"txt":b} for a,b in ent],"salidas":[{"tipo":a,"txt":b} for a,b in sal],"voz":v}
VIS=lambda t,cubos,v:{"t":"vistas","titulo":t,"cubos":cubos,"voz":v}
def escribir(n, M, STEPS, TIT, CLS):
    d = os.path.join(AQUI, f"mision-{n}"); os.makedirs(d, exist_ok=True)
    json.dump(M, open(os.path.join(d, f"mision-{n}.json"), "w"), ensure_ascii=False)
    for k, es in CLS.items():
        json.dump({"slug":f"ing1-m{n}-n{k}","step_id":STEPS[k],"materia":"Inglés I","titulo":TIT[k],"sub":f"Inglés I · Misión {n} · Nivel {k}","escenas":es},open(os.path.join(RAIZ,f"ing1-m{n}-n{k}.json"),"w"),ensure_ascii=False)
    print("ok misión", n)

# ---- Inglés: actividades con las marcas de js/ingles-duo.js y pantallas nuevas
def _v(t):
    t = t.strip(); b = t.lower(); return [t, b, b.rstrip(".?!"), t.rstrip(".?!")]
def AU(texto, p, e, ac=None, **k): return SA(p + " [[audio:" + texto + "]]", ac or list(dict.fromkeys(_v(texto))), e, **k)
def HA(texto, p, e, ac=None, **k): return SA(p + " [[hablar:" + texto + "]]", ac or list(dict.fromkeys(_v(texto))), e, **k)
def MEM(p, iz, de, e, **k): return MAT("[[memorama]] " + p, iz, de, e, **k)
TAR=lambda t,it,v:{"t":"tarjetas","titulo":t,"items":[{"en":a,"es":b,**({"emoji":c} if c else {})} for a,b,c in it],"voz":v}
ORA=lambda t,pa,tr,v:{"t":"oracion","titulo":t,"partes":[{"txt":a,"rol":b} for a,b in pa],"traduccion":tr,"voz":v}
PRO=lambda t,pa,v:{"t":"pronunciacion","titulo":t,"palabras":[{"en":a,"como":b,"es":c} for a,b,c in pa],"voz":v}
