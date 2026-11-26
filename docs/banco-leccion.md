# Banco de la lección interactiva (Matemática) — catálogo
Solo para la lección interactiva (`js/leccion-banco.js` + `js/leccion-banco2.js`). Separado del banco de actividades: no se mezclan.
En la lección: `"ejemplo": {"motor": "<id>", "p": {...}}` (escena para explorar cambiando los números) y `"ejercicio": {"motor": "<id>", "p": {...}}` (botón del tema, con Comprobar y Otros números).

## Ejemplos (explorar)
| Área | Motor (`p`) |
|---|---|
| Divisibilidad | `explorador` (`modo`: multiplos, divisores, primo) · `explorador2` (`modo`: mcd, mcm) · `escalera_factores` |
| Números | `pasoapaso` (`u`: /actividades/pasoapaso/…html) · `binario_lamparas` · `sexagesimal` · `redondeo` · `notacion_cientifica` · `periodo` · `recta_explorar` · `signos` · `potencias_explorar` · `raiz_explorar` · `jerarquia` · `porcentaje_barra` (`modo`: parte, aumento, descuento) |
| Fracciones | `fraccion_barras` (`op`: suma, resta) · `fraccion_area` · `fraccion_cantidad` |
| Proporcionalidad | `proporcionalidad` (`modo`: directa, inversa) · `escala` · `velocidad` |
| Medidas | `escalera_unidades` (`magnitud`: longitud, capacidad, masa, superficie, volumen) |
| Geometría | `transportador` · `triangulo` · `poligono_angulos` · `area_figura` (`figura`: rectangulo, triangulo, paralelogramo, rombo, trapecio) · `volumen_cubitos` · `circulo` |
| Álgebra | `valor_numerico` · `terminos_semejantes` · `patron_figuras` · `balanza` · `monomio` · `distributiva` |
| Funciones | `plano` · `funcion_lineal` |
| Estadística y probabilidad | `frecuencias` · `medidas` · `urna` · `combinaciones_tabla` |

## Ejercicios (botón del tema)
| Área | Motor (`p`) |
|---|---|
| Divisibilidad | `cajas` (`modo`: multiplos, divisores, primos, divisible, fraccion1) · `mcd_guiado` · `mcd_mcm_problemas` |
| Números | `llevar` (`modo`: equivalentes, irreducibles, potencias, raices, sumas) · `ordenar` (`modo`: enteros, decimales, fracciones) · `recta` · `posicional` (`modo`: ubicar, decimal) · `columnas` (`op`: suma, resta, mixta) · `letras` (`modo`: pagare, dictado, fraccion) · `binario_conv` · `sexagesimal_conv` · `redondear` · `notacion` · `decimal_tipo` · `combinadas` · `porcentaje` (`modo`: parte, que, aumento, descuento) |
| Fracciones | `fraccion_operar` (`op`: suma, resta, producto, division) · `fraccion_cantidad_x` |
| Proporcionalidad | `proporcional` · `regla_de_tres` (`modo`: directa, inversa) · `regla_tres_compuesta` · `escala_x` · `velocidad_x` |
| Medidas y geometría | `convertir_unidades` (`magnitud`) · `angulo_tipo` · `angulo_falta` (`modo`: triangulo, cuadrilatero, complementario, suplementario) · `area_perimetro` (`que`: area, perimetro; `figura`) · `volumen` |
| Álgebra | `valor_numerico_x` · `reducir_terminos` · `patron_termino` · `ecuacion` (`modo`: simple, dos_miembros) · `ecuacion_denominadores` · `traducir` · `monomio_x` · `polinomio_operar` (`op`: suma, resta) · `distributiva_x` |
| Funciones | `coordenadas` · `funcion_tabla` |
| Estadística y probabilidad | `tabla_frecuencias` · `media_moda_mediana` (`que`: media, moda, mediana) · `barras_armar` · `probabilidad` · `combinaciones` |

Si un tema necesita un motor que no está, se crea en el banco (con su prueba automática) antes de escribir la lección: no se fuerza uno que no corresponde.

## Agregados (26/11/2026)
| Motor | Tipo | Para qué | `p` |
|---|---|---|---|
| `valor_posicional` | ejemplo | escribís un número y ves cada cifra en su lugar, cuánto vale y la descomposición; con `leer`, los períodos y cómo se lee | `{"modo":"valor"\|"leer"}` |
| `comparar_naturales` | ejemplo | dos números: cuenta cifras y marca la primera cifra distinta | — |
| `sexa_operar` | ejemplo | suma y resta de tiempos (o ángulos con `angulo`) con los canjes de a 60 a la vista | `{"modo":"angulo"}` opcional |
| `descomponer` | ejemplo | cada cifra se convierte en un bloque de color con su valor | `{"modo":"aditiva"\|"potencias"}` |
| `descomponer_x` | ejercicio | escribir el valor de cada cifra (o el exponente de cada potencia) | `{"modo":"potencias"}` opcional |
| `binario_pasar` | ejemplo | escalera de divisiones por 2 (a_binario) o valor de cada lugar (a_decimal) | `{"modo":"a_binario"\|"a_decimal"}` |
| `sexa_operar_x` | ejercicio | sumar o restar dos tiempos (o ángulos con `angulo`) | `{"modo":"angulo"}` opcional |

