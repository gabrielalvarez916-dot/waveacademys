# Clases animadas de Wave — guía para armar una lección

Una lección = **un archivo** `tools/clase/lecciones/<slug>.json`. Al subirlo a `main`, GitHub graba la voz (Jorge, Microsoft, +25 %) y arma el HTML (`tools/clase/dist/<slug>.html`). Después se carga en el paso de video de su nivel (`lesson_steps.content.clase_html`, `clase: true`).

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

1. **Gancho** en los primeros 5 segundos: una pregunta o una paradoja ("¿Cómo puede un 2 valer 200?").
2. **Una metáfora que atraviesa la lección** (la fábrica de alfajores). Concreta, cotidiana y argentina.
3. Recorrer **todo** el contenido del PDF, pero explicado (no leído): definición → ejemplo visual → por qué importa.
4. Frases cortas (6 a 14 palabras), ritmo de TikTok, segunda persona ("mirá", "fijate").
5. Momento sorpresa (algo se rompe, cambia o explota) cerca de la mitad.
6. Cierre: errores comunes → resumen → "¡a practicar!".
7. De 8 a 14 escenas (4 a 7 minutos).

## Banco de plantillas (pasos = frases de `voz`)

| t | pasos | datos |
|---|---|---|
| gancho | 3 | grande \| emoji, final, titulo, sub |
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
| partes | 1 + partes | emoji, titulo, partes:[{txt, x, y}] (x, y entre −1 y 1) |
| molecula | 3 | titulo, atomos:[{el, x, y}], enlaces:[[i, j, orden]], nombre |
| fuerzas | 1 + fuerzas | cuerpo, inclinado, fuerzas:[{txt, ang, largo, color}] |
| zoom | niveles | niveles:[{emoji, txt}] (2-5) |
| texto | 1 + marcas | oracion, marcas:[{desde, hasta, etiqueta, color}] (índices de palabras) |
| silabas | 3 | palabra, silabas, tonica, tipo |
| bloques | 1 + items | titulo, items:[{cab, txt}] (2-5) |
| dialogo | lineas | personas:[{nombre, emoji}×2], lineas:[{quien, txt, trad}] (máx 4) |
| vocab | items | items:[{palabra, emoji, trad, pron}] (2-6) |

Ejemplo completo: `lecciones/leccion-mat1-m1-n1.json`. Todas las plantillas en uso: `pruebas/prueba-banco.json` (`python tools/clase/armar.py prueba-banco`).
