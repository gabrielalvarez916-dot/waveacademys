# Lección interactiva (reemplaza al PDF dentro del nivel)

La máquina la arma sola desde el borrador de cada nivel (`niveles.N` de `mision-N.json`):
- **Cada sección** (`secciones[i]`) es un tema: a la izquierda la explicación (sus `bloques`), a la derecha un **ejemplo paso a paso** con botón «Otro ejemplo», y abajo el botón **«Practicá este tema»** (ejercicio nuevo cada vez, se corrige en el momento, no lleva nota).
- **Al final**, el resumen: `resumen`, `tip`, `ojo` y `glosario` del borrador.
- El PDF se sigue armando igual y queda en el círculo **Recursos (opcional)** de la misión. La entrega de la carpeta sigue obligatoria.

## Lo único que hay que escribir: `practica` en cada sección (obligatoria)

Se escribe con el borrador y la clase animada del nivel a la vista: mismo tema, mismo nivel, ejemplos propios (no copiar los del PDF).

**Con números al azar** (Matemática y todo lo que tenga cuentas):
```json
"practica": {
  "vars": {"t": {"valores": [20, 25, 50]}, "a": {"min": 2, "max": 20}},
  "calculadas": {"p": "a*100/t"},
  "reglas": ["a*100%t==0"],
  "enunciado": "En una encuesta a {t} alumnos, {a} eligieron fútbol. ¿Qué porcentaje eligió fútbol?",
  "pasos": ["El total de datos es {t}.", "{a} × 100 ÷ {t} = {p}. Eligió fútbol el {p}%."],
  "respuesta": {"formula": "p"},
  "unidad": "%"
}
```
- `vars`: `min`/`max` (y `paso`) o `valores` (también palabras: nombres, objetos, contextos). `calculadas` y `reglas` como en las cuentas con números al azar (docs/tipos-de-pregunta.md). Funciones: abs, min, max, floor, ceil, round, sqrt, mcd.
- `pasos`: 2 a 8, cortos, en orden. **El último paso tiene que llegar al resultado** (el control lo verifica en 60 sorteos).
- `respuesta`: `{"formula": ".."}` (acepta fracción o decimal con coma; `tolerancia` opcional), `{"acepta": ["..", ".."]}` (texto) o `{"opciones": [..], "correcta": ".."}`.

**Sin números al azar** (Lengua, Sociales, Naturales, conceptos): 3 o más ejemplos que se van rotando.
```json
"practica": { "variantes": [
  {"enunciado": "..", "pasos": ["..", ".."], "respuesta": {"opciones": ["..", ".."], "correcta": ".."}},
  {"enunciado": "..", "pasos": ["..", ".."], "respuesta": {"acepta": [".."]}},
  {"enunciado": "..", "pasos": ["..", ".."], "respuesta": {"formula": "37"}} ] }
```

Misiones VARIANTE: dentro de `practica` (o de cada variante) puede ir `"neutro": {..}` con lo que cambia para alumnos de otros países, como en el resto del borrador.

## Qué hace la máquina (`.github/workflows/mision-avanzado.yml`)
1. `node tools/interactiva/validar.js` — control de las prácticas (si falla, no se carga nada).
2. Control de calidad general y carga completa **solo si la misión cambió en algo más que las prácticas** (`tools/interactiva/solo_practicas.py`).
3. `python tools/interactiva/cargar.py` — carga o actualiza las prácticas en los borradores (función `cargar_practicas`; sirve para misiones ya cargadas).
4. PDF y publicación como siempre.

En la plataforma: `lecciones_con_interactiva(materia)` dice qué niveles ya la tienen (ahí el paso PDF pasa a ser «Lección») y `leccion_interactiva(lección)` entrega el borrador al visor (`js/leccion-interactiva.js`).
