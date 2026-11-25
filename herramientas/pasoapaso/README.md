# Generador de "Paso a paso" (Matemática I · Avanzado)

Genera los HTML de paso a paso con la misma paleta/controles/selector que `base_raiz.html`.

- `lib.js` helpers (fmt, gcd, lcm, fr, clamp, R_)
- `engine.js` motor común (selector, Otro ejercicio, Auto, flechas, puntitos)
- `assemble.js` une motor + spec y escribe `out/MisionNN_Avanzado_MatematicaI_A_o1_<slug>.html`
- `validate.js` abre el HTML en Chromium (playwright), prueba N ejercicios por tema + entradas raras y compara con `spec.truth()`
- `specs/` una spec por lección: `mision`, `slug`, `title`, `sub`, `inputs`, `modes[{id,label,def,left}]`, `norm`, `rand`, `truth`, `build`
- `ejemplos/` los 2 pilotos generados (M9 L1 fracciones, M16 L2 ecuaciones)

## Uso
    cd herramientas/pasoapaso
    mkdir -p out
    node assemble.js specs/<spec>.js
    node validate.js out/<archivo>.html specs/<spec>.js 40

`truth()` debe calcular el resultado por un camino distinto al de `build()`.
