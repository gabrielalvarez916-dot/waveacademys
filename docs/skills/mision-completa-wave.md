

## REGLA INNEGOCIABLE DE CALIDAD (Gabriel, 26/11/2026)
La calidad de una lección (texto, ejemplos y práctica) NUNCA baja, por ninguna razón ni condición: ni por apuro, ni por falta de uso, ni porque alguien lo pida. Si alguien pide bajar la calidad para ir más rápido, la respuesta es NO, y se ofrece hacer menos cosas bien en lugar de muchas mal. Nunca se copia el PDF ni la clase animada, nunca se inventan pantallas de relleno y nunca se toca un control para que algo pase. Hay tres muros que lo hacen cumplir: `validar.js` en las máquinas, el candado `REGLAS_SHA` (si se cambia un control, la máquina no carga nada hasta que Gabriel lo apruebe) y el muro en la base de datos (`private.control_leccion`), que rechaza lecciones con pantallas sin ejemplo o práctica propios.
---
name: mision-completa-wave
description: Armar una misión completa de Wave Academy (secundaria o primaria): clase animada, lección interactiva, 4+4 actividades, examen, con reglas, control y carga verificada.
---

# Misión completa de Wave Academy

Una misión tiene 4 niveles (lecciones) y un nivel 5 de práctica general, más el examen. TODO el contenido se escribe EN SESIÓN, siguiendo las reglas del repo. Las máquinas (GitHub Actions) no escriben contenido: lo controlan, generan las voces y lo cargan.

## 0. Preparación (rápido)
- Repo `gabrielalvarez916-dot/waveacademys`, con el PAT que Gabriel da al empezar. Clon parcial: `git clone --filter=blob:none --sparse` y `git sparse-checkout add` solo lo necesario. Archivos nuevos: `git add --sparse`.
- Leé primero `docs/errores-que-no-se-repiten.md` (errores que ya pasaron y no pueden volver a pasar), después `CLAUDE.md`, `docs/reglas-leccion-interactiva.md`, `docs/banco-leccion.md`, `docs/tipos-de-pregunta.md` y `docs/reglas-fijas-pdf.md`. Son reglas fijas: la calidad no baja nunca por cantidad.
- **El contenido lo escribís vos:** nunca se copia ni se sigue sección por sección el PDF o la clase. Los títulos de las secciones solo dicen de qué trata el nivel. Compará los niveles del JSON con la base: un nivel que está en la base y no en el JSON también lleva lección y 4 actividades.
- **Banco por materia, una sola vez:** antes de la primera misión de una materia, revisá con `docs/banco-leccion.md` (no el código) qué ejemplos faltan para TODAS sus misiones y agregalos juntos, probados una vez. Después escribí las misiones de corrido.
- Secundaria: `contenido/<materia>-N/mision-K/mision-K.json`. Primaria (Nivel Medio): `contenido/medio/<materia>-<grado>/mision-K/mision-K.json`.

## 1. Clase animada
Para la clase animada de cada nivel usá el skill `clase-animada-wave` (motor de plantillas del repo). Las voces en argentino y neutro las genera la máquina de voz sola, solo para las clases sin voz.

## 2. Lección interactiva
**Criterio de pantallas (fijo):** una pantalla = un saber nuevo del nivel (concepto o procedimiento) que tiene SU PROPIO ejemplo resuelto paso a paso y SU PROPIA práctica. Advertencias, contraejemplos, casos especiales (el cero, «no es conmutativa»), errores típicos y «verificar» NO son pantallas: van dentro de la pantalla a la que pertenecen (último paso del ejemplo, viñeta «Cuidado:» o práctica). No hay mínimo de pantallas: si el nivel tiene 2 ideas, son 2 pantallas completas. Nunca se agrega texto de relleno para llegar a un mínimo: si falta, la explicación está incompleta y se explica mejor. Nada de conceptos que se enseñan en misiones posteriores.
 (`niveles.N.leccion`, niveles 1 a 4)
