# MÁQUINA DEL NIVEL MEDIO · guía para armar una lección (separada de la del Avanzado: tools/clase y tools/pdf no se tocan)

## Cómo se hace una misión completa (todo automático)

1. Carpeta `contenido/medio/<materia>/mision-N/` con dos scripts:
   - `mision.py` → `mision-N.json`: los 4 PDF (con dibujos), actividades, Relámpago y examen. Lleva `subject_id` y `tema`.
   - `clases.py` → `tools/medio/clase/lecciones/<slug>.json`: las 4 clases animadas (con el `step_id` del paso de video de cada nivel). Imprime una línea por clase que empieza con su slug.
2. `bash tools/medio/controlar.sh contenido/medio/<materia>/mision-N` → arma y pasa todos los controles (incluida la **variedad del banco de formatos**, ver «Variedad»). Si marca algo, se corrige.
3. Subir a `main`. GitHub hace el resto solo, sin que nadie toque nada:
   - **Voz de las clases del NIVEL MEDIO** (`voz-clases-medio.yml`): graba la voz, arma el HTML y carga cada clase en su lección (`cargar_clase_medio`).
   - **Misiones del NIVEL MEDIO** (`mision-medio.yml`): carga actividades, Relámpago y examen (`cargar_mision_medio`) y arma y sube los PDF argentino y neutro (`pdf-medio`).
4. Cuando la misión queda **completa** (4 clases, 4 PDF, Relámpago y examen) **se publica sola** (`tools/medio/publicar.py` → `publicar_completas_medio`). Nunca despublica.

Separación con el Avanzado: esta máquina no usa ni modifica nada de `tools/clase`, `tools/pdf`, `tools/neutro.py`, `fabrica-pdf`, `cargar_mision` ni `cargar_clase`, y sus funciones de la base rechazan cualquier materia que no sea del Nivel Medio. Secreto de GitHub: `MEDIO_TOKEN` (= `gen_config.medio_token`).


Una lección = **un archivo** `tools/medio/clase/lecciones/<slug>.json`. Al subirlo a `main`, GitHub graba la voz (Jorge, Microsoft, +25 %) y arma el HTML (`tools/medio/clase/dist/<slug>.html`). Después **la carga sola en la plataforma** (`tools/medio/clase/cargar.py` → función `cargar_clase_medio`, que solo acepta lecciones del Nivel Medio): en el paso de video del nivel si la lección tiene `step_id`, o en la introducción de la materia si tiene `subject_id`.

## Formato

```json
{ "slug": "mat1-m2-n1", "step_id": "<id del paso de video del nivel>", "materia": "Matemática I",
  "titulo": "Título de la clase", "sub": "Matemática I · Misión 2 · Nivel 1",
  "escenas": [ { "t": "gancho", "voz": ["frase 1", "frase 2", "frase 3"], "grande": "2", "final": "200", "titulo": "...", "sub": "..." } ] }
```

- `voz`: **una frase por paso** de la plantilla (la cantidad está en la tabla de abajo). Si no coincide, el reproductor avisa el error.
- Palabras clave entre `*asteriscos*` → salen en amarillo en el subtítulo.
- Números con punto de miles (`4.000`, `53.608`): la voz los dice bien ("cuatro mil"). Romanos en mayúsculas (`MMXXVI`): los deletrea. `+` se dice "más" y `×` se dice "por".

## Estilo (lo que hace que funcione)

1. **Gancho** en los primeros 5 segundos, y **variado**: rotar entre `gancho` (pregunta o paradoja con números), `historia` (algo que le pasó a Juan, a Marta…), `chat` (mensajes de celular), `noticia` (placa de "último momento") y `reto` (desafío con cuenta regresiva). Nunca el mismo tipo en dos niveles seguidos.
2. **Una metáfora que atraviesa la lección** (la fábrica de alfajores). Concreta, cotidiana y argentina.
3. Recorrer **todo** el contenido del PDF, pero explicado (no leído): definición → ejemplo visual → por qué importa.
4. Frases cortas (6 a 14 palabras), ritmo de TikTok, segunda persona ("mirá", "fijate").
5. Momento sorpresa (algo se rompe, cambia o explota) cerca de la mitad.
6. Cierre: errores comunes → resumen → "¡a practicar!".
7. De 8 a 14 escenas (4 a 7 minutos).

## Variedad: ir rotando el banco de formatos (regla fija del Nivel Medio)

Las clases no pueden salir todas con el mismo molde: se van variando los formatos del banco (tabla de abajo). `revisar_contenido.py` lo controla y `controlar.sh` no deja subir si no se cumple.

