# -*- coding: utf-8 -*-
"""Inglés I · Misiones 7 (Health and Wellbeing) y 8 (Around the World), COMUNES. Un solo archivo para las dos:
genera mision-7.json, mision-8.json y las 8 clases."""
from ing import *
CHAT=lambda c,ms,ti,sub,v:{"t":"chat","contacto":{"nombre":c[0],"emoji":c[1]},"mensajes":[{"yo":a,"txt":b} for a,b in ms],"titulo":ti,"sub":sub,"voz":v}
HIS=lambda p,lu,li,ti,sub,v:{"t":"historia","personaje":{"nombre":p[0],"emoji":p[1]},"lugar":lu,"lineas":li,"titulo":ti,"sub":sub,"voz":v}
VOC=lambda it,v:{"t":"vocab","items":[{"palabra":a,"emoji":b,"trad":c,**({"pron":d} if d else {})} for a,b,c,d in it],"voz":v}
DIA=lambda pe,li,v:{"t":"dialogo","personas":[{"nombre":a,"emoji":b} for a,b in pe],"lineas":[{"quien":a,"txt":b,"trad":c} for a,b,c in li],"voz":v}
MAPA=lambda z,pa,v:{"t":"mapa","zona":z,"pasos":pa,"voz":v}

# =============================== MISIÓN 7 · HEALTH AND WELLBEING ===============================
A1=NV("Vas a nombrar síntomas comunes, preguntar cómo se siente alguien y sugerir remedios simples.",["Síntomas","What's the matter?","Remedios","En el consultorio"],[
 S(1,"Síntomas",[T("Síntomas comunes",["Inglés","Español"],[["a headache","dolor de cabeza"],["a stomachache","dolor de panza"],["a sore throat","dolor de garganta"],["a cough","tos"],["a fever","fiebre"],["a cold","un resfrío"]]),IM("Idea clave","Los síntomas van con have o have got y llevan a: I have a headache.")]),
 S(1,"What's the matter?",[P("Para preguntar qué le pasa a alguien: What's the matter? o What's wrong? Para responder: I have a sore throat. I don't feel well. Con he, she o it se usa has: She has a fever.")]),
 S(2,"Remedios",[T("Síntoma y remedio",["Síntoma","Remedio"],[["a cold","rest and drink hot tea"],["a fever","see a doctor"],["a sore throat","drink something warm"],["a headache","rest in a quiet room"]])]),
 S(2,"En el consultorio",[D("Diálogo con el médico","Doctor: What's the matter? Patient: I have a cough and a fever. Doctor: How long have you had it? Patient: For two days."),P("La pregunta How long…? sirve para saber desde cuándo está el síntoma.")])],
 {"titulo":"contar un síntoma","planteo":"Decí que a tu hermano le duele la panza.","pasos":["Es he: se usa has.","El síntoma lleva a: a stomachache.","Resultado: He has a stomachache."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Con she se usa ___ : She ___ a fever.","Para preguntar qué le pasa a alguien: What's the ___ ?"]},
 {"titulo":"tu turno","planteo":"Escribí un diálogo corto entre un médico y un paciente con dos síntomas y un remedio."},
 {"titulo":"Has con he y she","texto":"I have, you have, pero he has, she has."},
 ["Decir I have headache, sin a.","Usar have con he o she."],
 RS(("Síntoma","Lo que sentís cuando estás enfermo."),("What's the matter?","¿Qué te pasa?"),("Has","Con he, she e it."),("Remedio","Lo que ayuda a mejorar.")),
 G(("Symptom","Síntoma."),("Remedy","Remedio."),("Sore","Dolorido."),("Painkiller","Analgésico.")),
 ["Completá: She ___ a sore throat.","Tu amigo tose y tiene fiebre. ¿Qué dos síntomas tiene en inglés?","Un compañero escribe: I have headache. ¿Cómo se corrige?","Tiene un resfrío. ¿Qué remedio de la tabla conviene?"],
 ["aplicar","aplicar","error","analizar"],
 [["has","has."],["a cough and a fever","cough and fever","a fever and a cough","fever and cough"],["i have a headache","i have a headache.","I have a headache."],["rest and drink hot tea","rest","drink hot tea","rest and hot tea"]],
 {"incompleto":"Has. Matter.","solo":"Respuesta personal: diálogo con dos síntomas y un remedio.","carpeta":["Has.","A cough and a fever.","I have a headache.","Rest and drink hot tea."]})
A2=NV("Vas a dar consejos con should y shouldn't, y advertencias más fuertes con had better.",["Should","Shouldn't","Had better","Consejo o advertencia"],[
 S(1,"Should",[D("Should","Sirve para dar un consejo. Después va el verbo en forma base: You should drink more water."),T("Forma",["Sujeto","Consejo"],[["I, you, we, they","should rest"],["he, she, it","should rest"]],"Should no cambia con he o she.")]),
 S(1,"Shouldn't",[P("La negativa es shouldn't (should not): You shouldn't eat so much sugar. Para preguntar: Should I see a doctor?")]),
 S(2,"Had better",[D("Had better","Es más fuerte que should: avisa que si no lo hacés, algo malo puede pasar. You'd better see a doctor."),P("La negativa es had better not: You'd better not go to school with a fever.")]),
 S(2,"Consejo o advertencia",[T("Qué tan fuerte",["Forma","Uso"],[["should","Consejo amable"],["had better","Advertencia, hay un riesgo"]]),IM("Idea clave","Después de should y had better el verbo va sin to.")])],
 {"titulo":"dar un consejo","planteo":"Tu amiga está muy cansada. Aconsejale dormir más.","pasos":["Es un consejo amable: should.","Sigue el verbo base: sleep.","Resultado: You should sleep more."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["La negativa de should es ___ .","Si hay un riesgo, se usa had ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí dos consejos con should y una advertencia con had better para alguien con gripe."},
 {"titulo":"Sin to","texto":"Should drink, no should to drink."},
 ["Escribir you should to rest.","Usar had better para un consejo sin riesgo."],
 RS(("Should","Consejo."),("Shouldn't","Consejo en negativo."),("Had better","Advertencia fuerte."),("Verbo","En forma base, sin to.")),
 G(("Advice","Consejo."),("Warning","Advertencia."),("Risk","Riesgo."),("Flu","Gripe.")),
 ["Completá: You ___ drink more water (consejo).","Completá con la negativa: You ___ eat so much sugar.","Un compañero escribe: You should to rest. ¿Cómo se corrige?","Tiene fiebre muy alta. ¿Should o had better?"],
 ["aplicar","aplicar","error","analizar"],
 [["should","should."],["shouldn't","should not","shouldn't."],["you should rest","you should rest.","You should rest."],["had better","had better.","you'd better"]],
 {"incompleto":"Shouldn't. Better.","solo":"Respuesta personal: dos consejos y una advertencia.","carpeta":["Should.","Shouldn't.","You should rest.","Had better."]})
A3=NV("Vas a hablar de hábitos de sueño, estrés y pantallas con too much, too many y not enough.",["Hábitos","Too much y too many","Not enough","Hablar de tus hábitos"],[
 S(1,"Hábitos",[T("Vocabulario",["Inglés","Español"],[["sleep","dormir, sueño"],["stress","estrés"],["screen time","tiempo frente a pantallas"],["go to bed","irse a dormir"],["relax","relajarse"]])]),
 S(1,"Too much y too many",[D("Too much / too many","Indican que hay más de lo conveniente. Too much va con lo que no se cuenta: too much screen time. Too many va con lo que se cuenta: too many hours."),P("Ejemplo: I spend too much time on my phone. I drink too many fizzy drinks.")]),
 S(2,"Not enough",[P("Not enough indica que falta: I don't get enough sleep. I don't drink enough water. Enough va antes del sustantivo."),IM("Idea clave","Too much es de más; not enough es de menos.")]),
 S(2,"Hablar de tus hábitos",[P("Podés contar un hábito y su efecto: I don't sleep enough, so I feel tired. I spend too much time online, so I feel stressed.")])],
 {"titulo":"contar un hábito","planteo":"Decí que pasás demasiado tiempo con el celular.","pasos":["Time no se cuenta: too much.","Se usa spend time on.","Resultado: I spend too much time on my phone."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Con hours, que se cuentan, se usa too ___ .","Para decir que falta algo se usa not ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tres frases sobre tus hábitos de sueño y pantallas con too much, too many o not enough."},
 {"titulo":"Contable o no","texto":"¿Se puede contar? Too many. ¿No se puede? Too much."},
 ["Decir too many screen time.","Poner enough después del sustantivo: sleep enough water."],
 RS(("Too much","De más, no contable."),("Too many","De más, contable."),("Not enough","Falta."),("So","Une hábito y efecto.")),
 G(("Habit","Hábito."),("Stress","Estrés."),("Screen time","Tiempo frente a pantallas."),("Tired","Cansado.")),
 ["Completá: I spend too ___ time on my phone.","Completá: I play too ___ video games.","Un compañero escribe: I have too many stress. ¿Cómo se corrige?","Dormís cinco horas por noche. ¿Too much o not enough sleep?"],
 ["aplicar","aplicar","error","analizar"],
 [["much","much."],["many","many."],["i have too much stress","i have too much stress.","I have too much stress.","too much stress"],["not enough","not enough."]],
 {"incompleto":"Many. Enough.","solo":"Respuesta personal: tres frases sobre hábitos.","carpeta":["Much.","Many.","I have too much stress.","Not enough."]})
A4=NV("Vas a escribir un plan de bienestar: un problema, consejos con should y try to, y una razón con because.",["Partes del plan","Consejos","Razones","Un plan completo"],[
 S(1,"Partes del plan",[T("Estructura",["Parte","Ejemplo"],[["Problema","I feel tired at school."],["Consejo","You should go to bed earlier."],["Razón","because sleep helps you focus."],["Meta","I'm going to sleep eight hours."]])]),
 S(1,"Consejos",[P("Además de should, podés usar try to: Try to turn off your phone at ten. Para algo importante: You'd better not skip breakfast.")]),
 S(2,"Razones",[P("Because explica por qué: Drink water because it gives you energy. So cuenta la consecuencia: I exercise, so I feel better."),IM("Idea clave","Un consejo con razón convence más.")]),
 S(2,"Un plan completo",[P("My problem: I feel stressed. My advice: I should take short breaks and try to walk every day, because exercise reduces stress. My goal: I'm going to walk three times a week.")])],
 {"titulo":"armar un consejo","planteo":"Escribí un consejo con su razón para alguien que no desayuna.","pasos":["Consejo: You should eat breakfast.","Razón: because it gives you energy.","Resultado: You should eat breakfast because it gives you energy."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Para explicar por qué se usa ___ .","Para una meta se usa going ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí tu plan de bienestar: un problema, dos consejos con razón y una meta."},
 {"titulo":"Consejo más razón","texto":"Should más because: el plan se entiende y convence."},
 ["Escribir try to turning off.","Dar consejos sin explicar por qué."],
 RS(("Problema","Lo que querés mejorar."),("Consejo","Should o try to."),("Razón","Because."),("Meta","Going to.")),
 G(("Wellbeing","Bienestar."),("Goal","Meta."),("Break","Pausa."),("Focus","Concentrarse.")),
 ["Completá: You should sleep more ___ sleep helps you focus.","Completá: Try ___ turn off your phone at ten.","Un compañero escribe: Try to turning off the TV. ¿Cómo se corrige?","¿Qué palabra cuenta la consecuencia: because o so?"],
 ["aplicar","aplicar","error","analizar"],
 [["because","because."],["to","to."],["try to turn off the tv","try to turn off the tv.","Try to turn off the TV."],["so","so."]],
 {"incompleto":"Because. To.","solo":"Respuesta personal: plan de bienestar.","carpeta":["Because.","To.","Try to turn off the TV.","So."]})
ACT7={"1":[MC("Elegí la imagen que corresponde a: a fever.",["🤧","🤒","🤕"],"🤒","Fever es fiebre.",n="aplicar"),
  FB("What's the matter? I ___ a sore throat.",[["have","have got"]],"Con I se usa have.",n="aplicar"),
  MEM("Uní cada síntoma con su remedio.",["a cold","a sore throat","a headache"],["rest and drink hot tea","drink something warm","rest in a quiet room"],"Síntoma y remedio.",n="aplicar")],
 "2":[CLF("¿Should o had better?",["You ___ eat more fruit.","Your fever is very high. You ___ see a doctor.","You ___ drink more water.","It's icy. You ___ be careful on the road."],["Should","Had better"],{"You ___ eat more fruit.":"Should","Your fever is very high. You ___ see a doctor.":"Had better","You ___ drink more water.":"Should","It's icy. You ___ be careful on the road.":"Had better"},"Consejo amable: should. Riesgo: had better.",n="analizar"),
  ORD("Ordená las palabras.",["more","should","water","drink","You"],["You","should","drink","more","water"],"Sujeto, should y verbo base.",n="aplicar")],
 "3":[AU("I don't get enough sleep.","Escuchá y escribí lo que oís.","Not enough: falta.",n="aplicar"),
  CLF("¿Too much o too many?",["___ screen time","___ hours online","___ sugar","___ fizzy drinks"],["Too much","Too many"],{"___ screen time":"Too much","___ hours online":"Too many","___ sugar":"Too much","___ fizzy drinks":"Too many"},"Contable: too many. No contable: too much.",n="analizar")],
 "4":[HA("You should go to bed earlier because sleep helps you focus.","Escuchá la frase y decila en voz alta.","Consejo con razón.",n="aplicar"),
  KW("Escribí un consejo para alguien que está estresado, con su razón.","Escribí una frase.",[["should","try to","had better","'d better"],["because","porque","so"]],2,"Por ejemplo: You should take short breaks because they reduce stress.",n="aplicar")],
 "5":[MC("Relámpago. Con she se usa…",["have","has","having"],"has","She has.",tiempo=20,n="recordar"),
  MC("Relámpago. La advertencia más fuerte es…",["should","try to","had better"],"had better","Hay un riesgo.",tiempo=20,n="recordar"),
  VF("Relámpago. Screen time va con too many.","Falso","No se cuenta: too much.",tiempo=15,n="recordar"),
  FB("Relámpago. You ___ rest (consejo).",[["should"]],"Should más verbo base.",tiempo=25,n="recordar")]}
EX7=[[1,AU("She has a sore throat and a cough.","Escuchá y escribí lo que oís.","Has con she.",n="aplicar")],
 [1,MC("Elegí la frase correcta.",["He have a fever.","He has fever.","He has a fever.","He is a fever."],"He has a fever.","Has más a.",n="aplicar")],
 [1,MEM("Uní cada síntoma con su significado.",["a headache","a stomachache","a cough"],["dolor de cabeza","dolor de panza","tos"],"Vocabulario de síntomas.",n="recordar")],
 [2,FB("Your fever is very high. You ___ better see a doctor.",[["had","'d"]],"Advertencia: had better.",n="aplicar")],
 [2,KW("Un compañero escribe: You should to rest. Explicá cómo se corrige.","Escribí una frase.",[["to","sin to","quitar","sacar"],["base","verbo","should rest"]],1,"Después de should el verbo va en forma base, sin to.",n="error")],
 [2,MC("¿Cuál es una advertencia y no un consejo amable?",["You should read more.","You'd better not touch that cable.","You should try yoga.","Should I drink tea?"],"You'd better not touch that cable.","Hay un riesgo: had better.",n="analizar")],
 [3,CLF("¿Too much o not enough?",["Duermo cinco horas.","Paso ocho horas con el celular.","Tomo un vaso de agua por día.","Como mucha azúcar."],["Too much","Not enough"],{"Duermo cinco horas.":"Not enough","Paso ocho horas con el celular.":"Too much","Tomo un vaso de agua por día.":"Not enough","Como mucha azúcar.":"Too much"},"De más o falta.",n="analizar")],
 [3,VF("Too many va con lo que no se puede contar.","Falso","Too many va con lo que se cuenta.",n="error")],
 [3,ORD("Ordená las palabras.",["enough","get","I","sleep","don't"],["I","don't","get","enough","sleep"],"Enough antes del sustantivo.",n="aplicar")],
 [4,MS("¿Qué partes tiene un plan de bienestar?",["Un problema","Consejos","Una razón","Un precio"],["Un problema","Consejos","Una razón"],"El precio no corresponde.",n="analizar")],
 [4,FB("You should eat breakfast ___ it gives you energy.",[["because"]],"Because explica la razón.",n="aplicar")],
 [4,HA("I'm going to walk three times a week.","Escuchá la frase y decila en voz alta.","Meta con going to.",n="aplicar")],
 [4,KW("Explicá por qué un consejo con because convence más que uno sin razón.","Escribí una frase.",[["razón","razon","por qué","porque","because","explica"],["convence","entiende","sentido","motivo"]],1,"Because da el motivo, y así el consejo se entiende y convence.",n="analizar")]]
M7={"subject_id":SID,"tema":7,"practica":"Práctica general: Health and Wellbeing","examen_titulo":"Nivel jefe: Health and Wellbeing","niveles":{"1":A1,"2":A2,"3":A3,"4":A4},"act":ACT7,"examen":EX7}
ST7={1:"49bf0e46-87aa-4b86-8353-e737137218a2",2:"5f344ee1-d4e3-4bdb-aa9c-ebcb3779698e",3:"ab8a5ddc-2448-439c-b8ee-50ba0355a2a2",4:"6a9a2eb0-d973-475c-a08a-9d42ac8deb89"}
TI7={1:"Symptoms and remedies",2:"Should, shouldn't and had better",3:"Sleep, stress and screen time",4:"A wellbeing plan: write advice"}
CL7={1:[
 CHAT(("Mamá","👩"),[(True,"I don't feel well 🤒"),(False,"What's the matter?"),(True,"I have a headache and a fever.")],"SÍNTOMAS","cómo contar qué te pasa",["Un mensaje: alguien no se siente bien.","La mamá pregunta: *What's the matter?*","La respuesta: *headache* y *fever*.","Hoy: *síntomas y remedios*."]),
 VOC([("headache","🤕","dolor de cabeza","jédeik"),("sore throat","😖","dolor de garganta","sor zrout"),("cough","😷","tos","cof"),("fever","🤒","fiebre","fíver")],["Primer síntoma: *headache*.","Segundo: *sore throat*.","Tercero: *cough*.","Y cuarto: *fever*."]),
 DIA([("Doctor","🧑‍⚕️"),("Paciente","🧒")],[(0,"What's the matter?","¿Qué te pasa?"),(1,"I have a cough and a fever.","Tengo tos y fiebre."),(0,"You should rest and drink water.","Tenés que descansar y tomar agua.")],["El médico pregunta *qué pasa*.","El paciente cuenta *dos síntomas*.","Y el médico da un *remedio*."]),
 TB("SÍNTOMA Y REMEDIO",["Síntoma","Remedio"],[["a cold","rest and hot tea"],["a fever","see a doctor"],["a sore throat","something warm"]],["Cada síntoma tiene su remedio.","Para un *cold*, descanso y té caliente.","Para la *fever*, ver al médico.","Para la garganta, algo *tibio*."]),
 Q("She ___ a stomachache.",["have","has","is"],1,["Te toca: con *she*.","¿*Have*, *has* o *is*?","*Has*, con she."]),
 ER([("I have headache","I have a headache"),("He have a cold","He has a cold")],["Errores típicos.","Olvidar la *a* antes del síntoma.","Y usar *have* con *he*."]),
 RES(["Repasemos.","Para preguntar: *What's the matter?*","Para contar: *I have a* más el síntoma.","Con he y she, *has*.","¡Clase terminada! Ahora, *a practicar*."],[["PREGUNTA","What's the matter?"],["SÍNTOMA","I have a headache"],["HE, SHE","has"]])],
2:[
 NOT("CONSEJOS","¿Consejo o advertencia?","Dos formas de aconsejar en inglés","💬","SHOULD Y HAD BETTER","consejos y advertencias",["Noticia: ¿consejo o advertencia?","Dos formas de aconsejar.","Hoy: *should y had better*."]),
 ORA("UN CONSEJO",[("You","sujeto"),("should drink","verbo"),("more water","complemento")],"Tendrías que tomar más agua",["Primero, *a quién*.","Después, *should* más el verbo base.","Luego, *qué*.","Significa que tendría que tomar más agua."]),
 CMP(("SHOULD","Consejo amable","🙂"),("SHOULDN'T","Mejor no hacerlo","🙅"),"vs",["Afirmativo y negativo.","*Should*: conviene hacerlo.","*Shouldn't*: conviene no hacerlo."]),
 DEF("Had better","Advertencia fuerte: si no lo hacés, algo malo puede pasar. You'd better see a doctor.","⚠️",["*Had better* es más fuerte que should.","Avisa que hay un *riesgo*."]),
 CL([("SHOULD","🙂"),("HAD BETTER","⚠️")],[("Comé más fruta",0),("Fiebre muy alta",1),("Probá yoga",0),("Cable pelado",1)],["¿Cuál conviene?","Un consejo *sin riesgo*: should.","Un *riesgo* de verdad: had better."]),
 Q("You ___ to rest. ¿Qué está mal?",["Sobra el to","Falta el to","Está bien"],0,["Te toca: should *to* rest.","¿Sobra, falta o está bien?","*Sobra el to*: should rest."]),
 RES(["Repasemos.","*Should* da un consejo.","*Shouldn't* aconseja no hacerlo.","*Had better* avisa un riesgo.","¡Clase terminada! Ahora, *a practicar*."],[["SHOULD","consejo"],["SHOULDN'T","mejor no"],["HAD BETTER","advertencia"]])],
3:[
 RET("I sleep five hours. ¿Too much o not enough?",6,"Not enough","😴","HÁBITOS","sueño, estrés y pantallas",["Desafío: cinco horas de sueño. ¿De más o de menos? Seis segundos.","*Not enough*.","Hoy: *sueño, estrés y pantallas*."]),
 CAU(("Too much screen time","📱"),[("Poor sleep","😴"),("Stress","😣"),("Less exercise","🛋️")],["Mucho tiempo con pantallas trae efectos.","Primero, *dormir mal*.","Segundo, *estrés*.","Tercero, *menos ejercicio*."]),
 CMP(("TOO MUCH","No se cuenta: time, sugar","📈"),("TOO MANY","Se cuenta: hours, games","🔢"),"vs",["Dos formas de decir *de más*.","*Too much* con lo que no se cuenta.","*Too many* con lo que se cuenta."]),
 TAR("NOT ENOUGH",[("I don't get enough sleep.","No duermo lo suficiente.","🛏️"),("I don't drink enough water.","No tomo suficiente agua.","💧"),("I don't relax enough.","No me relajo lo suficiente.","🧘")],["Primero, el *sueño*.","Segundo, el *agua*.","Tercero, *relajarse*."]),
 Q("I play too ___ video games.",["much","many","enough"],1,["Te toca: video games.","¿*Much*, *many* o *enough*?","*Many*: se cuentan."]),
 ER([("too many screen time","too much screen time"),("sleep enough water","drink enough water")],["Errores típicos.","Usar *many* con lo que no se cuenta.","Y mezclar el verbo: el agua se *toma*."]),
 RES(["Repasemos.","*Too much* y *too many*: de más.","*Not enough*: falta.","*So* une el hábito con su efecto.","¡Clase terminada! Ahora, *a practicar*."],[["TOO MUCH","no contable"],["TOO MANY","contable"],["NOT ENOUGH","falta"]])],
4:[
 HIS(("Lucas","🧑"),"📱",["Lucas mira el celular hasta muy tarde.","Al otro día está cansado y no se concentra."],"MI PLAN","plan de bienestar",["Te presento a *Lucas*.","Usa el celular hasta *muy tarde*.","Al otro día, *cansado*: necesita un plan."]),
 PA("UN PLAN DE BIENESTAR",[("Problem: I feel tired","😩"),("Advice: I should sleep more","💡"),("Reason: because sleep helps","🧠"),("Goal: I'm going to sleep 8 hours","🎯")],["Un plan tiene cuatro partes.","Primero, el *problema*.","Después, el *consejo*.","Luego, la *razón* con because.","Y por último, la *meta*."]),
 MZ("CONSEJOS PARA CADA ÁREA",[("SLEEP","Go to bed earlier"),("SCREENS","Turn off your phone at ten"),("STRESS","Take short breaks"),("FOOD","Don't skip breakfast")],["Consejos para cuatro áreas.","*Sleep*: acostarse más temprano.","*Screens*: apagar el celular a las diez.","*Stress*: hacer pausas cortas.","*Food*: no saltear el desayuno."]),
 AD(("SIN RAZÓN","🤷","You should sleep more."),("CON RAZÓN","✅","You should sleep more because it helps you focus."),["Sin razón, el consejo *no convence*.","Con *because*, se entiende por qué."]),
 Q("¿Qué palabra explica la razón?",["so","because","try"],1,["Te toca: la razón.","¿*So*, *because* o *try*?","*Because*."]),
 RES(["Repasemos.","El plan empieza con un *problema*.","Sigue el *consejo* con su razón.","Termina con una *meta*.","¡Clase terminada! Ahora, *a practicar*."],[["PROBLEMA","I feel tired"],["CONSEJO","should, try to"],["META","going to"]])]}

# =============================== MISIÓN 8 · AROUND THE WORLD ===============================
B1=NV("Vas a decir países, nacionalidades e idiomas, y describir rasgos de otras culturas.",["Países y nacionalidades","Terminaciones","Idiomas","Hablar de culturas"],[
 S(1,"Países y nacionalidades",[T("País y nacionalidad",["País","Nacionalidad"],[["Argentina","Argentinian"],["Brazil","Brazilian"],["Mexico","Mexican"],["Japan","Japanese"],["China","Chinese"],["Spain","Spanish"],["France","French"],["the UK","British"]])]),
 S(1,"Terminaciones",[P("Muchas nacionalidades terminan en -ian, -an, -ese o -ish: Italian, Mexican, Japanese, Spanish. Algunas son distintas: France, French; Greece, Greek."),IM("Idea clave","En inglés, países, nacionalidades e idiomas van siempre con mayúscula: She is Japanese.")]),
 S(2,"Idiomas",[P("Muchas veces el idioma coincide con la nacionalidad: They speak French. Pero no siempre: in Brazil they speak Portuguese; in Mexico they speak Spanish.")]),
 S(2,"Hablar de culturas",[P("Para describir una cultura: In Japan, people take off their shoes at home. In Spain, people often have dinner late. Se usa el presente simple porque son costumbres.")])],
 {"titulo":"presentar a alguien","planteo":"Contá que Yuki es de Japón.","pasos":["País: She is from Japan.","Nacionalidad con mayúscula: Japanese.","Resultado: She is from Japan. She is Japanese."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["France: la nacionalidad es ___ .","Las nacionalidades van con ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí sobre tres personas de distintos países: país, nacionalidad e idioma."},
 {"titulo":"Mayúscula siempre","texto":"Japanese, French, Argentinian: siempre con mayúscula."},
 ["Escribir la nacionalidad en minúscula: she is japanese.","Suponer que en Brasil se habla brasileño."],
 RS(("Country","País."),("Nationality","Nacionalidad."),("Language","Idioma."),("Mayúscula","En los tres casos.")),
 G(("Culture","Cultura."),("Custom","Costumbre."),("Nationality","Nacionalidad."),("Language","Idioma.")),
 ["Completá: Pedro is from Mexico. He is ___ .","¿Qué idioma se habla en Brasil, en inglés?","Un compañero escribe: She is japanese. ¿Cómo se corrige?","¿Por qué una costumbre se cuenta en presente simple?"],
 ["aplicar","aplicar","error","analizar"],
 [["mexican","Mexican","mexican."],["portuguese","Portuguese","portuguese."],["she is japanese","She is Japanese.","she is japanese."],["porque se repite","es un hábito","porque es habitual","se repite siempre","es una costumbre"]],
 {"incompleto":"French. Mayúscula.","solo":"Respuesta personal: tres personas con país, nacionalidad e idioma.","carpeta":["Mexican.","Portuguese.","She is Japanese.","Porque es habitual."]})
B2=NV("Vas a armar un itinerario de viaje con going to, conectores de orden y medios de transporte.",["El itinerario","Conectores de orden","Transporte","Un itinerario completo"],[
 S(1,"El itinerario",[D("Itinerary","Plan de viaje día por día: adónde vas, qué vas a hacer y cómo vas a moverte."),P("Para los planes se usa going to: On day 1, we are going to visit the museum.")]),
 S(1,"Conectores de orden",[T("Para ordenar",["Conector","Significa"],[["First","Primero"],["Then","Después"],["After that","Luego de eso"],["Finally","Por último"]])]),
 S(2,"Transporte",[P("Para el medio de transporte se usa by: by plane, by train, by bus, by car. Pero caminando es on foot."),IM("Idea clave","By plane, sin the: no se dice by the plane.")]),
 S(2,"Un itinerario completo",[P("Day 1: First, we are going to fly to Rome by plane. Then we are going to visit the Colosseum. Day 2: After that, we are going to take the train to Florence. Finally, we are going to fly home.")])],
 {"titulo":"un día del viaje","planteo":"Contá que primero van a visitar un museo y después van a ir en tren a otra ciudad.","pasos":["Orden: First y then.","Plan: going to.","Resultado: First, we are going to visit a museum. Then we are going to travel by train."]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Para el transporte se usa ___ plane.","Caminando se dice on ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un itinerario de dos días a una ciudad que te guste, con conectores y transporte."},
 {"titulo":"By sin the","texto":"By plane, by bus, by train. Caminando: on foot."},
 ["Decir by the plane.","Decir by foot en vez de on foot."],
 RS(("Itinerary","Plan día por día."),("Going to","Planes."),("First, then, finally","Ordenan."),("By","Transporte.")),
 G(("Itinerary","Itinerario."),("Trip","Viaje."),("Flight","Vuelo."),("Sightseeing","Recorrer lugares turísticos.")),
 ["Completá: We are going to travel ___ train.","Completá: ___ , we are going to fly home (por último).","Un compañero escribe: We go by foot. ¿Cómo se corrige?","¿Por qué el itinerario usa going to y no el pasado?"],
 ["aplicar","aplicar","error","analizar"],
 [["by","by."],["finally","Finally","finally."],["we go on foot","We go on foot.","on foot"],["porque es un plan","es un plan","son planes","porque es futuro","es futuro"]],
 {"incompleto":"By. Foot.","solo":"Respuesta personal: itinerario de dos días.","carpeta":["By.","Finally.","We go on foot.","Porque es un plan."]})
B3=NV("Vas a pedir ayuda con cortesía al viajar: indicaciones, preguntas indirectas y respuestas.",["Pedir con cortesía","Preguntar el camino","Indicaciones","Responder y agradecer"],[
 S(1,"Pedir con cortesía",[P("Para llamar la atención se dice Excuse me. Para pedir algo con cortesía: Could you help me, please? Can I have a map, please?"),IM("Idea clave","Could you…? es más amable que Can you…?")]),
 S(1,"Preguntar el camino",[P("Pregunta directa: Where is the station? Pregunta indirecta, más amable: Could you tell me where the station is?"),D("Pregunta indirecta","Después de Could you tell me, el orden es como en una afirmación: where the station is, no where is the station.")]),
 S(2,"Indicaciones",[T("Indicaciones",["Inglés","Español"],[["Go straight on","Seguí derecho"],["Turn left","Doblá a la izquierda"],["Turn right","Doblá a la derecha"],["It's on the corner","Está en la esquina"],["It's next to the bank","Está al lado del banco"]])]),
 S(2,"Responder y agradecer",[P("Si no entendés: Sorry, could you repeat that, please? Para agradecer: Thank you so much! Respuesta: You're welcome.")])],
 {"titulo":"preguntar el camino","planteo":"Preguntá con cortesía dónde está el museo.","pasos":["Llamás la atención: Excuse me.","Pregunta indirecta: Could you tell me…","Resultado: Excuse me, could you tell me where the museum is?"]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Para doblar a la izquierda: turn ___ .","Para pedir que repitan: could you ___ that?"]},
 {"titulo":"tu turno","planteo":"Escribí un diálogo en el que un turista pide cómo llegar a la estación y le responden con dos indicaciones."},
 {"titulo":"Orden indirecto","texto":"Could you tell me where the bank is? El verbo va al final."},
 ["Decir could you tell me where is the station.","Olvidar Excuse me antes de preguntar."],
 RS(("Excuse me","Para llamar la atención."),("Could you…?","Pedido amable."),("Pregunta indirecta","Verbo al final."),("Turn left, turn right","Indicaciones.")),
 G(("Directions","Indicaciones."),("Corner","Esquina."),("Straight on","Derecho."),("Tourist","Turista.")),
 ["Completá: ___ me, could you help me?","Completá: Turn ___ (a la derecha).","Un compañero escribe: Could you tell me where is the bank? Completá bien: Could you tell me where the bank ___ ?","¿Cuál es más amable: Can you…? o Could you…?"],
 ["aplicar","aplicar","error","analizar"],
 [["excuse","Excuse","excuse."],["right","right."],["is","is."],["could you","Could you","could you…?"]],
 {"incompleto":"Left. Repeat.","solo":"Respuesta personal: diálogo con dos indicaciones.","carpeta":["Excuse.","Right.","Is.","Could you."]})
B4=NV("Vas a escribir un post de blog de viaje: contar en pasado, describir con adjetivos y recomendar.",["Partes del post","Contar en pasado","Describir","Recomendar"],[
 S(1,"Partes del post",[T("Estructura",["Parte","Ejemplo"],[["Título","My amazing week in Peru"],["Dónde y cuándo","Last year, I visited Cusco with my family."],["Qué hice","We walked to Machu Picchu."],["Opinión","The view was breathtaking."],["Recomendación","You should try the local food."]])]),
 S(1,"Contar en pasado",[P("Lo que hiciste va en pasado simple: we visited, we took, we ate, it was. Los verbos irregulares cambian: go, went; eat, ate; see, saw.")]),
 S(2,"Describir",[T("Adjetivos fuertes",["Común","Más fuerte"],[["good","amazing"],["big","huge"],["beautiful","breathtaking"],["bad","awful"]]),IM("Idea clave","Un adjetivo fuerte hace el post más interesante.")]),
 S(2,"Recomendar",[P("Para cerrar, recomendá: You should visit the market. Don't miss the sunset! If you go, take a jacket.")])],
 {"titulo":"una oración de blog","planteo":"Contá que fuiste a la playa y que estuvo increíble.","pasos":["Go en pasado: went.","Adjetivo fuerte: amazing.","Resultado: I went to the beach. It was amazing!"]},
 {"titulo":"completar","planteo":"Completá.","pasos":["Eat en pasado: ___ .","Un adjetivo más fuerte que big: ___ ."]},
 {"titulo":"tu turno","planteo":"Escribí un post de blog sobre un viaje o paseo: título, qué hiciste, opinión y una recomendación."},
 {"titulo":"Pasado y consejo","texto":"Lo que hiciste, en pasado. El consejo para el lector, con should."},
 ["Escribir we goed en vez de we went.","Repetir good en todo el texto."],
 RS(("Título","Atrae al lector."),("Pasado simple","Lo que hiciste."),("Adjetivos fuertes","Amazing, huge."),("Recomendación","You should…")),
 G(("Blog post","Entrada de blog."),("Breathtaking","Impresionante."),("Huge","Enorme."),("Sunset","Atardecer.")),
 ["Completá: Last year, we ___ to Cusco (go).","Cambiá good por un adjetivo más fuerte: The trip was ___ .","Un compañero escribe: We eated empanadas. ¿Cómo se corrige?","¿Qué parte del post usa should?"],
 ["aplicar","aplicar","error","analizar"],
 [["went","went."],["amazing","amazing.","awesome","great","fantastic"],["we ate empanadas","We ate empanadas.","ate"],["la recomendación","recomendacion","recomendación","la recomendacion"]],
 {"incompleto":"Ate. Huge.","solo":"Respuesta personal: post de blog de viaje.","carpeta":["Went.","Amazing.","We ate empanadas.","La recomendación."]})
ACT8={"1":[MEM("Uní cada país con su nacionalidad.",["Japan","France","Brazil","Spain"],["Japanese","French","Brazilian","Spanish"],"País y nacionalidad.",n="aplicar"),
  MC("Elegí la frase correcta.",["She are from Japan. She is Japanese.","She is from Japan. She is Japanese.","She is from Japanese. She is Japan.","She is from Japan. She speaks Japan."],"She is from Japan. She is Japanese.","Mayúscula y orden correcto.",n="aplicar")],
 "2":[ORD("Ordená el itinerario.",["Finally, we fly home.","Then we visit the museum.","First, we arrive in Rome.","After that, we take a train."],["First, we arrive in Rome.","Then we visit the museum.","After that, we take a train.","Finally, we fly home."],"First, then, after that, finally.",n="aplicar"),
  FB("We are going to travel ___ bus.",[["by"]],"By más transporte.",n="aplicar")],
 "3":[AU("Could you tell me where the station is?","Escuchá y escribí lo que oís.","Pregunta indirecta.",n="aplicar"),
  MC("Un turista quiere saber dónde está el banco. ¿Qué pregunta es correcta y amable?",["Where the bank is?","Could you tell me where is the bank?","Could you tell me where the bank is?","Tell me the bank."],"Could you tell me where the bank is?","Orden de afirmación al final.",n="error"),
  HA("Excuse me, could you help me, please?","Escuchá la frase y decila en voz alta.","Pedido amable.",n="aplicar")],
 "4":[CLF("¿Qué parte del post es?",["Last year, I visited Cusco.","The view was breathtaking.","You should try the local food.","We walked for hours."],["Qué hice","Opinión","Recomendación"],{"Last year, I visited Cusco.":"Qué hice","The view was breathtaking.":"Opinión","You should try the local food.":"Recomendación","We walked for hours.":"Qué hice"},"Pasado, opinión o consejo.",n="analizar"),
  KW("Escribí una oración de blog sobre un lugar que visitaste, con un adjetivo fuerte.","Escribí una frase.",[["went","visited","was","saw","ate","took"],["amazing","huge","breathtaking","awful","awesome","fantastic","incredible","beautiful"]],2,"Por ejemplo: I visited Iguazú. The waterfalls were amazing!",n="aplicar")],
 "5":[MC("Relámpago. La nacionalidad de France es…",["Francian","French","Franch"],"French","France, French.",tiempo=20,n="recordar"),
  MC("Relámpago. Caminando se dice…",["by foot","on foot","with foot"],"on foot","On foot.",tiempo=20,n="recordar"),
  VF("Relámpago. Could you…? es más amable que Can you…?","Verdadero","Could suena más cortés.",tiempo=15,n="recordar"),
  FB("Relámpago. Go en pasado: ___ .",[["went"]],"Verbo irregular.",tiempo=25,n="recordar")]}
EX8=[[1,AU("They are from Brazil. They speak Portuguese.","Escuchá y escribí lo que oís.","País e idioma.",n="aplicar")],
 [1,KW("Un compañero escribe: He is mexican. Explicá cómo se corrige.","Escribí una frase.",[["mayúscula","mayuscula","Mexican"],["nacionalidad","siempre","va con"]],1,"Las nacionalidades van con mayúscula: He is Mexican.",n="error")],
 [1,MEM("Uní cada país con su idioma.",["Brazil","Mexico","France"],["Portuguese","Spanish","French"],"No siempre coinciden.",n="analizar")],
 [2,FB("___ , we are going to visit the museum. Then we are going to have lunch.",[["first"]],"First abre el itinerario.",n="aplicar")],
 [2,MC("Elegí la frase correcta.",["We are going to travel by the plane.","We are going to travel by plane.","We going to travel by plane.","We are going travel by plane."],"We are going to travel by plane.","By sin the y going to completo.",n="error")],
 [2,ORD("Ordená las palabras.",["going","We","visit","to","are","Rome"],["We","are","going","to","visit","Rome"],"Plan con going to.",n="aplicar")],
 [3,MC("Un turista no entendió la indicación. ¿Qué dice?",["You're welcome, have a nice trip.","Sorry, could you repeat that, please?","Go straight on and turn left.","Thank you so much for your help!"],"Sorry, could you repeat that, please?","Pide que repitan.",n="aplicar")],
 [3,FB("Could you tell me where the station ___ ?",[["is"]],"El verbo va al final.",n="error")],
 [3,HA("Go straight on and turn left.","Escuchá la frase y decila en voz alta.","Indicaciones.",n="aplicar")],
 [4,CLF("¿Pasado o recomendación?",["We ate empanadas.","You should visit the market.","It was amazing.","Don't miss the sunset!"],["Pasado","Recomendación"],{"We ate empanadas.":"Pasado","You should visit the market.":"Recomendación","It was amazing.":"Pasado","Don't miss the sunset!":"Recomendación"},"Lo que hiciste o lo que aconsejás.",n="analizar")],
 [4,VF("En un post de blog, lo que hiciste se cuenta en presente simple.","Falso","Se cuenta en pasado simple.",n="error")],
 [4,MS("¿Qué adjetivos son más fuertes que good o beautiful?",["amazing","breathtaking","nice","OK"],["amazing","breathtaking"],"Nice y OK son comunes.",n="analizar")],
 [4,KW("Explicá por qué conviene terminar el post con una recomendación.","Escribí una frase.",[["lector","leen","lee","otros","viajar","visitar"],["ayuda","consejo","recomienda","sirve","útil","util"]],1,"Porque le da al lector un consejo útil si viaja a ese lugar.",n="analizar")]]
M8={"subject_id":SID,"tema":8,"practica":"Práctica general: Around the World","examen_titulo":"Nivel jefe: Around the World","niveles":{"1":B1,"2":B2,"3":B3,"4":B4},"act":ACT8,"examen":EX8}
ST8={1:"fc7e0214-0a8b-44a0-a1da-7c38a3eca3aa",2:"362db273-8930-4f4d-b089-8b7b5eb30a0d",3:"d1d5bdc0-df66-4488-8b5b-f9b2dfda9232",4:"85f68602-347f-4adb-a993-a46a6078c5c5"}
TI8={1:"Countries, cultures and nationalities",2:"Travel plans: itineraries",3:"Asking for help while travelling",4:"Writing a travel blog post"}
CL8={1:[
 NOT("EL MUNDO","¿De dónde sos?","Países, nacionalidades e idiomas","🌍","AROUND THE WORLD","países y culturas",["Noticia: ¿de dónde sos?","Países, nacionalidades e idiomas.","Hoy: *around the world*."]),
 MAPA("mundo",[{"resaltar":["Japón"],"texto":"Japan · Japanese"},{"resaltar":["Brasil"],"color":"#7fb6ff","texto":"Brazil · Brazilian"},{"resaltar":["Francia"],"color":"#ffb36b","texto":"France · French"}],["Viajemos por el mapa.","*Japan*: la gente es *Japanese*.","*Brazil*: la gente es *Brazilian*.","*France*: la gente es *French*."]),
 TB("TERMINACIONES",["Terminación","Ejemplo"],[["-ian","Argentinian, Brazilian"],["-ese","Japanese, Chinese"],["-ish","Spanish, British"]],["Tres terminaciones frecuentes.","Con *ian*: Argentinian.","Con *ese*: Japanese.","Con *ish*: Spanish."]),
 ORA("UNA PRESENTACIÓN",[("She","sujeto"),("is","verbo"),("Japanese","complemento")],"Ella es japonesa",["Primero, *quién*.","Después, el verbo *is*.","Y la nacionalidad, con *mayúscula*.","Significa que ella es japonesa."]),
 Q("In Brazil, people speak…",["Brazilian","Portuguese","Spanish"],1,["Te toca: Brasil.","¿*Brazilian*, *Portuguese* o *Spanish*?","*Portuguese*."]),
 ER([("She is japanese","She is Japanese"),("He is from Mexican","He is from Mexico")],["Errores típicos.","La nacionalidad en *minúscula*.","Y confundir *país* con *nacionalidad*."]),
 RES(["Repasemos.","País: *Japan*. Nacionalidad: *Japanese*.","Siempre con *mayúscula*.","El idioma no siempre coincide.","¡Clase terminada! Ahora, *a practicar*."],[["PAÍS","Japan"],["NACIONALIDAD","Japanese"],["MAYÚSCULA","siempre"]])],
2:[
 RET("¿Qué conector abre un itinerario: first o finally?",6,"First","🗺️","ITINERARIOS","planes de viaje",["Desafío: ¿qué conector va primero? Seis segundos.","*First*.","Hoy: *itinerarios de viaje*."]),
 LI("MI ITINERARIO",[("Day 1","Fly to Rome","✈️"),("Day 2","Visit the Colosseum","🏛️"),("Day 3","Train to Florence","🚆")],["*Día uno*: volar a Roma.","*Día dos*: visitar el Coliseo.","*Día tres*: tren a Florencia."]),
 FL("PARA ORDENAR",[("First","1️⃣"),("Then","2️⃣"),("After that","3️⃣"),("Finally","🏁")],["Primero, *first*.","Después, *then*.","Luego, *after that*.","Y al final, *finally*."]),
 TAR("CÓMO VIAJAR",[("by plane","en avión","✈️"),("by train","en tren","🚆"),("on foot","a pie","🚶")],["En *avión*.","En *tren*.","Y *a pie*: on foot."]),
 Q("We are going to travel ___ train.",["in the","by","with"],1,["Te toca: el transporte.","¿*In the*, *by* o *with*?","*By* train."]),
 ER([("by the plane","by plane"),("by foot","on foot")],["Errores típicos.","Poner *the* después de by.","Y decir *by foot*: es *on foot*."]),
 RES(["Repasemos.","El itinerario usa *going to*.","Los conectores *ordenan* los días.","El transporte va con *by*.","¡Clase terminada! Ahora, *a practicar*."],[["PLANES","going to"],["ORDEN","first, then, finally"],["TRANSPORTE","by plane"]])],
3:[
 DIA([("Turista","🧳"),("Vecina","👩")],[(0,"Excuse me, could you help me?","Disculpe, ¿me podría ayudar?"),(1,"Sure!","¡Claro!"),(0,"Could you tell me where the station is?","¿Me podría decir dónde está la estación?"),(1,"Go straight on and turn left.","Siga derecho y doble a la izquierda.")],["El turista llama la atención con *Excuse me*.","La vecina acepta.","Pregunta con cortesía *dónde está la estación*.","Y recibe las *indicaciones*."]),
 PA("INDICACIONES",[("Go straight on","⬆️"),("Turn left","⬅️"),("Turn right","➡️"),("It's on the corner","📍")],["Cuatro indicaciones.","*Go straight on*: seguir derecho.","*Turn left*: a la izquierda.","*Turn right*: a la derecha.","*On the corner*: en la esquina."]),
 DEF("Pregunta indirecta","Después de Could you tell me, el verbo va al final: where the station is.","🔀",["La *pregunta indirecta* es más amable.","El verbo va *al final*."]),
 PRO("PARA PRACTICAR",[("excuse me","ekskiús mi","disculpe"),("station","stéishon","estación")],["Primera expresión: *excuse me*.","Segunda palabra: *station*."]),
 Q("Could you tell me where the bank ___ ?",["is","are","does"],0,["Te toca: el final.","¿*Is*, *are* o *does*?","*Is*, al final."]),
 ER([("where is the station?","where the station is?"),("Can you give me a map","Could you give me a map, please?")],["Errores típicos.","Dejar el verbo *antes* en la indirecta.","Y olvidar la *cortesía*."]),
 RES(["Repasemos.","Empezá con *Excuse me*.","Pedí con *Could you*.","En la indirecta, el *verbo al final*.","¡Clase terminada! Ahora, *a practicar*."],[["LLAMAR","Excuse me"],["PEDIR","Could you…?"],["INDIRECTA","where it is"]])],
4:[
 HIS(("Sofi","👧"),"🏔️",["Sofi volvió de Cusco con mil fotos.","Quiere contarlo en su blog, pero en inglés."],"MI BLOG","post de viaje",["Te presento a *Sofi*.","Volvió de *Cusco*.","Quiere escribir un *blog* en inglés."]),
 BQ("PARTES DEL POST",[("TÍTULO","My amazing week in Peru"),("QUÉ HICE","We walked to Machu Picchu."),("OPINIÓN","The view was breathtaking."),("CONSEJO","You should try the local food.")],["Un post tiene cuatro partes.","El *título* atrae al lector.","*Qué hiciste*, en pasado.","Tu *opinión*, con adjetivos fuertes.","Y un *consejo* para el lector."]),
 AD(("COMÚN","😐","The trip was good."),("FUERTE","🤩","The trip was amazing!"),["Con *good*, el texto queda chato.","Con *amazing*, el lector se entusiasma."]),
 TAR("VERBOS IRREGULARES",[("go → went","ir → fui","🚶"),("eat → ate","comer → comí","🍽️"),("see → saw","ver → vi","👀")],["*Go* pasa a *went*.","*Eat* pasa a *ate*.","*See* pasa a *saw*."]),
 Q("We ___ empanadas in Salta.",["eated","ate","eat"],1,["Te toca: pasado de *eat*.","¿*Eated*, *ate* o *eat*?","*Ate*: es irregular."]),
 RES(["Repasemos.","Lo que hiciste, en *pasado*.","Opiniones con *adjetivos fuertes*.","Cerrá con un *consejo*.","¡Clase terminada! Ahora, *a practicar*."],[["PASADO","went, ate, saw"],["ADJETIVOS","amazing, huge"],["CONSEJO","you should"]])]}

escribir(7, M7, ST7, TI7, CL7)
escribir(8, M8, ST8, TI8, CL8)
