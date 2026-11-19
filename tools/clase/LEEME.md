# Clases animadas (videos de las misiones) — costo $0

Convierte cada lección que ya está escrita (`secciones`, definiciones, tablas, ejemplos, resumen…) en una clase animada tipo video, con voz y subtítulos palabra por palabra. No usa ninguna IA para escribir: sale del contenido que ya existe.

1. `node tools/clase/convertir.mjs nivel.json clase.json "Título"` → arma las escenas y la narración.
2. (opcional) `ELEVEN_KEY=xxx ELEVEN_VOZ=id node tools/clase/voz.mjs clase.json audio/` → voz ElevenLabs. Guarda lo generado y no lo repite; si se acaba la cuota corta prolijo.
3. `node tools/clase/construir.mjs clase.json salida.html` → un solo archivo HTML listo.

Sin audio de ElevenLabs, la clase usa la voz gratis del celular/compu del alumno. Las escenas que ya tienen audio usan ElevenLabs.
Al terminar manda `postMessage({ tipo: 'wave-clase-fin', puntaje: 100 })`.

Ejemplo: `actividades/clases/mat1-m1-n1.html` (Matemática I · Misión 1 · Nivel 1).