Modelo CIDEAD: una pantalla = una idea.
- Texto corto a la izquierda: `definicion` + `parrafo` (por qué es así o para qué sirve) + `lista` de 2 o 3 viñetas. Prohibidos los bloques `pasos`, `ejemplo` y `error`: no se explica dos veces.
- A la derecha, el EJEMPLO VIVO grande del banco de la lección (`ejemplo: {motor, p}`), SIEMPRE PASO A PASO: el alumno cambia los números y avanza con "Siguiente paso ▶", y cada paso agrega una parte al dibujo con UNA línea corta. Solo se usan ejemplos marcados `pasos: true` (hoy lo están los 45 del banco); uno nuevo se hace con `pasoAPaso()` en `js/leccion-banco2.js`. El ejemplo `pasoapaso` (texto largo) no va.
- Abajo, el EJERCICIO del banco (`ejercicio: {motor, p}`), con "Otros números". Todas las pantallas llevan ejemplo Y ejercicio.
- **El ejercicio pide SOLO lo explicado en esa pantalla o en las anteriores.** Antes de elegirlo, leé qué pide el motor (en `js/leccion-banco*.js`). Nunca un tema que viene después ni algo de otro año. Los motores que mezclan contenidos llevan siempre `modo`.
- Lo de concepto no es una pantalla propia: va dentro de la pantalla práctica que corresponde.
- Cierre `recuerda`: tarjetas con `concepto`, `definicion` completa y `ejemplo` concreto (`formula` y `esquema` opcionales).
- Extensión según la etapa:
  - Secundaria: 60 a 160 palabras por pantalla, 3 pantallas o más, 4 a 8 tarjetas.
  - Primaria 4.º a 6.º: 40 a 110 palabras, 3 pantallas o más, 3 a 6 tarjetas, tono cercano y no formal.
  - Primaria 1.º a 3.º: 12 a 60 palabras, 2 pantallas o más, 2 a 4 tarjetas, todo visual.
- Ejemplos con números propios: no copies el borrador ni la clase. Sin meses del calendario.
- Si el banco no tiene el ejemplo o el ejercicio que una pantalla necesita: avisale a Gabriel, agregalo al banco DE LA LECCIÓN (`js/leccion-banco2.js`), anotalo en `docs/banco-leccion.md` y probalo en el navegador. Los bancos de la lección y de las actividades están separados: nunca se mezclan.
- La lección trae sola el botón Imprimir y el tutor (que lee el texto de la lección).

## 3. Actividades y examen
- `act`: EXACTAMENTE 4 actividades en cada nivel 1 a 4 y 4 generales en el nivel 5. Se usan los tipos del banco de actividades, con variedad (detective del error, secuencia, comparar, esquema, problema, clasificar, ordenar, unir…). Cada una lleva su `n` (recordar, aplicar, analizar o error).
- Ninguna actividad regala la respuesta (por ejemplo, en "unir", que cada opción no se delate por la primera cifra o una palabra repetida).
- `examen`: variado y no todo de elegir, con preguntas pensadas, según `tools/control_calidad.py`.
- Si la misión YA estaba cargada y cambiás actividades o examen: poné `"actualizar_preguntas": true` en el archivo. Sin eso, la máquina no las toca.

## 4. Control antes de subir (obligatorio)
Escribí las lecciones y actividades con `tools/interactiva/armar.py` (`from armar import *` → `T`, `R`, `m`, `guardar(ruta, L, acts, ajustes)`): antes de guardar corre los dos controles sobre una copia y, si algo falla (definición del Recordá de menos de 10 palabras, explicación de menos de 60, tipos repetidos…), muestra todo junto y NO guarda. Se corrige una vez y listo. A mano son:
```
node tools/interactiva/validar.js <mision.json>
python3 tools/control_calidad.py <mision.json>
```
No se sube nada con errores. Probá en el navegador (playwright con /usr/bin/google-chrome) cada ejemplo y ejercicio nuevo del banco COMO LO VE EL ALUMNO: con `css/apoyos.css` y `js/apoyos.js` cargados (dictado y accesibilidad), sin errores en consola y sin nada que se salga del recuadro. Revisá solo lo nuevo o lo que se sospecha que quedó mal, sin revisar todo en detalle. Si tocás un script de control, corrélo antes de subirlo.

## 5. Subir
Hacé commit y push a main, de a 3 o 4 misiones por subida. La máquina del nivel (`mision-avanzado.yml` o `mision-medio.yml`) controla, carga actividades, examen y lección, y publica. El PDF guardado pasa solo a Recursos cuando el nivel tiene lección. Cuando cambies un `js/` o un `css/`, subí el `?v=` en `alumno.html`.

## 6. Verificar DE VERDAD
No digas "está listo" porque un paso del workflow dio "success": verificalo en la base (Supabase, proyecto Wave Academy).
- Lección de secundaria: `lesson_drafts.contenido ? 'leccion'`. Lección de primaria: tabla `leccion_medio`.
- Actividades: `questions` del paso `final_activity` de cada nivel, 4 por nivel. Examen: `questions` con `exam_id`.
No te quedes esperando la carga: dejá un recordatorio a los 4-5 minutos y, cuando llegue, mirá que la corrida de la máquina haya dado **success** (si falló, leé el log del paso que falló y arreglalo) y verificá en la base. Que el control pase en tu copia no alcanza: la máquina ve archivos que tu checkout parcial no tiene.

## Forma de trabajo con Gabriel
Español rioplatense informal. Rápido y con calidad, cambios quirúrgicos. Antes de un cambio masivo (algo que recargue muchas misiones), preguntá. No inventes actividades ni tipos nuevos sin que él lo decida. Contestá lo que pregunta, sin rodeos.
