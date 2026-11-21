import json
R="Relámpago. "
def mc(p,o,c,e,t=20): return {"t":"multiple_choice","p":R+p,"o":o,"r":{"correcta":c},"e":e,"tiempo":t}
def tf(p,c,e,t=15): return {"t":"true_false","p":R+p,"o":["Verdadero","Falso"],"r":{"correcta":c},"e":e,"tiempo":t}
def fb(p,h,e,t=25): return {"t":"fill_blank","p":R+p,"o":[],"r":{"huecos":[h]},"e":e,"tiempo":t}
def cl(p,pares,cats,e,t=35): return {"t":"classify","p":R+p,"o":{"elementos":list(pares),"categorias":cats},"r":{"categorias":pares},"e":e,"tiempo":t}
def ma(p,pares,e,t=35): return {"t":"matching","p":R+p,"o":{"izquierda":list(pares),"derecha":list(pares.values())},"r":{"pares":pares},"e":e,"tiempo":t}
def od(p,items,orden,e,t=30): return {"t":"ordering","p":R+p,"o":items,"r":{"orden":orden},"e":e,"tiempo":t}
def ms(p,o,c,e,t=25): return {"t":"multi_select","p":R+p,"o":o,"r":{"correctas":c},"e":e,"tiempo":t}
def tp(p,seg,idx,e,t=25): return {"t":"tap_text","p":R+p,"o":{"segmentos":seg,"modo":"palabras"},"r":{"tocar":idx},"e":e,"tiempo":t}
P={
1:[cl("¿Qué tipo de norma es cada una?",{"Pagar impuestos":"Jurídica","Decir la verdad":"Moral","Saludar al entrar":"Social"},["Jurídica","Moral","Social"],"Cada norma tiene su origen."),
   tf("Los derechos no tienen límites.","Falso","Terminan donde empiezan los de otros."),
   fb("El poder que hace las leyes es el ___ .",["legislativo"],"Sanciona las leyes."),
   mc("Dividir el poder sirve para…",["Evitar abusos","Hacer más leyes","Votar menos"],"Evitar abusos","Los poderes se controlan entre sí.")],
2:[ma("¿Cómo se llama cada forma de poder?",{"Elegir quién decide":"Democracia representativa","Decidir cada ley con el voto de todos":"Democracia directa","Tomar el poder por la fuerza":"Golpe de Estado"},"Cada forma, su nombre."),
   tf("Contrastar fuentes ayuda a evitar noticias falsas.","Verdadero","Verificar es clave."),
   od("Orden para verificar una noticia.",["Compartir solo si es confiable","Buscar la fuente original","Contrastar con otros medios","Dudar del titular"],["Dudar del titular","Buscar la fuente original","Contrastar con otros medios","Compartir solo si es confiable"],"Primero dudar, al final compartir."),
   ms("¿Cuáles son rasgos democráticos?",["Elecciones libres","Censura","Libertad de expresión","Partido único"],["Elecciones libres","Libertad de expresión"],"La censura y el partido único son autoritarios.")],
3:[cl("¿Qué tipo de participación es cada acción?",{"Votar":"Política","Afiliarse a un partido":"Política","Ayudar en un comedor del barrio":"Comunitaria","Integrar una cooperadora":"Comunitaria"},["Política","Comunitaria"],"Unas deciden autoridades; otras ayudan a la comunidad."),
   tf("La protesta pacífica es un derecho.","Verdadero","Sin violencia."),
   fb("El sindicato defiende a los ___ .",["trabajadores"],"Es su función."),
   mc("¿Pueden participar los jóvenes?",["Sí, tienen derecho","Solo con permiso","Nunca"],"Sí, tienen derecho","La participación es un derecho de todos.",15)],
4:[ma("¿Qué significa cada término?",{"Oposición":"Partidos que no gobiernan","Balotaje":"Segunda vuelta","Sistema proporcional":"Cargos según el porcentaje"},"Cada término, su significado."),
   tp("Tocar la palabra que nombra la segunda vuelta: «El balotaje define entre los dos más votados».",["El","balotaje","define","entre","los","dos","más","votados."],[1],"Es la segunda vuelta."),
   tf("El voto obligatorio garantiza que el voto sea informado.","Falso","Aumenta la cantidad, no la calidad."),
   mc("El padrón electoral es la lista de…",["Personas que pueden votar","Candidatos","Partidos"],"Personas que pueden votar","Define quién vota.")],
5:[od("De mayor a menor jerarquía.",["Ordenanza","Constitución","Decreto","Ley"],["Constitución","Ley","Decreto","Ordenanza"],"La constitución está por encima de todo."),
   tf("El Judicial hace las leyes.","Falso","Las hace el Legislativo."),
   fb("La garantía contra detenciones ilegales es el hábeas ___ .",["corpus"],"Protege la libertad física.",25),
   mc("Nadie está por encima de la ley: es…",["Imperio de la ley","Veto","Amparo"],"Imperio de la ley","Rige a todos.")],
6:[cl("¿Qué tipo de derecho es cada uno?",{"Votar":"Político","Ser elegido":"Político","Recibir educación":"Social","Acceder a la salud":"Social"},["Político","Social"],"Unos permiten participar; otros cubren necesidades."),
   tf("La Declaración Universal es de 1948.","Verdadero","Tras la guerra."),
   mc("Los derechos humanos valen para…",["Todas las personas","Solo adultos","Solo ciudadanos"],"Todas las personas","Son universales.",15),
   tp("Tocar quién queda obligado por un tratado ratificado: «Un tratado ratificado obliga al Estado».",["Un","tratado","ratificado","obliga","al","Estado."],[5],"Obliga al Estado.")],
7:[ma("¿Qué protege o resuelve cada herramienta?",{"Hábeas corpus":"Libertad física","Hábeas data":"Datos personales","Mediación":"Conflicto sin juicio"},"Cada herramienta, su uso."),
   tf("Sin dinero no se puede reclamar nada.","Falso","Hay defensa pública gratuita."),
   fb("La ayuda neutral para resolver un conflicto sin juicio es la ___ .",["mediacion","mediación"],"Ayuda neutral."),
   mc("Quien no puede pagar un abogado tiene…",["Defensa pública gratuita","Que esperar","Ningún recurso"],"Defensa pública gratuita","Es un derecho.")],
8:[cl("¿Qué hace cada actitud ante la burla?",{"Reírse de la víctima":"Suma al problema","Callar y mirar":"Suma al problema","Acompañar a la víctima":"Ayuda a frenarlo","Frenar la burla":"Ayuda a frenarlo"},["Suma al problema","Ayuda a frenarlo"],"Callar también deja sola a la víctima."),
   tf("Callar siempre protege a la víctima.","Falso","La deja sola.",15),
   fb("La opinión negativa formada sin conocer es un ___ .",["prejuicio"],"Se forma antes de conocer."),
   mc("La xenofobia es el rechazo a personas…",["Extranjeras","Mayores","Deportistas"],"Extranjeras","Es su definición.",15)],
9:[cl("¿Señal de cuidado o de alerta?",{"Controlar el celular":"Alerta","Aislar de las amistades":"Alerta","Respetar los tiempos":"Cuidado","Aceptar un no":"Cuidado"},["Cuidado","Alerta"],"Controlar no es cuidar."),
   tf("El consentimiento se puede retirar.","Verdadero","Es reversible."),
   fb("Un consentimiento válido es ___ , sin presión.",["libre"],"Sin presión."),
   mc("La idea de quién es cada persona es la…",["Identidad","Presión","Veda"],"Identidad","Se construye con el tiempo.",15)],
}
if __name__=="__main__":
  for n,a in P.items():
    f=f"mision-{n}/mision-{n}.json"; d=json.load(open(f)); d["act"]["5"]=a
    json.dump(d,open(f,"w"),ensure_ascii=False,indent=1)
  def q(s): return "'"+s.replace("'","''")+"'"
  out=["begin;"]
  for n,a in P.items():
    out.append(f"""create temp table _p{n} on commit drop as select s.id paso from topics t join lessons l on l.topic_id=t.id and l.position=5 join lesson_steps s on s.lesson_id=l.id and s.step_type='final_activity' where t.subject_id='a549d16a-c872-4df7-b243-e4b508bd8668' and t.position={n} and coalesce(t.solo_para,'')<>'internacional';
delete from question_rubrics where question_id in (select id from questions where lesson_step_id in (select paso from _p{n}));
delete from questions where lesson_step_id in (select paso from _p{n});""")
    for i,x in enumerate(a,1):
      out.append(f"""with nq as (insert into questions (lesson_step_id,question_type,prompt,options,points,position,tiempo_seg) select paso,{q(x['t'])}::question_type,{q(x['p'])},{q(json.dumps(x['o'],ensure_ascii=False))}::jsonb,1,{i},{x['tiempo']} from _p{n} returning id) insert into question_rubrics (question_id,reference_answer,explanation) select id,{q(json.dumps(x['r'],ensure_ascii=False))}::jsonb,{q(x['e'])} from nq;""")
  out.append("commit;")
  open("/tmp/practica.sql","w").write("\n".join(out))
