# Reglas fijas del PDF de Wave Academy

Versión del 18/11/2026. Copia también guardada en Supabase, tabla `reglas_fijas`, nombre "Reglas fijas del PDF".

## Quién hace qué

- El contenido de cada lección lo escribe Claude en sesión con Gaby. No se usa la API de IA para esto (es cara; la API queda solo para el Tutor y las correcciones).
- El contenido se guarda como borrador listo en `lesson_drafts.contenido` (JSON).
- GitHub dibuja el PDF con `tools/pdf/render_leccion.py` (lo llama `tools/pdf/generar.py`, workflow `pdfs-lecciones.yml`) y lo sube a la lección sin publicarla. GitHub no crea contenido: solo dibuja lo que está en el JSON.
- Por eso todo lo que el PDF necesite (texto, tablas, figuras) tiene que venir ya dentro del JSON.

## Estructura fija, en este orden

1. Portada: título y objetivo (qué va a poder hacer el alumno).
2. Lo que vas a ver: 4 a 6 puntos, en el orden en que aparecen.
3. Etapa 1, los conceptos principales: 2 a 3 conceptos, cada uno con definición y ejemplo.
4. Etapa 2, profundizamos: 2 a 3 ideas que amplían la etapa 1, cada una con ejemplo. Solo usa lo definido en la etapa 1.
5. Ejemplo completo: problema resuelto paso a paso, integrando las dos etapas.
6. Ejemplo incompleto: mismo tipo de problema con 2 a 4 huecos `___`, que se completan con lo ya explicado.
7. Hacelo solo: mismo tipo, un poco más difícil, una única respuesta.
8. Tip: consejo práctico, no repite nada.
9. Ojo con esto: 1 o 2 errores típicos de la ficha.
10. Resumen: 4 a 6 tarjetas, cada una con una frase y un mini ejemplo.
11. Glosario: 5 a 8 términos que aparecen en el PDF, en lenguaje del alumno.
12. Actividad de carpeta: 3 o 4 consignas, de simple a pensada, una apunta a un error típico.
13. Soluciones: al final de todo, letra chica: hueco(s) del incompleto, hacelo solo y cada consigna de carpeta. Cortas, sin volver a explicar. Es solo para que el alumno se corrija: la plataforma no las lee ni las usa para corregir.

## Reglas de contenido: explicar todo

Cada concepto principal se explica siempre así: (1) qué es, definición corta en recuadro; (2) para qué sirve o cómo se reconoce; (3) ejemplo fácil, con tabla o esquema si hay posiciones, pasos o partes; (4) una frase que conecta el ejemplo con la definición.

- Nada se usa antes de definirse (ni en una lección anterior que figure como "ya vista").
- Se explica completo lo que la lección necesita. Ejemplo: en el sistema decimal hay que decir qué es un sistema de numeración, cuántas cifras tiene, cómo se agrupa y por qué el lugar cambia el valor.
- Etapa 1 = lo indispensable. Etapa 2 = ampliaciones, casos especiales y usos. Nunca se mezclan.
- Cada concepto y cada idea de la etapa 2 lleva su propio ejemplo. Un ejemplo muestra un solo punto a la vez, de lo simple a lo complejo.
- En matemática se muestran todas las cuentas, paso por paso, recalculadas una por una.
- Se respeta la ficha: lo que "no entra" no aparece y no se adelantan lecciones posteriores.
- Voseo rioplatense, tono cálido y directo. Notación argentina (punto en los miles, coma en los decimales). Negrita solo en términos clave. No se inventan datos ni anécdotas.

## Cuadros e imágenes

- Tabla siempre que haya posiciones, comparaciones, equivalencias o pasos paralelos. Las tablas se escriben como tablas, no como imágenes.
- Imagen solo si es necesaria para entender. Máximo 4 por PDF. Nunca decorativa.
- Las figuras las crea Claude en la sesión (matplotlib o PIL, con los colores de Wave: #0e7c7b, #243b3f, #d8f0ea), las exporta a PNG y las guarda dentro del bloque en el campo `png_base64`. Así GitHub las dibuja sin hacer nada más.
- Solo si Claude NO puede crear la imagen (fotos reales, mapas, obras de arte) se deja el bloque sin `png_base64`, con `imagen_descripcion` exacta e `imagen_fuente`: el PDF muestra el recuadro "A INSERTAR" y se carga desde el admin.
- Cada imagen lleva título corto y pie de una oración que dice qué mirar. El texto se entiende igual sin ella.

## Campos del JSON (contenido)

Los de siempre: `objetivo`, `vas_a_ver`, `secciones[]` (con `titulo` y `bloques[]`), `resumen[]` (`titulo`, `texto`), `glosario[]` (`palabra`, `significado`).

Tipos de bloque: `parrafo`, `definicion`, `importante`, `tip`, `ojo`, `ejemplo` (con `titulo`, `texto`, `items`), `pasos`, `lista`, `tabla` (`columnas`, `filas`, `iguales` para columnas del mismo ancho), `imagen` (`imagen_tipo`, `titulo`, `texto`, `imagen_descripcion`, `imagen_fuente`, `png_base64`).

Nuevos (todos opcionales; un borrador viejo sin ellos se dibuja como antes):
- `secciones[].etapa`: 1 o 2. Muestra el banner "Etapa 1 / Etapa 2" al cambiar.
- `ejemplo_completo`, `ejemplo_incompleto`, `ejemplo_solo`: cada uno con `titulo`, `planteo`, `pasos[]` y, opcional, una tabla (`columnas`, `filas`, `iguales`).
- `tip`: `{titulo, texto}`. `ojo`: lista de textos.
- `carpeta`: lista de consignas.
- `soluciones`: `{incompleto: texto, solo: texto, carpeta: [texto, ...]}`.

## Largo real

Con el diseño actual, una lección completa sale de unas 8 páginas: portada, página de inicio y unas 6 de contenido. Entre 1.800 y 2.600 palabras.

## Qué hay de esto en el código

- Dibujo del PDF: `tools/pdf/render_leccion.py` (commit del 18/11/2026).
- Lo que NO se toca todavía: la fábrica de IA `generar-leccion` (no se usa), la actividad por consigna y el repaso, que se reemplazarán por los bancos de práctica y examen.
- Pendiente: el texto para el Tutor (`aTexto` en `fabrica-pdf`) todavía no incluye los campos nuevos.

## Pendiente de diseñar

- Frontend: cómo se ve por dentro un tema (misión con 4 niveles, cada nivel como máquina con 5 estaciones).
- Bancos de práctica y de examen.
- Nivel 4, proyecto, rehecho según aprendizaje basado en proyectos.
