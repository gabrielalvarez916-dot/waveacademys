# -*- coding: utf-8 -*-
"""Ciencias Naturales Integradas I · Misión 1 · Ciencia y método. Genera mision-1.json (se carga con cargar_mision)."""
import os, sys, io, base64, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "matematica-1", "mision-4"))
from base import *
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
V, O, C = "#0e7c7b", "#243b3f", "#d8f0ea"
def png(fig):
    b = io.BytesIO(); fig.savefig(b, format="png", dpi=110, bbox_inches="tight", facecolor="white"); plt.close(fig)
    im = Image.open(io.BytesIO(b.getvalue())).convert("RGB").quantize(colors=16); o = io.BytesIO(); im.save(o, format="PNG", optimize=True); return base64.b64encode(o.getvalue()).decode()
def IMG(t, pie, desc, b64): return {"tipo":"imagen","imagen_tipo":"diagrama","titulo":t,"texto":pie,"imagen_descripcion":desc,"imagen_fuente":"Dibujo propio (matplotlib).","png_base64":b64}
def fig_regla():
    fig, ax = plt.subplots(figsize=(7, 1.7)); ax.set_xlim(11.4, 13.6); ax.set_ylim(-0.6, 1.3); ax.axis("off")
    ax.add_patch(plt.Rectangle((11.4, 0), 2.2, 0.8, facecolor="#f4e3b5", edgecolor="#8a6a2a"))
    for i in range(114, 137):
        x = i / 10; h = 0.4 if i % 10 == 0 else (0.28 if i % 5 == 0 else 0.18); ax.plot([x, x], [0.8, 0.8 - h], color=O, lw=1)
        if i % 10 == 0: ax.text(x, 0.25, f"{i//10}", ha="center", fontsize=10, color=O)
    ax.add_patch(plt.Rectangle((11.4, 0.92), 0.93, 0.16, facecolor="#f2b33d", edgecolor=O)); ax.plot([12.33, 12.33], [0.75, 1.1], color="#c0392b", lw=1.6)
    ax.text(12.33, -0.35, "punta del lápiz: entre 12,3 y 12,4 → 12,3 ± 0,1 cm", ha="center", fontsize=10, color=V, weight="bold")
    return png(fig)

