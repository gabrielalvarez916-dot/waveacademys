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