1. **Cada clase** usa al menos **2 formatos distintos del banco** fuera de los básicos (básicos: pregunta, resumen, errores, definicion, consejo, frase, portada, tabla, clasificar, pasos y los ganchos).
2. **En una misión**, un mismo formato (fuera de los básicos) aparece como máximo en **3 de las 4 clases**, y no puede haber dos clases con la **misma secuencia** de escenas.
3. **Ganchos rotando**: el gancho de una clase no puede ser del mismo tipo que el de la clase anterior (gancho, historia, chat, noticia, reto).
4. **Contra la misión anterior** de la misma materia: cada misión nueva **suma al menos un formato del banco** que no estaba en la anterior, y ningún nivel repite la secuencia de escenas del mismo nivel de la misión anterior.
5. Si el tema pide un dibujo que el banco no tiene, se crea una plantilla nueva (en `motor/t-mate.js` u otro), se suma a la tabla de abajo y queda disponible para todas las materias del Nivel Medio.

## Banco de plantillas (pasos = frases de `voz`)

| t | pasos | datos |
|---|---|---|
| gancho | 3 | grande \| emoji, final, titulo, sub |
| historia | lineas + 1 | personaje:{nombre, emoji}, lugar (emoji), lineas (1-3), titulo, sub — gancho con un personaje: "A Marta le pasó…" |
| chat | mensajes + 1 | contacto:{nombre, emoji}, mensajes:[{yo, txt}] (2-5), titulo, sub — gancho como chat de celular |
| noticia | 3 | cinta, titular, bajada, emoji, titulo, sub — gancho como placa de noticiero |
| reto | 3 | texto, segundos, respuesta, emoji, titulo, sub — desafío con cuenta regresiva |
| portada | 1 | texto, sub, emoji |
| definicion | 2 | palabra, texto, emoji |
| dato | 2 | numero, antes, despues, texto, emoji |
| frase | 1 | texto, emoji, color |
| consejo | 1 | titulo, texto, emoji |
| errores | 1 + items | items:[{mal, bien}] (máx 3) |
| pregunta | 3 | pregunta, opciones:[...], correcta |
| resumen | 2 + items | items:[[cab, txt]] (máx 6), fin:{titulo, sub} |
| comparar | 3 (+1 con def) | a:{cab, texto, emoji, estilo:'piedra'}, b:{...}, signo, def:{cab, texto} |
| antesdespues | 2 | antes:{cab, emoji, texto}, despues:{...} |
| clasificar | 1 + cajas | cajas:[{cab, emoji}] (2-4), fichas:[{txt, caja}] |
| tabla | 1 + filas | titulo, columnas, filas |
| venn | 4 | a, b, itemsA, itemsB, ambos |
| balanza | 3 | izq:{cab, items}, der:{cab, items}, gana:'izq'\|'der' |
| matriz | 1 + celdas | titulo, celdas:[{cab, txt}] (4) |
| pasos | 1 + items | titulo, items:[txt \| {txt, emoji}] (máx 6) |
| ciclo | 1 + items | titulo, items (3-6) |
| flujo | items | titulo, items (2-5) |
| causas | 1 + items | causa:{txt, emoji}, items (2-4) |
| linea | eventos | titulo, eventos:[{fecha, txt, emoji}] (2-6) |
| mapa | 1 + pasos | zona:'mundo'\|'america'\|'sudamerica'\|'argentina', pasos:[{resaltar:[países en español], color, marcas:[{lon, lat, txt}], ruta:[[lon,lat],[lon,lat]], texto}] |
| barras | 1 + items | titulo, unidad, items:[{txt, valor}] |
| torta | 1 + items | titulo, items:[{txt, valor}] |
| curva | 2 + marcas | titulo, x, y, puntos:[[x,y]], marcas:[{x, y, txt}] |
| porcentaje | 2 | valor, txt, emoji |
| fichas | 3 | fichas:[...], grande, etiqueta |
| juntar | 3 | a:{emoji, n}, b:{emoji, n}, texto — dos grupos con su número y el +; se juntan en una caja; el total (a + b ≤ 10, primeros años) |
| agregar | 3 | emoji, n, mas, texto — el grupo con su número; los nuevos caen cuando la voz cuenta ("5, 6, 7"); el total (n + mas ≤ 10, primeros años) |
| sacar | 3 | emoji, n, menos, texto — el grupo con su número; se tachan y salen volando los que sacamos; lo que queda (n ≤ 10, primeros años) |
| agrupar | niveles + 1 | niveles:[{nombre, valor, icono:'alf'\|'pack'\|'caja'\|'camion'\|emoji}], salto |
| estante | 5 | numero, cab, dig, val, flechas, destacar, etiqueta |
| quitar | 5 | tarjetas:[{cab, val}×2], cab, dig, quitar, resultado, sello, etiqueta |
| descomponer | 5 | numero, titulo, partes, signo, tachar, resultado |
| multiplicar | 3 + cifras (− 1 si apagar) | titulo, cab, dig, val, apagar, ecuacion |
| canje | 5 | titulo, grande:{n, txt}, chico:{n, txt}, sueltos, ec1, ec2 |
| ejemplo | 7 | numero, cab, dig, val, lineas:[a, m], suma:[...], destacar, etiqueta |
| recta | 1 + marcas | min, max, paso, marcas:[{v, txt}] |
| cuenta | 2 | filas, op, resultado |
| fraccion | 2 | num, den, forma:'pizza'\|'barra', txt |
| ecuacion | pasos | pasos:[...], notas:[...] |
| figura | 2 | tipo:'triangulo'\|'cuadrado'\|'rectangulo'\|'circulo'\|'angulo', grados, etiquetas |
| grilla | 1 + resaltar | filas, cols, titulo, resaltar:[{fila, col, txt}] |
| geo | pasos | titulo, vista:[xmin,xmax,ymin,ymax], pasos:[{el:[...], txt}] — geometría paso a paso. Elementos: `{seg:[[x,y],[x,y]], dash, flechas, color}`, `{pol:[[x,y]...]}`, `{pt:[x,y], txt}`, `{txt:[x,y], s}`, `{ang:[x,y], a1, a2, r, txt, recto}` (grados), `{arco:[x,y], r, a1, a2}` (compás), `{marca:[[x,y],[x,y]], n}`. Usar en TODA lección de geometría: cada figura que se nombra, se dibuja |
| saltos | 1 + saltos | titulo, min, max, cada, inicio, saltos:[{a, txt}] — saltos con flecha sobre la recta (sumas y restas de enteros, múltiplos, multiplicar como suma repetida) |
| platillos | estados | titulo, estados:[{izq:[...], der:[...], txt}] — balanza con bolsitas (emoji) y pesas (texto), un estado por paso (ecuaciones) |
| criba | 2 + tachar | hasta, cols, tachar:[2,3,5,7], txt (criba de Eratóstenes: tacha múltiplos, brillan los primos) |
| arbol | 2 + ramas | numero, ramas:[[primo, cociente]...], resultado (árbol de factores primos) |
| libro | 1 + partes | titulo, libro:{titulo, autor, editorial, emoji}, partes:[{parte:'contratapa'\|'lomo'\|'tapa'\|'indice', txt}] — dibuja un libro y marca sus partes (paratexto) |
| parrafo | 1 + marcas | titulo, lineas:[...], marcas:[{linea, pos:'inicio'\|'fin'\|'sangria', txt}] — párrafo real con marcas (sangría, mayúscula, punto) |
| ficha | 1 + campos | titulo, campos:[[cab, valor]] — ficha bibliográfica que se completa |
| orden | 3 | titulo, items:[{txt, emoji}] en orden cronológico, relato:[índices en el orden en que se cuenta] — reordena tarjetas: así se cuenta → así pasó (flashback, in medias res) |
| corrige | 1 + cambios | titulo, cambios:[{antes, despues, motivo}] (máx 3) — tacha lo incorrecto y escribe lo correcto (revisión de textos) |
| experimento | 3 | titulo, variable, a:{cab, emojis, txt, res}, b:{…} — grupo control vs grupo con cambio: montajes, variable, resultados (Naturales) |
| medidor | 3 | titulo, tipo:'termometro'\|'regla'\|'probeta', min, max, valor, unidad, nota — instrumento dibujado con su lectura (Naturales) |
| celula | 1 + partes | titulo, tipo:'animal'\|'vegetal', partes:[{p:'membrana'\|'citoplasma'\|'nucleo'\|'mitocondria'\|'pared'\|'cloroplasto'\|'vacuola', txt}] — célula dibujada con sus partes marcadas (Naturales) |
| globo | 1 + marcas | titulo, marcas:[{tipo:'ecuador'\|'greenwich'\|'paralelo'\|'meridiano'\|'punto', lat, lon, txt}] — la Tierra con paralelos y meridianos (Sociales/Geografía) |
| orbita | 1 + posiciones | titulo, posiciones:[{ang, txt}] — el Sol y la Tierra en su órbita (estaciones) |
| partes | 1 + partes | emoji, titulo, partes:[{txt, x, y}] (x, y entre −1 y 1) |
| molecula | 3 | titulo, atomos:[{el, x, y}], enlaces:[[i, j, orden]], nombre |
| fuerzas | 1 + fuerzas | cuerpo, inclinado, fuerzas:[{txt, ang, largo, color}] |
| zoom | niveles | niveles:[{emoji, txt}] (2-5) |
| texto | 1 + marcas | oracion, marcas:[{desde, hasta, etiqueta, color}] (índices de palabras) |
| silabas | 3 | palabra, silabas, tonica, tipo |
| bloques | 1 + items | titulo, items:[{cab, txt}] (2-5) |
| dialogo | lineas | personas:[{nombre, emoji}×2], lineas:[{quien, txt, trad}] (máx 4) |
| vocab | items | items:[{palabra, emoji, trad, pron}] (2-6) |