N1={"objetivo":"Vas a poder reconocer los instrumentos de laboratorio más comunes y elegir el adecuado para cada tarea.",
"vas_a_ver":["Instrumentos para medir","Instrumentos para contener y calentar","Instrumentos para ver","Cómo elegir el instrumento correcto"],
"secciones":[
 S(1,"Instrumentos para medir",[D("Medir","Comparar una cantidad con una unidad. Cada magnitud tiene su instrumento."),
  T("Para medir",["Instrumento","Qué mide","Unidad"],[["Probeta","Volumen de líquidos","ml"],["Balanza","Masa","g"],["Termómetro","Temperatura","°C"],["Cronómetro","Tiempo","s"],["Regla","Longitud","cm, mm"]])]),
 S(1,"Para contener y calentar",[T("Para contener y calentar",["Instrumento","Para qué sirve"],[["Vaso de precipitado","Contener y calentar líquidos (medida aproximada)"],["Tubo de ensayo","Mezclar cantidades chicas"],["Matraz","Mezclar y agitar sin que salpique"],["Mechero","Dar calor con una llama"],["Gradilla","Sostener los tubos de ensayo"]])]),
 S(2,"Para ver lo pequeño",[P("La <b>lupa</b> aumenta unas pocas veces el tamaño de lo que miramos. El <b>microscopio</b> aumenta cientos de veces y permite ver células y microorganismos que a simple vista no se ven.")]),
 S(2,"Elegir bien",[E("¿Vaso o probeta?","Hay que medir 50 ml de agua exactos.",["El vaso de precipitado tiene marcas, pero son aproximadas.","La probeta es angosta y sus marcas son precisas.","Se usa la probeta."])]),
],
"ejemplo_completo":{"titulo":"preparar agua tibia","planteo":"Hay que calentar 100 ml de agua hasta 40 °C. ¿Qué instrumentos se usan?","pasos":["Medir 100 ml con la probeta.","Pasar el agua a un vaso de precipitado.","Calentar con el mechero.","Controlar con el termómetro hasta que marque 40 °C."]},
"ejemplo_incompleto":{"titulo":"completar","planteo":"Completá los espacios.","pasos":["La masa se mide con la ___ .","Los tubos de ensayo se apoyan en la ___ ."]},
"ejemplo_solo":{"titulo":"la hoja","planteo":"Querés ver las células de una hoja. ¿Qué instrumento usás?"},
"tip":{"titulo":"Medir o contener","texto":"Antes de agarrar un instrumento, preguntate: ¿necesito medir con precisión o solo contener? Si es medir, buscá el instrumento con escala precisa."},
"ojo":["Medir un volumen exacto con el vaso de precipitado.","Calentar un tubo de ensayo apuntando hacia una persona."],
"resumen":[{"titulo":"Medir","texto":"Probeta, balanza, termómetro, cronómetro."},{"titulo":"Contener","texto":"Vaso, tubo, matraz."},{"titulo":"Calentar","texto":"Mechero."},{"titulo":"Ver","texto":"Lupa y microscopio."}],
"glosario":[{"palabra":"Probeta","significado":"Tubo graduado para medir volumen."},{"palabra":"Balanza","significado":"Mide la masa."},{"palabra":"Mechero","significado":"Da calor con una llama."},{"palabra":"Gradilla","significado":"Soporte para tubos de ensayo."},{"palabra":"Microscopio","significado":"Aumenta cientos de veces lo que se observa."}],
"carpeta":["¿Con qué instrumento se mide la temperatura?","¿Qué instrumento sirve para medir 30 ml de un líquido con precisión?","¿Qué instrumento da calor con una llama?","Para ver bacterias, ¿alcanza con una lupa o hace falta un microscopio?"],
"respuestas_carpeta":[["termometro","termómetro","el termómetro"],["probeta","la probeta"],["mechero","el mechero"],["microscopio","un microscopio","el microscopio"]],
"soluciones":{"incompleto":"Balanza. Gradilla.","solo":"El microscopio.","carpeta":["El termómetro.","La probeta.","El mechero.","Un microscopio."]}}
N2={"objetivo":"Vas a poder aplicar las normas de seguridad del laboratorio y reconocer las señales de peligro de las etiquetas.",
"vas_a_ver":["Elementos de protección","Normas de oro","Cómo oler una sustancia","Señales de peligro","Qué hacer ante un accidente"],
"secciones":[
 S(1,"Protección",[D("Elementos de protección","<b>Antiparras</b> para los ojos, <b>guardapolvo</b> para la ropa y la piel, <b>guantes</b> para las manos. El pelo largo, atado.")]),
 S(1,"Normas de oro",[T("Normas",["Norma","Por qué"],[["No comer, beber ni probar nada","Las sustancias pueden ser tóxicas"],["Oler abanicando con la mano","Llega poco vapor a la nariz"],["No correr","Se pueden volcar o romper cosas"],["Avisar cualquier accidente","Se actúa rápido"],["Leer la etiqueta antes de usar","Dice si hay peligro"]])]),
 S(2,"Señales de peligro",[P("Las etiquetas usan <b>pictogramas</b>: dibujos con borde rojo que avisan el peligro."),
  T("Pictogramas",["Dibujo","Significa","Cuidado"],[["Llama","Inflamable","Lejos del fuego"],["Calavera","Tóxico","No tocar ni oler"],["Mano corroída","Corrosivo","Quema la piel"],["Explosión","Explosivo","No golpear ni calentar"]])]),
 S(2,"Ante un accidente",[P("Si algo se rompe, salpica o te lastimás: <b>avisar enseguida</b> al adulto a cargo. Si una sustancia toca la piel o los ojos, se lava con <b>mucha agua</b>. Nunca esconder un accidente.")]),
],
"ejemplo_completo":{"titulo":"el frasco con calavera","planteo":"Tenés que usar un frasco con una calavera en la etiqueta. ¿Qué cuidados tomás?","pasos":["La calavera significa tóxico.","Uso guantes y antiparras.","No lo huelo directo: si hace falta, abanico.","Me lavo las manos al terminar."]},
"ejemplo_incompleto":{"titulo":"completar","planteo":"Completá los espacios.","pasos":["Para proteger los ojos se usan ___ .","Una etiqueta con una llama indica que la sustancia es ___ ."]},
"ejemplo_solo":{"titulo":"el vaso roto","planteo":"Se te cayó un vaso de precipitado y se rompió. ¿Qué es lo primero que hacés?"},
"tip":{"titulo":"Leé antes de tocar","texto":"La etiqueta es lo primero: dice qué es y qué peligro tiene. Diez segundos de lectura evitan accidentes."},
"ojo":["Oler un frasco directo.","No avisar un accidente por vergüenza."],
"resumen":[{"titulo":"Protección","texto":"Antiparras, guardapolvo, guantes, pelo atado."},{"titulo":"Normas","texto":"No probar, abanicar, no correr, avisar."},{"titulo":"Señales","texto":"Inflamable, tóxico, corrosivo, explosivo."},{"titulo":"Accidente","texto":"Avisar y lavar con agua."}],
"glosario":[{"palabra":"Antiparras","significado":"Anteojos de protección."},{"palabra":"Pictograma","significado":"Dibujo que avisa un peligro."},{"palabra":"Inflamable","significado":"Que se prende fuego fácilmente."},{"palabra":"Tóxico","significado":"Que es venenoso."},{"palabra":"Corrosivo","significado":"Que quema o destruye la piel y los materiales."}],
"carpeta":["¿Se puede probar una sustancia en el laboratorio? Respondé sí o no.","¿Cómo se huele una sustancia: directo o abanicando?","¿Qué significa una etiqueta con una calavera?","Si una sustancia te salpica la piel, ¿con qué se lava?"],
"respuestas_carpeta":[["no"],["abanicando"],["toxico","tóxico","que es tóxico"],["agua","con agua","mucha agua"]],
"soluciones":{"incompleto":"Antiparras. Inflamable.","solo":"Avisar al adulto a cargo, sin tocar los vidrios.","carpeta":["No.","Abanicando con la mano.","Tóxico.","Con mucha agua."]}}
N3={"objetivo":"Vas a poder expresar una medición con su incertidumbre y su unidad, y mejorarla repitiendo y promediando.",
"vas_a_ver":["Por qué ninguna medida es perfecta","La apreciación del instrumento","Cómo se escribe el resultado","Medir varias veces y promediar","El error de paralaje"],
"secciones":[
 S(1,"Ninguna medida es perfecta",[D("Incertidumbre","Es el <b>margen de duda</b> de toda medición. Depende del instrumento, de quien mide y de cómo se mide."),
  P("Si dos personas miden la misma mesa y obtienen 120 cm y 121 cm, puede que ninguna se haya equivocado: las dos medidas están dentro de la incertidumbre.")]),
 S(1,"La apreciación",[D("Apreciación","Es la <b>menor medida</b> que puede marcar un instrumento. En una regla común es 1 mm; en una balanza de cocina, 1 g."),
  IMG("Medir con una regla","La punta queda entre dos marcas de milímetro.","Regla con marcas de milímetro; un lápiz termina entre 12,3 y 12,4 cm.",fig_regla())]),
 S(2,"Cómo se escribe",[P("El resultado se escribe <b>valor ± incertidumbre</b> y con <b>unidad</b>: 12,3 ± 0,1 cm. Significa que el largo real está entre 12,2 y 12,4 cm.")]),
 S(2,"Promediar y leer bien",[E("Tres mediciones","Un lápiz se midió tres veces: 12,2 cm; 12,4 cm y 12,3 cm.",["Se suman: 12,2 + 12,4 + 12,3 = 36,9.","Se divide por la cantidad de medidas: 36,9 ÷ 3 = 12,3.","Resultado: 12,3 cm."]),
  P("<b>Error de paralaje</b>: si se lee una probeta o una regla mirando en diagonal, el valor da mal. Hay que poner los ojos a la altura de la marca.")]),
],
"ejemplo_completo":{"titulo":"la temperatura","planteo":"Un termómetro marca de a 1 °C. Se midió el agua tres veces: 21 °C, 23 °C y 22 °C. Escribí el resultado.","pasos":["Apreciación del termómetro: 1 °C.","Promedio: (21 + 23 + 22) ÷ 3 = 22.","Resultado: 22 ± 1 °C.","La temperatura real está entre 21 y 23 °C."]},
"ejemplo_incompleto":{"titulo":"completar","planteo":"Completá los espacios.","pasos":["La apreciación de una regla común es 1 ___ .","Si el resultado es 50 ± 1 g, el valor real está entre 49 g y ___ g."]},
"ejemplo_solo":{"titulo":"la probeta","planteo":"Se midió un volumen tres veces: 40 ml, 42 ml y 41 ml. ¿Cuál es el promedio?"},
"tip":{"titulo":"Siempre tres partes","texto":"Un resultado completo tiene tres partes: el valor, la incertidumbre y la unidad. Si falta una, está incompleto."},
"ojo":["Escribir un resultado sin incertidumbre ni unidad.","Leer la probeta mirando desde arriba."],
"resumen":[{"titulo":"Incertidumbre","texto":"Margen de duda de toda medida."},{"titulo":"Apreciación","texto":"La menor marca del instrumento."},{"titulo":"Resultado","texto":"Valor ± incertidumbre + unidad."},{"titulo":"Promedio","texto":"Medir varias veces mejora el resultado."}],
"glosario":[{"palabra":"Incertidumbre","significado":"Margen de duda de una medición."},{"palabra":"Apreciación","significado":"Menor medida que marca un instrumento."},{"palabra":"Promedio","significado":"Suma de los valores dividida por la cantidad."},{"palabra":"Paralaje","significado":"Error por mirar la escala en diagonal."},{"palabra":"Precisión","significado":"Qué tan finas son las medidas de un instrumento."}],
"carpeta":["¿Cuál es el promedio de 10 cm, 12 cm y 11 cm? Respondé solo el número.","Si un resultado es 30 ± 2 °C, ¿cuál es el valor más bajo posible? Respondé solo el número.","¿Cuál es la apreciación de una regla común: 1 mm o 1 cm?","¿Para leer una probeta los ojos van desde arriba o a la altura de la marca?"],
"respuestas_carpeta":[["11","11 cm","11cm"],["28","28 °C","28°C"],["1 mm","1mm","mm"],["a la altura","a la altura de la marca","altura"]],
"soluciones":{"incompleto":"mm. 51.","solo":"41 ml: (40 + 42 + 41) ÷ 3.","carpeta":["11 cm.","28 °C.","1 mm.","A la altura de la marca."]}}
N4={"objetivo":"Vas a poder usar las unidades del Sistema Internacional, sus prefijos, y escribir números en notación científica.",
"vas_a_ver":["El Sistema Internacional","Los prefijos","Qué es la notación científica","Números grandes","Números chicos"],
"secciones":[
 S(1,"El Sistema Internacional",[D("Sistema Internacional (SI)","Conjunto de unidades que usan los científicos de todo el mundo para entenderse."),
  T("Unidades básicas",["Magnitud","Unidad","Símbolo"],[["Longitud","metro","m"],["Masa","kilogramo","kg"],["Tiempo","segundo","s"],["Temperatura","kelvin (y °C en la vida diaria)","K"]])]),
 S(1,"Los prefijos",[T("Prefijos",["Prefijo","Significa","Ejemplo"],[["kilo (k)","1000 veces","1 km = 1000 m"],["centi (c)","la centésima parte","1 m = 100 cm"],["mili (m)","la milésima parte","1 m = 1000 mm"],["micro (µ)","la millonésima parte","1 m = 1 000 000 µm"]])]),
 S(2,"Notación científica",[D("Notación científica","Se escribe un número entre 1 y 10 multiplicado por una <b>potencia de 10</b>. El exponente indica cuántos lugares se corrió la coma."),
  E("Un número grande","Distancia Tierra–Sol: 150 000 000 000 m.",["La coma se corre a la izquierda hasta dejar 1,5.","Saltó 11 lugares.","Resultado: 1,5 × 10¹¹ m (exponente positivo)."])]),
 S(2,"Números chicos",[E("Una bacteria","Mide 0,000 002 m.",["La coma se corre a la derecha hasta dejar 2.","Saltó 6 lugares.","Resultado: 2 × 10⁻⁶ m (exponente negativo)."]),
  P("Regla: números <b>grandes</b>, exponente <b>positivo</b>; números <b>menores que 1</b>, exponente <b>negativo</b>.")]),
],
"ejemplo_completo":{"titulo":"de kilómetros a metros","planteo":"Una ruta mide 3,5 km. ¿Cuántos metros son? Escribilo también en notación científica.","pasos":["Kilo significa 1000.","3,5 × 1000 = 3500 m.","En notación científica, la coma salta 3 lugares.","3500 m = 3,5 × 10³ m."]},
"ejemplo_incompleto":{"titulo":"completar","planteo":"Completá los espacios.","pasos":["4000 = 4 × 10^___ .","0,03 = 3 × 10^___ ."]},
"ejemplo_solo":{"titulo":"los centímetros","planteo":"¿Cuántos centímetros hay en 2,5 m?"},
"tip":{"titulo":"Contá los saltos","texto":"Marcá con flechitas cada lugar que salta la coma. La cantidad de flechitas es el exponente; si el número era chico, va con signo menos."},
"ojo":["Dejar adelante un número mayor que 10, como 30 × 10².","Confundir el signo del exponente en números chicos."],
"resumen":[{"titulo":"SI","texto":"Metro, kilogramo, segundo, kelvin."},{"titulo":"Prefijos","texto":"Kilo, centi, mili, micro."},{"titulo":"Notación","texto":"Número entre 1 y 10 × 10ⁿ."},{"titulo":"Exponente","texto":"Positivo para grandes, negativo para chicos."}],
"glosario":[{"palabra":"Unidad","significado":"Cantidad que se usa para comparar al medir."},{"palabra":"Prefijo","significado":"Parte que agranda o achica una unidad."},{"palabra":"Potencia de 10","significado":"10 multiplicado por sí mismo varias veces."},{"palabra":"Exponente","significado":"Número chiquito arriba que dice cuántas veces."},{"palabra":"Notación científica","significado":"Forma corta de escribir números muy grandes o muy chicos."}],
"carpeta":["¿Cuántos metros hay en 2 km? Respondé solo el número.","¿Cuántos milímetros hay en 1 m? Respondé solo el número.","En 7 × 10³, ¿cuál es el exponente? Respondé solo el número.","Para un número menor que 1, ¿el exponente es positivo o negativo?"],
"respuestas_carpeta":[["2000","2000 m"],["1000","1000 mm"],["3"],["negativo"]],
"soluciones":{"incompleto":"3. −2.","solo":"250 cm.","carpeta":["2000 m.","1000 mm.","3.","Negativo."]}}
ACT={
"1":[{"t":"matching","p":"Uní cada instrumento con lo que mide.","o":{"izquierda":["Probeta","Balanza","Termómetro","Cronómetro"],"derecha":["Volumen","Masa","Temperatura","Tiempo"]},"r":{"pares":{"Probeta":"Volumen","Balanza":"Masa","Termómetro":"Temperatura","Cronómetro":"Tiempo"}},"e":"Cada magnitud tiene su instrumento."},
     MC("¿Qué instrumento sirve para ver células?",["Lupa","Microscopio","Probeta","Gradilla"],"Microscopio","Aumenta cientos de veces.")],
"2":[{"t":"classify","p":"Clasificá cada acción.","o":{"elementos":["Usar antiparras","Oler abanicando","Probar una sustancia","Correr en el laboratorio"],"categorias":["Seguro","Peligroso"]},"r":{"categorias":{"Usar antiparras":"Seguro","Oler abanicando":"Seguro","Probar una sustancia":"Peligroso","Correr en el laboratorio":"Peligroso"}},"e":"Las normas de oro evitan accidentes."},
     MC("Una etiqueta con una llama indica que la sustancia es…",["Tóxica","Inflamable","Corrosiva","Inofensiva"],"Inflamable","Hay que mantenerla lejos del fuego.")],
"3":[N("Se midió tres veces el largo de un cuaderno: 20 cm, 22 cm y 21 cm. ¿Cuál es el promedio en cm?",{"acepta":[21]},"(20 + 22 + 21) ÷ 3 = 21."),
     MC("¿Cuál es un resultado completo?",["12,3","12,3 cm","12,3 ± 0,1 cm","Más o menos 12"],"12,3 ± 0,1 cm","Valor, incertidumbre y unidad.")],
"4":[MC("¿Cómo se escribe 6000 en notación científica?",["6 × 10³","60 × 10²","6 × 10⁻³","0,6 × 10⁴"],"6 × 10³","La coma salta 3 lugares a la izquierda."),
     N("¿Cuántos metros son {k} km?",{"formula":"k*1000"},"Kilo significa mil.",{"vars":{"k":{"min":2,"max":9}}})],
"5":[MC("Relámpago. ¿Con qué se mide la masa?",["Balanza","Probeta","Termómetro"],"Balanza","En gramos.",tiempo=20),
     MC("Relámpago. La calavera en una etiqueta significa…",["Tóxico","Inflamable","Explosivo"],"Tóxico","Es veneno.",tiempo=20),
     MC("Relámpago. La apreciación de una regla común es…",["1 mm","1 cm","1 m"],"1 mm","La marca más chica.",tiempo=20),
     MC("Relámpago. 0,005 en notación científica es…",["5 × 10⁻³","5 × 10³","50 × 10⁻⁴"],"5 × 10⁻³","Número chico, exponente negativo.",tiempo=20)],
}
EXAMEN=[
 [1,MC("¿Qué instrumento mide el volumen de un líquido con precisión?",["Vaso de precipitado","Probeta","Tubo de ensayo","Gradilla"],"Probeta","El vaso solo da una medida aproximada.")],
 [1,MC("¿Para qué sirve el mechero?",["Medir","Dar calor","Sostener tubos","Ver células"],"Dar calor","Produce una llama.")],
 [1,VF("La lupa aumenta más que el microscopio.","Falso","El microscopio aumenta cientos de veces.")],
 [2,MC("¿Cómo se huele una sustancia en el laboratorio?",["Directo","Abanicando con la mano","No se puede saber","Probándola"],"Abanicando con la mano","Así llega poco vapor.")],
 [2,MC("¿Qué hay que hacer si se rompe un vaso?",["Esconderlo","Avisar enseguida","Juntarlo con la mano","Seguir trabajando"],"Avisar enseguida","Nunca se esconde un accidente.")],
 [2,VF("Un pictograma con una mano corroída indica una sustancia corrosiva.","Verdadero","Quema la piel.")],
 [3,MC("¿Qué significa 20 ± 1 °C?",["Que es exactamente 20","Que está entre 19 y 21 °C","Que está mal medido","Que es 21"],"Que está entre 19 y 21 °C","Es el margen de duda.")],
 [3,N("¿Cuál es el promedio de 8, 10 y 12?",{"acepta":[10]},"(8 + 10 + 12) ÷ 3.")],
 [3,MC("¿Cómo se evita el error de paralaje?",["Mirando desde arriba","Con los ojos a la altura de la marca","Midiendo rápido","Con otra regla"],"Con los ojos a la altura de la marca","Mirar en diagonal engaña.")],
 [4,MC("¿Cuál es la unidad de masa del Sistema Internacional?",["Gramo","Kilogramo","Litro","Metro"],"Kilogramo","Junto al metro y al segundo.")],
 [4,MC("¿Cómo se escribe 0,0004 en notación científica?",["4 × 10⁴","4 × 10⁻⁴","0,4 × 10⁻³","40 × 10⁻⁵"],"4 × 10⁻⁴","Número chico: exponente negativo.")],
 [4,N("¿Cuántos centímetros hay en 3 m?",{"acepta":[300]},"1 m = 100 cm.")],
 [4,VF("En notación científica el número de adelante tiene que estar entre 1 y 10.","Verdadero","Por eso 30 × 10² no es correcto.")],
]
M={"subject_id":"9fa85d7b-ee7a-4853-8486-a69f9b539c12","tema":2,"practica":"Práctica general: el laboratorio y la seguridad","examen_titulo":"Nivel jefe: el laboratorio y la seguridad","niveles":{"1":N1,"2":N2,"3":N3,"4":N4},"act":ACT,"examen":EXAMEN}
json.dump(M,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mision-2.json"),"w"),ensure_ascii=False)
print("ok")
