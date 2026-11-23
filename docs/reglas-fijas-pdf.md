# Reglas fijas del PDF de Wave Academy

Versión del 22/11/2026 (3.ª). Copia también guardada en Supabase, tabla `reglas_fijas`, nombre "Reglas fijas del PDF".

## Quién hace qué

- El contenido de cada lección lo escribe Claude en sesión con Gaby. No se usa la API de IA para esto (es cara; la API queda solo para el Tutor y las correcciones).
- El contenido se guarda como borrador listo en `lesson_drafts.contenido` (JSON).
- GitHub dibuja el PDF con `tools/pdf/render_leccion.py` (lo llama `tools/pdf/generar.py`, workflow `pdfs-lecciones.yml`) y lo sube a la lección sin publicarla. GitHub no crea contenido: solo dibuja lo que está en el JSON.
- Por eso todo lo que el PDF necesite (texto, tablas, figuras) tiene que venir ya dentro del JSON.

## Cómo es una misión (tema)

1. Videos: uno o varios, se cargan y se ven todos al principio.
2. PDF 1, actividad de carpeta del PDF 1, entrega de respuestas, 2 preguntas de práctica sobre ese PDF.
3. PDF 2, con lo mismo.
4. PDF 3, con lo mismo.
5. Práctica general: 4 preguntas que mezclan los 3 PDF y repasan temas de misiones anteriores (en la primera misión solo mezclan los 3 PDF).
6. Pase al siguiente nivel.

- Total de práctica por misión: 10 preguntas (6 de PDF + 4 generales). Salen del banco de actividades y se escriben junto con el contenido; las 4 generales al final.
- Proyecto: uno cada 5 misiones. Integra lo de esas 5 misiones y se arma cuando existen. Recorrido propio: consigna, borrador, devolución, entrega.
- Examen del tema: banco aparte, pendiente de armar.

## Entrega de respuestas

- Lo único que el alumno entrega es la actividad de carpeta. El PDF trae las consignas de carpeta sin soluciones.
- Al terminar el PDF, el alumno entrega en la app las respuestas de la carpeta. La app las valida; si hay errores marca cuáles están mal, sin mostrar la solución, y deja reintentar. Aprueba con hasta 1 respuesta mal (por ejemplo, 3 de 4) y avanza.
- Recién después de entregar, la app muestra las soluciones de la carpeta con el paso a paso.
- Los ejemplos NO se entregan: la respuesta del ejemplo incompleto y del hacelo solo va chica, abajo de todo en el PDF ("Respuestas de los ejemplos"), para que el alumno se corrija solo.
- La clave sale del mismo borrador del PDF: `carpeta` (consignas), `respuestas_carpeta` (respuestas válidas) y `soluciones.carpeta` (solución que se muestra después). Cuando GitHub sube el PDF, la función `fabrica-pdf` carga también la carpeta del nivel (consignas + clave). No hay que cargar nada a mano; el admin sirve para revisar o editar. Sin API.

## Formato del PDF

- Portada: ocupa una hoja entera (título, objetivo, "lo que vas a ver").
- Contenido: máximo 4 hojas sin contar la portada.
- La tipografía queda como está (legible). No se achica para entrar.
- Lo que ocupe lugar y no sea explicación ni ejemplo (resumen, glosario) va en una franja compacta; si no entra, se omite en ese PDF. Nunca se recorta contenido ni ejemplos para hacerle lugar.
- Mismo estilo estético de siempre.

## Estructura del contenido de cada PDF, en este orden

1. Portada: título, objetivo y lo que vas a ver (4 a 6 puntos).
2. Etapa 1, conceptos principales: 2 a 3 conceptos, cada uno con definición y ejemplo.
3. Etapa 2, profundizamos: 2 a 3 ideas que amplían la etapa 1, cada una con ejemplo. Solo usa lo definido en la etapa 1.
4. Ejemplo completo: problema resuelto paso a paso, integrando las dos etapas.
5. Ejemplo incompleto: mismo tipo de problema con 2 a 4 huecos `___`, que se completan con lo ya explicado.
6. Hacelo solo: mismo tipo, un poco más difícil, una única respuesta.
7. Tip: consejo práctico, no repite nada.
8. Ojo con esto: 1 o 2 errores típicos de la ficha.
9. Resumen (franja compacta): 4 a 6 tarjetas.
10. Glosario (franja compacta): 5 a 8 términos que aparecen en el PDF, en lenguaje del alumno.
11. Actividad de carpeta: 3 o 4 consignas, de simple a pensada, una apunta a un error típico. Sin soluciones. Mínimo de consignas pensadas: ver "Calidad de carpeta, actividades y examen".