`pasoapaso` NO va como ejemplo de la lección: repite en texto la explicación. Queda para otros usos.
| `potencias10_x` | ejercicio | solo potencias de 10 (exponentes naturales) y ×÷ por 10, 100, 1.000 | — |
| `binario_lugares_x` | ejercicio | valores de los lugares en binario y qué números pueden ser binarios (sin pasar de sistema) | — |

Modos agregados: `binario_conv` `{"modo":"a_binario"|"a_decimal"|"ambos"}` · `sexagesimal_conv` `{"modo":"convertir"|"ambos"}` (convertir = sin sumar).
Para cargar actividades o examen cambiados en una misión YA cargada, el archivo lleva `"actualizar_preguntas": true` (si no, la máquina no las toca).

## Ejemplos PASO A PASO (26/11/2026)
TODOS los ejemplos del banco (45) muestran el procedimiento de a un paso: helper `pasoAPaso(v, P)` en `js/leccion-banco2.js` (`P = [{vis, txt}]`, "Siguiente paso ▶", una línea por paso) y marca `pasos: true`. En `escena()`, `dibujar` puede devolver la lista de pasos. Un ejemplo NUEVO se hace igual; el control no deja usar en una lección un ejemplo sin `pasos: true`. (`pasoapaso`, el de texto largo, no va en lecciones.)

## Naturales y potencias (Matemática I, Misiones 2 y 3)
| Motor | Tipo | `modo` |
|---|---|---|
| `naturales` | ejemplo paso a paso | asociativa, inversa, descomposicion, compensacion, multiplicar, distributiva (`op`: resta), mental, division, relacion, falta, redondear, estimar, pasos |
| `naturales_x` | ejercicio | asociativa, inversa, descomposicion, compensacion, multiplicar, distributiva (`op`: resta), mental, division, relacion, redondear, estimar, pasos |
| `potencias_n` | ejemplo paso a paso (solo naturales) | potencia, cuadrado_cubo, crecen, producto, cociente, potencia_potencia, distributiva, no_suma, raiz_cubica, raiz_grande, lado_area, arista_volumen, perfectos |
| `potencias_n_x` | ejercicio | potencia, base_exp, cuadrado_cubo, producto, cociente, potencia_potencia, distributiva, no_suma, raiz_cuadrada, raiz_cubica, raiz_grande, estimar_raiz, lado_area, arista_volumen, perfectos |

## Combinadas, calculadora y divisibilidad (Matemática I, Misiones 4 y 5)
| Motor | Tipo | `modo` |
|---|---|---|
| `jerarquia` / `combinadas` | ejemplo / ejercicio | basica, izq, terminos, parentesis, corchetes, enunciado, potencias, raiz (sin modo: mezcla, no usar en lecciones) |
| `calculadora` / `calculadora_x` | ejemplo / ejercicio | comun, estimar, tipeo |
| `divis` | ejemplo | patron, suma, multiplo, contraejemplo, reparto, cual, pistas |
| `divis_x` | ejercicio | multiplo_n, repite, cuantos_div, suma, multiplo, contraejemplo, reparto, cual, pistas |
En la práctica, un campo puede llevar `acepta: function (x) {…}` cuando hay varias respuestas válidas.

## Criterios y factorización (Matemática I, Misiones 6 y 7)
| Motor | Tipo | `modo` |
|---|---|---|
| `criterios` / `criterios_x` | ejemplo / ejercicio | 2_5_10, 3_9, 4_8, 6, 11, combinar |
| `factores` | ejemplo | criba, esprimo, divisores, mcd_desc, mcm_desc, producto, tres |
| `factores_x` | ejercicio | esprimo, desc, cuantos, mcd, mcm, coprimos, producto, tres |

### Fracciones (Matemática I · Misiones 8 y 9)
- `fracciones` (ejemplo, paso a paso) y `fracciones_x` (ejercicio, `modo` obligatorio). Modos: parte, cociente, tipos (propias/impropias/mixtos), equivalentes, irreducible, cruzados, recta, entre (densidad), comparar, referentes, mixtos (suma), inverso, division (cuántas veces entra), combinadas, potencia.
## Primer grado (Nivel Medio · Matemática 1, Misiones 1 y 2) — 26/11/2026
Todo en imprenta mayúscula, con dibujos grandes y números chicos.
| Motor | Tipo | `modo` |
|---|---|---|
| `primeros` | ejemplo paso a paso | contar (`max`), cantidad (`max`), mas_menos (`igual`), uno_a_uno (`igual`), igualar (`op`: agregar, quitar), tren (`desde`, `hasta`), decena (`ini`), leer (`forma`: escribir), anterior_siguiente, mayor_menor |
| `primeros_x` | ejercicio | contar (`min`, `max`), grupo, mas_menos, igual, parejas, alcanza, agregar, quitar, falta (`desde`, `hasta`), decena, leer, escribir, anterior_siguiente, mayor_menor |

