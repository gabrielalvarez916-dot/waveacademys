# Errores que ya pasaron y no pueden volver a pasar (leer antes de armar contenido)
| Error | Qué lo evita |
|---|---|
| Pantalla sin ejemplo o sin práctica | `validar.js` lo rechaza |
| Ejemplo con texto largo que repite la explicación | `pasoapaso` prohibido; bloques `pasos`/`ejemplo`/`error` prohibidos en el texto |
| Ejemplo que muestra el resultado de golpe | solo ejemplos `pasos: true` (Siguiente paso) |
| Práctica que pide algo de otra pantalla o de otro año | regla 6 + `modo` obligatorio en motores que mezclan contenidos; leer qué pide el motor antes de usarlo |
| Menos de 4 actividades por lección o de 4 generales | `control_calidad.py` lo rechaza |
| Actividades cambiadas que no llegan a la base (misión ya cargada) | `"actualizar_preguntas": true` + verificar en la base, no en el workflow |
| Decir "está listo" sin verlo | verificar en la base y, si hay pantalla nueva, mirarla con las herramientas de accesibilidad cargadas |
| Botón de dictar enorme en cada casilla | micrófono chico adentro de la casilla en la lección (`apoyos.js`) |

## 26/11/2026 — El control de calidad salteaba misiones "existentes"
Las misiones de `tools/calidad_existentes.txt` no pasaban el control de actividades, examen ni carpeta, y se dijo que estaban controladas. Desde ahora `control_calidad.py` revisa SIEMPRE lección, actividades, examen y carpeta en todas las misiones. Lo único que se saltea en las existentes es el control de las clases animadas (no se tocan). Nunca decir "pasó el control" si el control dijo "no se revisa".
