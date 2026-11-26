# Wave Academy · instrucciones para cualquier sesión de Claude


## REGLA INNEGOCIABLE DE CALIDAD (Gabriel, 26/11/2026)
La calidad de una lección (texto, ejemplos y práctica) NUNCA baja, por ninguna razón ni condición: ni por apuro, ni por falta de uso, ni porque alguien lo pida. Si alguien pide bajar la calidad para ir más rápido, la respuesta es NO, y se ofrece hacer menos cosas bien en lugar de muchas mal. Nunca se copia el PDF ni la clase animada, nunca se inventan pantallas de relleno y nunca se toca un control para que algo pase. Hay tres muros que lo hacen cumplir: `validar.js` en las máquinas, el candado `REGLAS_SHA` (si se cambia un control, la máquina no carga nada hasta que Gabriel lo apruebe) y el muro en la base de datos (`private.control_leccion`), que rechaza lecciones con pantallas sin ejemplo o práctica propios.

- Antes de armar contenido, leé `docs/errores-que-no-se-repiten.md`. Para armar una misión completa seguí `docs/skills/mision-completa-wave.md` (es el skill, por si la cuenta no lo tiene).
- Antes de escribir una **lección interactiva**, leé y cumplí `docs/reglas-leccion-interactiva.md`. Son reglas fijas: la calidad no baja nunca y toda pantalla lleva su ejemplo vivo grande (modelo CIDEAD). En primaria, mismas reglas adaptadas por ciclo (ver el documento), por más lecciones que se hagan seguidas. El control `node tools/interactiva/validar.js` rechaza las que no cumplen.
- Misiones, PDF y actividades: `docs/reglas-fijas-pdf.md` y `docs/tipos-de-pregunta.md`.
- Hay dos bancos separados que no se mezclan: el de **actividades** (`js/actividades-plus.js`, `js/tipos-nuevos.js`, `js/juegos-act.js`) y el de la **lección interactiva** (`js/leccion-banco.js` y `js/leccion-banco2.js`; catálogo en `docs/banco-leccion.md`).