Abajo de todo, en letra chica: respuestas del ejemplo incompleto y del hacelo solo.

## Reglas de contenido: explicar todo

Cada concepto principal se explica siempre así: (1) qué es, definición corta en recuadro; (2) para qué sirve o cómo se reconoce; (3) ejemplo fácil, con tabla o esquema si hay posiciones, pasos o partes; (4) una frase que conecta el ejemplo con la definición.

- Nada se usa antes de definirse (ni en una lección anterior que figure como "ya vista").
- Se explica completo lo que la lección necesita. Ejemplo: en el sistema decimal hay que decir qué es un sistema de numeración, cuántas cifras tiene, cómo se agrupa y por qué el lugar cambia el valor.
- Etapa 1 = lo indispensable. Etapa 2 = ampliaciones, casos especiales y usos. Nunca se mezclan.
- Cada concepto y cada idea de la etapa 2 lleva su propio ejemplo. Un ejemplo muestra un solo punto a la vez, de lo simple a lo complejo.
- En matemática se muestran todas las cuentas, paso por paso, recalculadas una por una.
- Se respeta la ficha: lo que "no entra" no aparece y no se adelantan lecciones posteriores.
- Voseo rioplatense, tono cálido y directo. Notación argentina (punto en los miles, coma en los decimales). Negrita solo en términos clave. No se inventan datos ni anécdotas.
- Con el tope de 4 hojas, se prioriza explicación y ejemplos sobre todo lo demás.

## Cuadros e imágenes