Ejemplo completo: `lecciones/medio-mat1-m1-n1.json`. PDF: `python tools/medio/pdf/generar.py contenido/medio/<materia>/mision-N/mision-N.json` (o el proceso "PDF de las misiones del NIVEL MEDIO").


## Cuándo va una imagen

Si la explicación habla de **las partes de algo** (un libro, una célula, una planta, una máquina) o de **cómo está ubicado algo** (un plano, un túnel, un mapa), la escena tiene que mostrarlo con una plantilla visual (`libro`, `partes`, `mapa`, `geo`, `figura`, `mundo`) y no solo con texto. Lo mismo en el PDF: una figura cuando sin ella no se entiende.


**Formato simple (decidido):** en todas las materias, `mundo` solo con `fondo:'nada'`, sin zoom ni movimientos; para Naturales preferir `experimento`, `medidor`, `partes`, `ciclo`, `molecula`.

## Antes de subir una misión (controles automáticos, sin capturas)

1. `python3 tools/medio/clase/armar.py <slugs>`
2. `python3 tools/medio/clase/revisar_contenido.py <slugs> --mision contenido/<materia>/mision-N/mision-N.json` — meses, formato simple, fichas, opciones, años, pronunciación, escritura en Lengua.
3. `python3 tools/medio/clase/revisar_pantalla.py <slugs>` — textos que se salen o se pisan (solo los slugs nuevos: ~20 s por misión).
Si alguno marca algo, se corrige antes de subir.

