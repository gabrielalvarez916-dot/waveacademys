# Archivo de Lengua (26/11/2026)
Lo que quedó fuera de lugar con el mapa nuevo (docs/lengua-misiones-de-genero.md). No se carga: está guardado por si sirve.
- `lengua-L-mision-K.json`: niveles, actividades y examen que salieron de cada misión, con el motivo.
- `generadores/`: los scripts viejos que armaban esos JSON. No se vuelven a correr (pisarían la mudanza); el JSON de cada misión es la fuente.
Lo que sí servía para otra misión está en la clave `"mudado"` del JSON de la misión destino.
