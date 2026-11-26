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
Los bloques son los mismos del PDF: `parrafo`, `definicion`, `pasos` (items), `ejemplo` (titulo, texto, items), `tabla`, `imagen`, `importante`, más `error` (titulo = el error, texto = por qué está mal y cómo darse cuenta).
`ejemplo` y `ejercicio` salen del BANCO DE LA LECCIÓN (`js/leccion-banco.js`), que es otro banco, separado del de actividades: nunca se usan motores de actividades acá ni motores de la lección en actividades.

## Qué tiene que tener cada tema (obligatorio)
1. **Qué es**: definición clara y precisa (bloque `definicion`), con las palabras del nivel (1.º año: 12 años, no son bobos).
2. **Por qué es así / para qué sirve**: un `parrafo` que explique el sentido, no solo la regla.
3. **Cómo se hace**: si el tema es práctico, bloque `pasos` con 3 o más pasos concretos (en temas de concepto no va).
4. **Ejemplo resuelto propio**: bloque `ejemplo` con 3 o más pasos y el resultado (en temas de concepto, un caso concreto bien explicado). Distinto del de la clase animada y del PDF.
5. **Error típico**: bloque `error` con el error, por qué está mal y cómo detectarlo.
6. **Mínimo 170 palabras** de explicación por tema (sin contar títulos). Sin máximo: si el tema lo pide, más.

## Dónde va ejemplo y ejercicio (y dónde NO)
- Solo en temas PRÁCTICOS: operaciones, cálculos, descomposiciones, construcciones, procedimientos (lo que se HACE con pasos).
- Los temas de CONCEPTO (qué es una variable, qué es aleatorio, para qué sirve cada medida, clasificar ideas) van solo con la explicación: sin ejemplo vivo, sin ejercicio, sin práctica. No todo es interactivo.
- El control lo exige: un tema con ejemplo o ejercicio tiene que tener un bloque `pasos` en su explicación, y la práctica escrita a mano tiene que ser una cuenta (respuesta con `formula`).

## Qué tiene que tener cada lección
- Los temas son los importantes de la clase: los que hagan falta (2, 3, 5…), no un número fijo. No se rellena para llegar a 4.
- Mínimo 650 palabras de explicación en toda la lección.
- Al final, "Recordá lo más importante" (sale del `resumen` del borrador).
- En Matemática, cada tema con procedimiento lleva `ejemplo` y/o `ejercicio` del banco. Si el banco no tiene el motor que el tema necesita, se avisa (no se fuerza uno que no corresponde).

## Prohibido
- Copiar: no más del 25 % de la explicación puede repetir frases de 6 palabras del borrador o de la narración de la clase (el control lo mide).
- Acortar con el tiempo: cada lección nueva tiene que tener al menos el 90 % de las palabras promedio de las lecciones ya escritas de esa materia (el control lo mide). Si una sale más corta, se completa, no se justifica.
- Explicaciones de dos líneas, "como vimos en la clase", listas sin explicar, ejemplos sin resolver.
- Fechas o meses del calendario (los alumnos entran en cualquier momento). Contenido de otro nivel.
- Inventar contenido que no corresponde al tema o al mapa curricular.

## Ritmo
Se pueden hacer muchas seguidas, pero cada tanda se controla igual. Si el control rechaza, se corrige esa lección antes de seguir con la siguiente.