### Decimales y enteros (Matemática I · Misiones 10 y 11)
- `decimales` / `decimales_x` (`modo` obligatorio): frac_dec, dec_frac, comparar, cual (¿exacto o periódico?), puro_frac, suma, resta, producto, division, estimar.
- `enteros` / `enteros_x` (`modo` obligatorio): situacion, opuesto, distancia, comparar, intervalo, absoluto; `enteros_x` además abs_opuesto.
- Misiones 12 y 13: `enteros` / `enteros_x` suman modos suma, resta, suprimir, division, combinadas, cuadrado (−3² y (−3)²), raiz; `enteros_x` además producto y potencia.
- Misiones 14 y 15: `razones` / `razones_x` (razon, proporcion, fundamental, desconocido) y `algebra` / `algebra_x` (equivalentes, un_valor, recursiva). `modo` obligatorio.

## Primer grado hasta 100 (Nivel Medio · Matemática 1, Misiones 3 y 4) — 26/11/2026
Cuadro desde el 0, de a 10 por fila (los redondos quedan en el margen izquierdo).
| Motor | Tipo | `modo` (y `p`) |
|---|---|---|
| `primeros` | ejemplo paso a paso | cuadro (`que`: contar, fila, columna, bajar; `hasta`: 30, 50, 100) · saltos (`de`: 2, 5, 10) · anterior_siguiente y tren ahora aceptan `min`/`max` y `desde`/`hasta` hasta 100 |
| `primeros_x` | ejercicio | cuadro (`que`: falta, fila, columna, bajar; `hasta`) · saltos (`de`) · redondo (`max`: después de un 9) · redondos (nombre de los redondos) · anterior_siguiente con `min`/`max` |
| `primeros` / `primeros_x` (Misiones 5 y 6) | ejemplo / ejercicio | comparar2 (hasta 99, decenas primero) · ordenar3 (`orden`: asc, desc) · recta100 (`que`: ubicar o saltar con `dir`: adelante, atras) · decenas (`que`: contar, escribir, desarmar; ejercicio: contar con `max`, cuantas, armar, desarmar) |
| `primeros` / `primeros_x` (Misiones 7 y 8) | ejemplo / ejercicio | dinero (`que`: contar, pagar, falta, caro; sin palabras de Argentina) · sumar (`que`: juntar, agregar, palitos, cuenta) |
| `primeros` / `primeros_x` (Misiones 9 y 10) | ejemplo / ejercicio | restar (`que`: sacar, atras, comparar, cuenta) · diez (`que`: cuadro, falta, parejas, dados) |
| `primeros` / `primeros_x` (Misiones 11 y 12) | ejemplo / ejercicio | dobles (`que`: espejo, iguales, casi, tabla) · decenas_op (`que`: sumar, restar, atras10; ejercicio también contar10) |
| `primeros` / `primeros_x` (Misiones 13 y 14) | ejemplo / ejercicio | problema (`tipo`: juntar, agregar, avanzar, completar, quitar, comparar, falta_resta; ejercicio también mezcla y operacion = ¿suma o resta?) |
| `primeros` / `primeros_x` (Misión 15) | ejemplo / ejercicio | calcu (`que`: partes, teclas con `op`: suma o resta, controlar, uno_diez con `op`: mas1, mas10, menos10) |
| `primeros` / `primeros_x` (Matemática 2, Misiones 1 y 2) | ejemplo / ejercicio | centenas (`que`: contar, escribir; ejercicio también leer; `min`/`max` de cajas) · serie (`de`: 1, 10, 100; `dir`: sube, baja, mezcla; `desde`/`hasta`) |
| `primeros` / `primeros_x` (Matemática 2, Misiones 3 y 4) | ejemplo / ejercicio | valor (ejercicio también `que`: desarmar) · comparar3 · orden3 (`orden`: desc) · recta1000 (ejercicio también `que`: entre) · redondos3 (ejercicio) |
| `primeros` / `primeros_x` (Matemática 2, Misiones 5 y 6) | ejemplo / ejercicio | cambia (`op`: 1, 10, 100) · dinero2 (`que`: contar, vuelto, sumar, caro; billetes de $50 a $500, sin la palabra vuelto) |
| `primeros` / `primeros_x` (Matemática 2, Misiones 7 y 8) | ejemplo / ejercicio | mental (`que`: chica con `esc` 10 o 100, falta100, desarmar, truco; `op`: suma o resta) |
| `primeros` / `primeros_x` (Matemática 2, Misiones 9 y 10) | ejemplo / ejercicio | columna (`op`: suma o resta; `lleva`: true para me llevo 1 / canje; ejercicio también `que`: estimar, control) |
