#!/usr/bin/env bash
# MÁQUINA DEL NIVEL MEDIO · arma y controla una misión antes de subirla.
# Uso: bash tools/medio/controlar.sh contenido/medio/matematica-1/mision-1
# Corre mision.py y clases.py de la carpeta, arma las clases y pasa los controles de contenido y de pantalla.
# clases.py tiene que imprimir una línea por clase que empiece con su slug.
set -e
DIR="${1%/}"; [ -d "$DIR" ] || { echo "No existe $DIR"; exit 1; }
python3 "$DIR/mision.py"
SLUGS=$(python3 "$DIR/clases.py" | awk '{print $1}' | tr '\n' ' ')
JSON=$(ls "$DIR"/mision-*.json | head -1)
python3 tools/medio/clase/armar.py $SLUGS
python3 tools/medio/clase/revisar_contenido.py $SLUGS --mision "$JSON"
python3 tools/medio/clase/revisar_pantalla.py $SLUGS
git checkout -q -- tools/medio/clase/dist 2>/dev/null; git clean -qf tools/medio/clase/dist  # el HTML final (con voz) lo arma GitHub: se deja como está en el repo
echo "LISTA PARA SUBIR: $JSON · clases: $SLUGS"