## Dos versiones: voseo y español neutro

Cada clase y cada PDF existen en dos versiones, que arma la máquina sola:
- **Argentina** (voseo, voz de la materia): lo que se escribe.
- **Neutra** (tuteo latinoamericano, voz neutra de la materia): `tools/medio/neutro_medio.py` convierte el texto con un diccionario cerrado.

La ve el alumno según su **país** (`students.pais`): Argentina → voseo; otro país → neutro.
- Clases: `armar.py` arma `dist/<slug>.html` y `dist/<slug>.neutro.html`; `voz_edge.py` graba `voz/<slug>.json` y `voz/<slug>.neutro.json`.
- PDF: `tools/medio/pdf/generar.py` arma también el PDF neutro de cada lección (`content.r2_key_neutro` del paso PDF).
- Si `revisar_contenido.py` avisa "voseo sin pasar al diccionario neutro", hay que sumar la palabra a `MAPA` (si es voseo) o a `OK` (si no lo es) en `tools/medio/neutro_medio.py`.

### Misiones COMÚN, VARIANTE y ALTERNATIVA (para alumnos de otros países)

Cada misión tiene su etiqueta en `topics.version` (copia en `tools/versiones.json`); se ve en el panel de Contenidos.
- **Común**: se escribe una vez; la versión neutra sale sola (voseo → tuteo).
- **Variante**: en el mismo archivo, cada bloque que cambia lleva al lado su parte para extranjeros con la clave `"neutro"`, ya escrita en neutro:
  - clase: `{"t": "definicion", "palabra": "Mar argentino", "texto": "...", "voz": [...], "neutro": {"palabra": "Mar territorial", "texto": "...", "voz": [...]}}`
  - PDF: igual, en cualquier bloque (`"neutro": {"texto": ...}`). Actividades y examen: solo el enunciado (`"neutro": {"p": ...}`); las opciones tienen que servir para los dos (si no, la corrección no coincide).
  - La interfaz de la plataforma (botones, mensajes, consignas) se pasa sola a neutro para extranjeros con `js/neutro.js`, que se genera desde `tools/neutro.py --js`: al sumar palabras al diccionario, regenerarlo.
  - Una clase de una misión variante que es igual para todos lleva `"sin_variante": true` (decisión consciente).