- Tabla siempre que haya posiciones, comparaciones, equivalencias o pasos paralelos. Las tablas se escriben como tablas, no como imágenes.
- Imagen solo si es necesaria para entender. Máximo 4 por PDF. Nunca decorativa.
- Las figuras las crea Claude en la sesión (matplotlib o PIL, con los colores de Wave: #0e7c7b, #243b3f, #d8f0ea), las exporta a PNG y las guarda dentro del bloque en el campo `png_base64`. Así GitHub las dibuja sin hacer nada más.
- Solo si Claude NO puede crear la imagen (fotos reales, mapas, obras de arte) se deja el bloque sin `png_base64`, con `imagen_descripcion` exacta e `imagen_fuente`: el PDF muestra el recuadro "A INSERTAR" y se carga desde el admin.
- Cada imagen lleva título corto y pie de una oración que dice qué mirar. El texto se entiende igual sin ella.

## Campos del JSON (contenido)

Los de siempre: `objetivo`, `vas_a_ver`, `secciones[]` (con `titulo` y `bloques[]`), `resumen[]` (`titulo`, `texto`), `glosario[]` (`palabra`, `significado`).

Tipos de bloque: `parrafo`, `definicion`, `importante`, `tip`, `ojo`, `ejemplo` (con `titulo`, `texto`, `items`), `pasos`, `lista`, `tabla` (`columnas`, `filas`, `iguales` para columnas del mismo ancho), `imagen` (`imagen_tipo`, `titulo`, `texto`, `imagen_descripcion`, `imagen_fuente`, `png_base64`).

Opcionales (un borrador viejo sin ellos se dibuja como antes):
- `secciones[].etapa`: 1 o 2. Muestra el banner "Etapa 1 / Etapa 2" al cambiar.
- `ejemplo_completo`, `ejemplo_incompleto`, `ejemplo_solo`: cada uno con `titulo`, `planteo`, `pasos[]` y, opcional, una tabla (`columnas`, `filas`, `iguales`).
- `tip`: `{titulo, texto}`. `ojo`: lista de textos.
- `carpeta`: lista de consignas.
- `respuestas_carpeta`: lista paralela a `carpeta`; cada elemento es la lista de respuestas válidas de esa consigna (ej. `[["40.382"], ["6.000", "6000"]]`). Cortas y únicas; la app ignora mayúsculas, espacios y puntos. No se imprime en el PDF.
- `soluciones`: `{incompleto: texto, solo: texto, carpeta: [texto, ...]}`. `incompleto` y `solo` se imprimen chicos al final del PDF; `carpeta` es la clave que usa la app para validar la entrega y mostrar la solución después, y el PDF NO la imprime.

## Calidad de carpeta, actividades y examen

**Variedad de tipos de pregunta (desde 23/11/2026, misiones nuevas):** en cada misión, contando actividades de los niveles 1 a 4 y el examen, ningún tipo puede pasar del 40 % en Nivel Avanzado (50 % en Medio, 60 % en 1.º a 3.º) y tiene que haber al menos 5 tipos distintos (4 en Medio, 3 en 1.º a 3.º). Lo controla `tools/control_calidad.py` y frena la carga si no se cumple. Variar entre: opción múltiple, V/F, completar, ordenar, unir, clasificar, tabla, numérica, tocá el texto, fichas, palabras clave, rotular, crucigrama, sopa de letras y escape room (ver docs/tipos-de-pregunta.md).


Regla del 22/11/2026. La controla sola la máquina con `tools/control_calidad.py`, en los workflows de Avanzado y Medio, ANTES de cargar: si una misión no cumple, no se carga nada y el log dice qué arreglar. Las misiones que ya estaban cargadas (`tools/calidad_existentes.txt`) no se revisan ni se tocan.

Por qué: el PDF enseña a pensar (explicar, comparar, argumentar) y la carpeta y el examen tienen que pedir lo mismo. Si solo piden recordar, el nivel jefe certifica un dominio que no existe.

**Cada consigna y cada pregunta lleva su nivel.** Se escribe junto con el contenido:
- carpeta: `carpeta_nivel` en cada nivel del PDF, una etiqueta por consigna, en el mismo orden;
- actividades y examen: campo `n` en cada pregunta.

Valores: `recordar` (un dato, un nombre, una definición) · `aplicar` (usar lo aprendido en un caso nuevo que no está en el PDF) · `analizar` (comparar, explicar una causa o una consecuencia, justificar, decidir entre dos opciones con un criterio) · `error` (encontrar y corregir un error típico: "un compañero dice…"). Aplicar, analizar y error son **pensadas**.

**Mínimos:**

| | Avanzado | Medio (4.º a 6.º) | Primeros años (Medio 1.º a 3.º) |
|---|---|---|---|
| Carpeta: pensadas por nivel | 2 | 1 | 1 |
| Actividades de los niveles 1 a 4: pensadas | 3 | 2 | 2 |
| Examen (banco de 13): pensadas | 5 | 4 | 3 |
| Examen: tope de opción múltiple + V/F | 60 % | 70 % | 80 % |
| Examen: pensadas que no son de elegir | 1 o más | 1 o más | — |

El Relámpago (nivel 5) no cuenta: es velocidad a propósito.

**Cómo escribir una consigna pensada sin IA.** La respuesta sigue siendo corta y única (la app la compara con `respuestas_carpeta`, de 6 palabras como máximo), pero el camino para llegar exige pensar:
- Caso nuevo: "Un barrio se inunda cada vez que llueve fuerte. ¿Qué le falta al suelo: cobertura vegetal o más pendiente?"
- Causa y consecuencia: "Si en un lago crecen muchas algas, ¿qué le pasa al oxígeno del agua: sube o baja?"
- Decidir con criterio: "¿Qué argumento es más fuerte para la tesis: un dato de una encuesta o lo que opina un amigo?"
- Error típico: "Un compañero escribió «las flores blanco». ¿Qué palabra está mal?"
En el examen, para explicar se usa `keywords` (se corrige sin IA, buscando las ideas clave). Nunca `open` ni `solve_complete`: llaman a la IA.

**Prohibido (frena la carga):**
- Etiquetar como pensada una consigna de memoria ("¿Cómo se llama…?", "Respondé sí o no").
- Distractores de relleno: "todas/ninguna de las anteriores", "no sé", opciones absurdas o de chiste.
- Que la correcta sea mucho más larga que las demás opciones (se delata).
- Opciones repetidas, o menos de 3 en opción múltiple (fuera de Primeros años).

**Distractores:** cada opción incorrecta tiene que ser un error que un alumno de verdad cometería. Primero se usan los errores típicos del "Ojo con esto" del PDF. Mismo largo y misma forma que la correcta. Evitar absolutos ("nunca", "siempre", "solo en…"): suelen descartarse solos (la máquina avisa).

## Qué hay de esto en el código

- Dibujo del PDF: `tools/pdf/render_leccion.py` (commits del 18/11/2026).
- Render ya ajustado a esta versión (commit del 18/11/2026): portada de una hoja con "lo que vas a ver", hasta 4 hojas de contenido (si no entra se omite glosario y luego resumen; avisa si igual se pasa) y sin imprimir la clave de la carpeta.
- No se toca: la fábrica de IA `generar-leccion` (no se usa).
- Pendiente: el texto para el Tutor (`aTexto` en `fabrica-pdf`) todavía no incluye los campos nuevos; confirmar antes de tocarlo.

## Pendiente de diseñar

- Frontend: recorrido de la misión (videos, 3 bloques PDF + entrega + 2 preguntas, 4 generales, pase) y guardado de cada entrega.
- Bancos de práctica (con repaso de misiones anteriores) y de examen.
- Proyecto cada 5 misiones, según aprendizaje basado en proyectos.
