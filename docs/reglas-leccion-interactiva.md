# REGLAS FIJAS · Lección interactiva (valen para cualquier sesión y cualquier cuenta de Claude)

La lección interactiva reemplaza al PDF dentro del nivel: es donde el alumno APRENDE. No es un resumen ni la clase repetida.
Estas reglas no se relajan nunca: ni por cantidad, ni por apuro, ni porque "ya se hicieron muchas". La lección número 300 se escribe
con el mismo cuidado y el mismo largo que la primera. Si no hay tiempo o uso para hacerla bien, se hacen menos lecciones, NUNCA peores.
El control `node tools/interactiva/validar.js` las hace cumplir: si una lección no cumple, no se carga nada de esa misión.

## Dónde se escribe
En `mision-N.json`, en cada nivel: `niveles.N.leccion = { "temas": [ ... ] }`. Cada tema:
```json
{ "titulo": "Divisores comunes",
  "explicacion": [ {bloques}, ... ],
  "ejemplo":   {"motor": "explorador2", "p": {"modo": "mcd"}},
  "ejercicio": {"motor": "mcd_guiado", "p": {}} }
```
Bloques permitidos en la explicación: `definicion`, `parrafo`, `lista`, `importante`, `tabla`, `imagen`. **Prohibidos** `pasos`, `ejemplo` y `error`: el procedimiento y el caso los muestra el ejemplo vivo de al lado; no se explica dos veces.
`ejemplo` y `ejercicio` salen del BANCO DE LA LECCIÓN (`js/leccion-banco.js` + `js/leccion-banco2.js`, catálogo en `docs/banco-leccion.md`), que es otro banco, separado del de actividades: nunca se usan motores de actividades acá ni motores de la lección en actividades.

## Cómo es cada pantalla (modelo CIDEAD, obligatorio)
Una pantalla = una idea. Mitad izquierda: texto corto. Mitad derecha: el EJEMPLO VIVO grande, donde el alumno cambia los números y ve el procedimiento. Abajo, el botón del ejercicio (opcional).
1. **Qué es**: bloque `definicion` completo y preciso (15 palabras o más), con las palabras del nivel (1.º año: 12 años, no son bobos).
2. **Por qué es así / para qué sirve**: un `parrafo` que dé el sentido, no solo la regla.
3. **Lo clave**: una `lista` de 2 o 3 viñetas: reglas, casos especiales y el error típico en una línea.
4. **Entre 60 y 160 palabras** de texto. Si hace falta más, es otra pantalla con su propio ejemplo.
5. **Ejemplo vivo SIEMPRE** (`ejemplo` con motor del banco): visual, con poquito texto. No repite la explicación (por eso `pasoapaso` no va).
6. **Ejercicio SIEMPRE** (`ejercicio` con motor del banco, con "Otros números"): ninguna pantalla sin práctica.
7. Cada lección tiene botón **Imprimir** (sale solo): imprime el texto de cada pantalla y el Recordá, como el PDF.
- Lo de CONCEPTO (qué es una variable, qué es aleatorio) no es pantalla propia: se explica dentro de la pantalla práctica que corresponde.
- Si el banco no tiene el ejemplo que la pantalla necesita, se agrega al banco de la lección (se avisa) y se anota en `docs/banco-leccion.md`. No se fuerza uno que no corresponde ni se deja la pantalla sin ejemplo.

## Qué tiene que tener cada lección
- 3 pantallas o más: las ideas importantes de la clase, no un número fijo. No se rellena.
- Al final, "Recordá lo más importante".

## Primaria (Nivel Medio): mismo modelo, adaptado a la edad
Mismo banco de ejemplos y ejercicios (es compartido) y mismas reglas; cambia cuánto texto lleva cada pantalla. El control lo saca de la carpeta: `contenido/medio/<materia>-<grado>/`.
| | Secundaria | Primaria 4.º a 6.º | Primaria 1.º a 3.º |
|---|---|---|---|
| Palabras por pantalla | 60 a 160 | 40 a 110 | 12 a 60 |
| Definición | completa, 15+ palabras | clara, 10+ palabras | una frase corta, 6+ palabras |
| Párrafo de sentido | obligatorio | obligatorio | no; como mucho un párrafo o una lista corta |
| Pantallas mínimas | 3 | 3 | 2 |
| Tarjetas del Recordá | 4 a 8 | 3 a 6 | 2 a 4 |
- **1.º a 3.º: poco texto, todo visual.** Frases cortas, palabras simples, el ejemplo hace casi todo. Nada de vocabulario técnico sin explicar.
- **4.º a 6.º: más texto pero no formal.** Se explica con palabras cercanas, como le hablaría la maestra; no con el tono de secundaria.
- Ejemplo y ejercicio en todas las pantallas, adaptados al contenido y a la edad (números chicos en 1.º, sin bloques de texto en el ejemplo).
- Se escribe en `niveles.N.leccion` del `mision-N.json` de primaria; la máquina del Nivel Medio la controla y la carga (tabla `leccion_medio`).

## "Recordá lo más importante" (cierre, formato CIDEAD)
Va en `niveles.N.leccion.recuerda`: 4 a 8 tarjetas, una por concepto o procedimiento clave de la lección, en grilla de dos columnas.
```json
{ "concepto": "Los divisores de un número", "definicion": "son los números que lo dividen de forma exacta, con resto 0.",
  "formula": "a · d = b · c", "esquema": ["Dato: a → b", "Pregunta: c → x", "Se calcula x = c · b / a"],
  "ejemplo": "D(18) = {1, 2, 3, 6, 9, 18}" }
```
- `concepto` en negrita + `definicion` como oración completa (10 palabras o más). Nada de "Media: suma ÷ cantidad".
- `ejemplo` concreto y corto, siempre (números reales, no "por ejemplo un número").
- `formula` (opcional) para propiedades y fórmulas: va destacada en recuadro. `esquema` (opcional) para procedimientos: los pasos como esquema.

## Prohibido
- Copiar: no más del 25 % de la explicación puede repetir frases de 6 palabras del borrador o de la narración de la clase (el control lo mide).
- Bajar la calidad con la cantidad: cada pantalla cumple lo mismo que la primera (definición completa, párrafo con sentido, ejemplo vivo).
- Repetir en el texto lo que muestra el ejemplo (pasos, caso resuelto, error largo).
- Explicaciones de dos líneas, "como vimos en la clase", listas sin explicar, pantallas sin ejemplo vivo.
- Fechas o meses del calendario (los alumnos entran en cualquier momento). Contenido de otro nivel.
- Inventar contenido que no corresponde al tema o al mapa curricular.

## Ritmo
Se pueden hacer muchas seguidas, pero cada tanda se controla igual. Si el control rechaza, se corrige esa lección antes de seguir con la siguiente.