- **Alternativa**: el extranjero hace otra misión en ese lugar.
  - El archivo de la misión trae `"alternativa": {...}` con la misión entera para extranjeros (niveles, act, examen, practica, examen_titulo, titulo, lecciones).
  - `cargar_mision` la carga sola en su par (la misión de la otra versión de la materia o una misión hermana solo para internacionales que crea en el momento).
  - Cada clase argentina lleva `"alternativa": "<slug de la clase para extranjeros>"`, y esa clase lleva `"alternativa_de": "<slug argentino>"`.

**Controles**: `revisar_contenido.py` avisa antes de subir y `cargar_mision` **no carga** una variante sin partes `"neutro"` ni una alternativa sin `"alternativa"`.

## Primeros años: 1.º, 2.º y 3.º del Nivel Medio (chicos que recién aprenden a leer)

Regla fija para estas materias (la lista está en `tools/medio/primeros_anios.py`; se aplica sola por el nombre de la materia, o con `"estilo": "primeros"`):

**Clase animada**
- Todos los textos de la pantalla y los subtítulos salen en **IMPRENTA MAYÚSCULA** (lo hace el motor; en el JSON se escribe normal, con minúsculas, para que la voz pronuncie bien).
- Subtítulos de a **2 palabras** (no de a 3) y voz más lenta (`+5 %` en vez de `+25 %`).
- Frases de **3 a 10 palabras**, palabras que usa un chico de 6 a 8 años. Nada de "TikTok": ritmo tranquilo, una idea por frase, repetir la idea clave.
- De **6 a 10 escenas** (3 a 4 minutos). Gancho con personaje o reto sencillo; preguntas de 2 o 3 opciones.
- Mucho dibujo y poca letra en pantalla: preferir `fichas`, `agrupar`, `balanza`, `comparar`, `clasificar`, `recta`, `grilla`, `partes`, `zoom`; textos de pantalla de 1 a 4 palabras.
- Números chicos y objetos que se puedan contar con emojis (🍎 🐶 ⭐ 🧸).

**PDF**
- Todo en **IMPRENTA MAYÚSCULA** y con letra 1,5 veces más grande (lo hace `tools/medio/pdf/render_leccion.py`; el contenido se escribe normal).
- Oraciones de **12 palabras como máximo**, en presente y en segunda persona ("contá", "uní", "pintá").
- **Un dibujo por sección como mínimo** (bloque `imagen` con `png_base64`, dibujado por script, como `contenido/medio/matematica-1/figuras.py`). Si no se entiende sin dibujo, va dibujo.
- Consignas de carpeta para hacer con dibujos: contar, rodear, unir, pintar, dibujar.
- Hasta 8 hojas de contenido (la letra grande ocupa más).

**Controles**: `revisar_contenido.py` marca frases largas, clases de más de 10 escenas y secciones del PDF sin dibujo.

## Etiquetas COMÚN, VARIANTE y ALTERNATIVA en el Medio

La etiqueta de cada misión está en la base (`topics.version`); copia en `tools/medio/versiones.json` (solo las que no son comunes). `revisar_contenido.py` avisa antes de subir y `cargar_mision_medio` vuelve a controlar: **no carga nada** si falta una parte.

- **Común**: se escribe una vez; la versión neutra sale sola.
- **Variante**: en el mismo archivo, cada bloque que cambia lleva su parte `"neutro"` (clase, PDF, y `"neutro": {"p": ...}` en actividades y examen). Una clase igual para todos lleva `"sin_variante": true`.
- **Alternativa**: el archivo de la misión trae `"alternativa": {niveles, act, examen, practica, examen_titulo, titulo, lecciones}`.
  - En el Medio el par suele estar en **otra materia** (por ejemplo "Ciencias Sociales 3" ↔ "Ciencias Sociales Argentina 3", unidas por `version_par`): la parte `"alternativa"` se carga en ese par y no se cambia ninguna marca. Si la misión no tiene par, se crea uno solo para alumnos de otros países.
  - PDF del par: lo arma y lo sube `generar.py` solo (todo en neutro).
  - Clase del par: otro archivo en `lecciones/` con `"alternativa_de": "<slug argentino>"` y, en vez de `step_id`, `"destino": {"subject_id": "<materia de la misión>", "tema": N, "nivel": K, "internacional": true}` (la máquina busca sola el paso de video del par). La clase argentina lleva `"alternativa": "<slug del par>"`.
- `"destino"` sirve también para cualquier clase (sin `"internacional"`): así no hace falta buscar ids a mano.
