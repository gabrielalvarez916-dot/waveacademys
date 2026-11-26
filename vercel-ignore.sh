#!/bin/bash
# Vercel corre esto antes de desplegar: sale 0 = NO desplegar (solo cambió contenido), sale 1 = desplegar.
# Los commits de clases, voces, misiones, PDF y herramientas no despliegan (no gastan el cupo diario).
B="${VERCEL_GIT_PREVIOUS_SHA:-HEAD^}"
git cat-file -e "$B^{commit}" 2>/dev/null || B="HEAD^"
git diff --quiet "$B" HEAD -- . ':(exclude)contenido' ':(exclude)tools' ':(exclude)docs' ':(exclude)supabase' ':(exclude).github' ':(exclude)actividades/clases' || exit 1
exit 0
