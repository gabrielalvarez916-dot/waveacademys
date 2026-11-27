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
| `primeros` / `primeros_x` (Matemática 2, Misiones 11 y 12) | ejemplo / ejercicio | problema ahora acepta `esc` (números grandes: 50 → de 100 a 450) y `tipo`: dospasos · prop (`que`: conmuta, amigos, dobles, familia) |
| `primeros` / `primeros_x` (Matemática 2, Misiones 13 y 14) | ejemplo / ejercicio | mult (`que`: grupos, signo, arreglo, girar; ejercicio también filas) |
| `primeros` / `primeros_x` (Matemática 2, Misión 15) | ejemplo / ejercicio | por10 (`de`: 10 o 100; `que`: cifras; ejercicio también problema, cuantos0) |
- `primeros` / `primeros_x` modo `miles`: números de 4 cifras con camiones de 1.000, cajas de 100, paquetes de 10 y sueltos (que: contar | escribir | leer). `serie` acepta pasos de 1.000 y muestra el punto de miles. (Mat3 m1)
- `primeros` / `primeros_x` modos de 4 cifras (Mat3 m2 y m3): `comparar4`, `orden4` (orden: desc), `vecinos4` (anterior y siguiente), `recta10000` (que: entre), `valor4` (que: desarmar | juntar), `armar4` (tarjetas; que: menor | mezcla), `cambia4` (op: 1 | 10 | 100 | 1000).
- Misiones 16 y 17: `ecuaciones` (verificar, inversa, dos_miembros, problema) / `ecuaciones_x` (verificar, problema) y `geometria` (relaciones, rectas, bisectriz, mediatriz, copiar) / `geometria_x` (relaciones, rectas, bisectriz, mediatriz, triangulo). `modo` obligatorio.
- Misiones 18 y 19: `figuras` / `figuras_x` (exterior, isosceles, ecuacion, paralelogramo, cuadrilateros, diagonales, suma360; `figuras_x` además clasificar) y `medida` / `medida_x` (perimetro, misma_unidad, circulo, compuesta, capacidad). `modo` obligatorio.

### Matemática I M20 y Matemática II (todas) · `modo` obligatorio
- `datos` / `datos_x`: circular, lineas, media_moda (sin mediana), muestral, azar.
- `racionales` / `racionales_x`: recta_neg, punto_medio, mixto (periódico mixto → fracción), mezcla (fracción + decimal), pot_neg, exp_neg, raiz_frac.
- `porcentajes` / `porcentajes_x`: factor, sucesivos, interes, variacion, compuesta (regla de tres compuesta).
- `ecuaciones2` / `ecuaciones2_x`: parentesis, denominadores, casos (una / ninguna / infinitas), despejar; `ecuaciones2_x` además densidad.
- `funciones` / `funciones_x`: es_funcion, grafico (creciente/decreciente, ordenada al origen).
- `geometria2` / `geometria2_x`: paralelas (transversal), pitagoras, congruencia (LLL, LAL, ALA), cuerpos (caras, aristas, vértices, Euler).

### Lengua (Lengua y Literatura I y II) · datos escritos en sesión en `p.items`
Marcas en textos: `{{frase|explicación}}` (ejemplos) y `[[frase|etiqueta]]` / `[[ok/mal1/mal2]]` / `[[palabra]]` (ejercicios). Prueba automática: `tools/interactiva/prueba-lengua.html` (abre cada motor con datos de muestra y verifica que la respuesta correcta pase).
- Ejemplos paso a paso: `marcar`, `versiones` (narrador, registro, variedades), `transformar` (reescritura: cohesión, registro, mostrar, expandir, unir, directo→indirecto), `palabra` (tilde), `vocales` (diptongo/hiato), `oracion` (análisis con bloques: S/P, núcleos, MD/MI/aposición, tácito, compuesta), `conjugador` (genera verbos regulares; perfecto vs imperfecto), `clases` (clases de palabras por color), `formacion` (prefijo+raíz+sufijo), `capas` (idea principal + prueba del borrado, estructura, causa-efecto, hecho/opinión, preguntas de la noticia), `esquema` (cuadro sinóptico o cuadro comparativo), `linea_tiempo` (orden del relato vs cronológico), `recursos` (metáfora, comparación, personificación, hipérbole, ironía), `verso` (versos, estrofas, rima), `personaje` (rasgos al inicio y al final), `conectores`, `formato` (carta, mail, formulario, reseña…), `revision` (lista de revisión sobre un borrador), `citar` (cita, paráfrasis y referencia).
- Ejercicios: `marcar_x` (tocar), `etiquetar_x`, `analizar_x` (etiquetas sintácticas a bloques), `completar_x` (huecos con opciones), `completar_banco_x` (fichas a huecos), `conjugar_x` (genera casos), `tilde_x`, `silabas_x`, `puntuar_x`, `ordenar_x`, `clasificar_x`, `elegir_x`, `unir_x`, `armar_x`, `borrar_x` (prueba del borrado), `transformar_x` (reescribir con control de lo pedido), `escribir_x` (producción con lista que se tilda sola), `relacion_x` (relación + conector), `dictado_x` (lee en voz alta y marca errores).
- `primeros` / `primeros_x` (Mat3 m4 y m5): `dinero4` (que: contar | formar | caro | vuelto; vuelto con `pago: 10000`) y `sumar4` (que: redondos | descomp | estimar | dobles | falta1000).
- `primeros` / `primeros_x` (Mat3 m6 y m7): `columna` acepta `cifras: 4` (cuentas de 4 cifras en columnas, con lleva, op resta, que estimar/control) y nuevo `problema4` (tipo: distancia | inicio (dir: quitar | mezcla) | pasos | inventar).
- `primeros` / `primeros_x` (Mat3 m8 y m9): `calcu4` (que: estimar | control | rota | problema; calculadora con números de 4 cifras) y `serie_prop` (que: serie | tabla | problema; tablas de una cantidad que se repite).
- `primeros` / `primeros_x` (Mat3 m10 y m11): `pitagorica` (que: armar | regular | tabla con min/max; ejercicio `solo`: lista de tablas) y `por10m` (de: 10 | 100 | 1000; que: redondos | problema).
- `primeros` / `primeros_x` (Mat3 m12 y m13): `mult1` (que: descomp | columna | lleva | estimar; multiplicar por una cifra) y `combina` (que: arreglo | grande | prendas | problema; organizaciones rectangulares y combinaciones).
- `primeros` / `primeros_x` (Mat3 m14 y m15): `divide3` (que: grande | grupos | resto | restando | tabla | comprobar | problema; repartos, grupos y división con resto).

## Naturales (todas las materias del área, secundaria y Nivel Medio) · `js/leccion-banco-nat.js` (27/11/2026)
Regla del área: cada ejemplo tiene su propio formato visual (no se repite el mismo molde). Todos paso a paso. Prueba: `python3 tools/interactiva/prueba-nat.py` (casos en `tools/interactiva/casos-nat.json`).
| Ejemplo | Ejercicio | Qué muestra | `p` |
|---|---|---|---|
| `partes` | `partes_x` (tocar el número) | dibujo con rótulos de a uno | `figura` o `figuras`: celula_animal, celula_vegetal, flor, planta, ojo, corazon, tierra, neurona, bacteria, virus, suelo · o `items` propios con emoji |
| `recorrido` | `recorrido_x` (ordenar) | una ficha viaja por estaciones y se transforma | `recorrido(s)`: digestion, sangre, aire, savia, reflejo, orina |
| `ciclo` | `ciclo_x` (etapa que falta) | rueda de etapas | `ciclo(s)`: agua, carbono, nitrogeno, rana, mariposa, celular, rocas, planta |
| `red_trofica` | `red_trofica_x` (`que`: rol, energia, quitar) | niveles, flechas, regla del 10 %, quitar una especie | `red`: pastizal, laguna, monte |
| `clave` | `clave_x` | clave dicotómica en escalera | `clave(s)`: vertebrados, invertebrados, plantas, reinos |
| `plato` | `plato_x` (grupos de alimentos) | plato recomendado contra una comida | `items` opcional |
| `osmosis` | `osmosis_x` | membrana, agua y célula que se hincha o arruga | `celula` |
| `enzima` | `enzima_x` | llave y cerradura, curva de actividad | — |
| `punnett` | `punnett_x` | gametos, cuadro y proporciones | `rasgo`: arveja, flor, grupo, daltonismo |
| `adn` | `adn_x` (`que`: complementaria, arn, aminoacido) | replicación, transcripción, traducción, mutación | `secuencia`, `modo` |
| `mitosis` | `mitosis_x` (`que`: orden, cuenta) | cromosomas fase por fase | `modo`: mitosis, meiosis |
| `tiempo_geo` | `tiempo_geo_x` (ordenar) | historia de la Tierra en un día o en una cancha | `modo`: reloj, cancha |
| `poblacion` | `poblacion_x` | curvas J y S | `modelo` |
| `epidemia` | `epidemia_x` | cadena de contagios, R₀ y vacunación | — |
Herramientas comunes en `H.nat` (dibujo SVG, elegir, ordenar, tocar) para los archivos que siguen: `leccion-banco-nat2.js` (materia y química) y `leccion-banco-nat3.js` (física, Tierra y espacio).

### Naturales parte 2 · `js/leccion-banco-nat2.js`: materia, química y laboratorio
| Ejemplo | Ejercicio | Qué muestra |
|---|---|---|
| `particulas` | `particulas_x` | modelo de partículas, estados y cambios de estado (agua, alcohol, hierro, nitrógeno, mercurio) |
| `mezclas` | `mezclas_x` | separar mezclas con el aparato dibujado (filtración, evaporación, imantación, decantación, tamización) |
| `densidad` | `densidad_x` | d = m/V, el objeto flota o se hunde en distintos líquidos |
| `atomo` | `atomo_x` | modelo de Bohr de Z = 1 a 20, iones (`p.z`) |
| `tabla_periodica` | `tabla_periodica_x` (tocar) | período, grupo, valencia, metales y tendencias |
| `enlace` | `enlace_x` (clasificar) | iónico y covalente con puntos de Lewis (NaCl, H₂O, O₂, CO₂, CH₄) |
| `ecuacion_quimica` | `ecuacion_quimica_x` | balancear contando átomos |
| `ph` | `ph_x` | escala de pH con sustancias de la casa |
| `gases` | `gases_x` | pistón: Boyle, Charles y Gay-Lussac (`p.ley`) |
| `carbono` | `carbono_x` | cadenas de carbono, hidrógenos, fórmula y nombre (alcanos, alquenos, alquinos, alcoholes, ácidos) |
| `radiactividad` | `radiactividad_x` | semivida con grilla de átomos |
| `instrumento` | `instrumento_x` | leer termómetro, probeta, regla y balanza; apreciación (`p.instrumentos`) |
| `tamanos` | `tamanos_x` (ordenar) | escala de potencias de 10, de una persona a un átomo |
| `grafico` | `grafico_x` | gráfico que se dibuja punto por punto; `p.items` propios {nombre, x, y, series, marcas, cierre} |
| `experimento` | `experimento_x` | pregunta, hipótesis, variables, montaje, resultados, conclusión; `p.items` propios |

### Naturales parte 3 · `js/leccion-banco-nat3.js`: física, Tierra y espacio
| Ejemplo | Ejercicio | Qué muestra |
|---|---|---|
| `circuito` | `circuito_x` | ley de Ohm, serie y paralelo, lámparas que brillan, qué pasa si se quita una (`p.modo`) |
| `movimiento` | `movimiento_x` | MRU, MRUV, caída libre y tiro vertical: el móvil y los gráficos x-t y v-t (`p.modo`) |
| `fuerzas` | `fuerzas_x` | diagrama de cuerpo libre en el piso o en un plano inclinado, leyes de Newton |
| `vectores` | `vectores_x` | suma gráfica, resultante y componentes |
| `palanca` | `palanca_x` | ley de la palanca y los tres géneros (`p.genero`) |
| `energia` | `energia_x` | montaña rusa o péndulo con barras de energía (`p.escena`) |
| `onda` | `onda_x` | amplitud, longitud de onda, frecuencia, v = λ·f, sonido |
| `luz` | `luz_x` | sombras, reflexión y refracción (`p.modo`) |
| `calor` | `calor_x` | equilibrio térmico y Q = m·c·ΔT |
| `fluidos` | `fluidos_x` | presión hidrostática y empuje (`p.modo`: presion, empuje) |
| `iman` | `iman_x` | polos, campo magnético, brújula y electroimán (`p.modo`) |
| `tierra_luna` | `tierra_luna_x` | día y noche, estaciones y fases de la Luna (`p.modo`: dia, estaciones, fases) |
| `sistema_solar` | `sistema_solar_x` (ordenar) | distancias y tamaños a escala (`p.modo`: dist, tam) |
En total el banco de Naturales tiene 42 ejemplos y 42 ejercicios. La prueba `prueba-nat.py` corre 91 casos.

## Sociales · `js/leccion-banco-soc.js` (27/11/2026)
Historia, Geografía, Ciudadanía, Filosofía, Economía y Ciencias Sociales. Cada ejemplo con formato visual propio, paso a paso, y su práctica. Prueba: `python3 tools/interactiva/prueba-nat.py <motor>`.
| Ejemplo | Ejercicio | Qué muestra | `p` |
|---|---|---|---|
| `linea_historica` | `linea_historica_x` (siglo, años entre fechas, también a. C.) | línea de tiempo con siglos y años transcurridos | `linea`: america, antigua, contemporanea · o `items` [{t, a, e}] |
| `coordenadas` | `coordenadas_x` (tocar la ciudad) | latitud y longitud en la grilla | — |
| `escala_mapa` | `escala_mapa_x` | medir con regla y pasar a km | — |
| `husos` | `husos_x` | husos horarios y relojes | — |
| `piramide_poblacion` | `piramide_poblacion_x` | pirámide joven, adulta y envejecida (datos aproximados) | — |
| `indicadores` | `indicadores_x` | densidad, natalidad, mortalidad, crecimiento natural | — |
| `circuito_productivo` | `circuito_productivo_x` (sectores) | etapas, sectores y valor agregado | `producto`: pan, yerba, remera |
| `mercado` | `mercado_x` | oferta, demanda, escasez, exceso y equilibrio | — |
| `inflacion` | `inflacion_x` | canasta que se encarece y poder de compra | — |
| `flujo_circular` | `flujo_circular_x` | familias, empresas y Estado | — |
| `desigualdad` | `desigualdad_x` | ingreso por quintiles y brecha | — |
| `estado` | `estado_x` (poderes) | tres poderes en tres niveles | `nivel` |
| `ley` | `ley_x` (ordenar) | cómo se hace una ley | — |
| `dhondt` | `dhondt_x` | reparto de bancas | — |
| `fuente` | `fuente_x` (primaria o secundaria) | análisis de una fuente: autor, fecha, intención | — |
| `causas` | `causas_x` (tipo de causa) | árbol de causas y consecuencias | `proceso`: mayo, industrial, crisis29 |
| `piramide_social` | `piramide_social_x` (ordenar) | sociedad feudal y colonial | `sociedad` |
| `migraciones` | `migraciones_x` (expulsión o atracción) | origen, destino y factores | `caso`: europea, regional, campo |
| `balanza_argumentos` | `balanza_argumentos_x` | argumentos a favor y en contra que inclinan la balanza | `debate`: uniforme, celulares, voto16 |
| `dilema` | `dilema_x` | un dilema desde la ética de las consecuencias, del deber y de la virtud | — |

## Nivel Medio: todas las áreas (js/leccion-banco-medio.js) — 27/11/2026
Para primaria, sobre todo de 1.º a 3.º: dibujos grandes y poco texto. Cada motor tiene su ejemplo paso a paso y su práctica (`_x`). Con `may: true` todo va en IMPRENTA MAYÚSCULA (1.º y 2.º); Tecnología y Ciudadanía escriben la explicación en minúscula. Para 4.º a 6.º sirven además los motores de secundaria que encajan (Naturales: partes, ciclo, red_trofica, recorrido, particulas, mezclas, densidad, circuito, iman, luz, calor, fuerzas, energia, sistema_solar, tierra_luna; Sociales: linea_historica, coordenadas, escala_mapa, circuito_productivo; Lengua: los de gramática y tildes de leccion-banco2.js).

| Área | Motor | Parámetros (`p`) |
|---|---|---|
| Lengua | `letras` / `letras_x` | `letras` (lista, ej. ["M","P"]); práctica `modo`: inicial, dibujo |
| Lengua | `silabas` / `silabas_x` | `palabras`; práctica `modo`: contar, armar |
| Lengua | `armar_palabra` / `armar_palabra_x` | — |
| Lengua | `oracion` / `oracion_x` | `modo`: (orden, mayúscula y punto) o signos (¿? ¡!) |
| Lengua | `rimas` / `rimas_x` | — |
| Lengua | `abecedario` / `abecedario_x` | orden alfabético |
| Lengua | `numero_genero` / `numero_genero_x` | `modo`: (singular y plural) o genero |
| Lengua | `ortografia` / `ortografia_x` | `modo`: mp_mb, r_rr, gue_gui, b_v, c_s_z, h |
| Lengua | `cuento` / `cuento_x` | inicio, problema y final con viñetas; práctica: ordenar el cuento |
| Naturales | `cuerpo` / `cuerpo_x` | `modo`: (partes) o sentidos |
| Naturales | `animales` / `animales_x` | ficha por fuera; práctica `criterio` 0 a 4 (cubierta, se mueve, come, vive, nace) |
| Naturales | `planta` / `planta_x` | `modo`: (partes) o ciclo |
| Naturales | `materiales` / `materiales_x` | pruebas de propiedades; práctica `prop` 0 a 3 |
| Naturales | `calor_frio` / `calor_frio_x` | `t`: temperatura inicial; estados del agua |
| Naturales | `sombras` / `sombras_x` | `h`: hora; día, noche y sombras |
| Naturales | `clima` / `clima_x` | tiempo atmosférico y ropa |
| Naturales | `crecer` / `crecer_x` | `ser`: personas, gallina, rana, mariposa, vaca |
| Sociales | `plano` / `plano_x` | plano del barrio, puntos cardinales y recorridos |
| Sociales | `campo_ciudad` / `campo_ciudad_x` | — |
| Sociales | `campo_mesa` / `campo_mesa_x` | `producto`: leche, pan, dulce |
| Sociales | `servicios` / `servicios_x` | servicios que llegan a casa |
| Sociales | `antes_ahora` / `antes_ahora_x` | objetos de antes y de ahora |
| Sociales | `tiempo` / `tiempo_x` | `modo`: (semana: ayer, hoy, mañana) o dia |
| Sociales | `instituciones` / `instituciones_x` | — |
| Inglés | `vocab` / `vocab_x` | `tema`: numbers, colours, family, body, animals, food, clothes, house, weather, feelings, places, jobs; práctica `modo`: escuchar, leer. Con audio 🔊 |
| Inglés | `rutina` / `rutina_x` | daily routine con reloj (o'clock) |
| Inglés | `frase_en` / `frase_en_x` | quién + qué hace + el resto |
| Tecnología | `herramientas` / `herramientas_x` | herramienta, operación y seguridad |
| Tecnología | `fabricar` / `fabricar_x` | `objeto`: mesa, remera, maceta; secuencia y producción en serie |
| Tecnología | `engranajes` / `engranajes_x` | `modo`: (engranajes) o polea; sentido y vueltas |
| Tecnología | `compu` / `compu_x` | entrada, proceso, salida y almacenamiento |
| Tecnología | `robot` / `robot_x` | programar con flechas (la práctica es programar de verdad) |
| Tecnología | `control` / `control_x` | sensor, controlador y actuador |
| Ciudadanía | `emociones` / `emociones_x` | emoción, cuerpo, termómetro y qué hacer |
| Ciudadanía | `normas` / `normas_x` | acuerdos de convivencia |
| Ciudadanía | `conflictos` / `conflictos_x` | semáforo: paro, pienso, actúo |
| Ciudadanía | `derechos` / `derechos_x` | derechos de chicas y chicos |

**Modo Medio en motores de secundaria (4.º a 6.º):** con `"medio": true` en `p`, los motores partes, ciclo, red_trofica, recorrido, clave, plato, particulas, mezclas, densidad, instrumento, grafico, experimento, circuito, fuerzas, palanca, energia, luz, calor, iman, tierra_luna, sistema_solar, linea_historica, coordenadas, escala_mapa, circuito_productivo, causas y fuente (y sus `_x`) se ven con letra y dibujo más grandes, y cada palabra técnica lleva al lado, la primera vez en cada paso, su explicación en palabras simples (glosario en js/leccion-banco-medio.js).

## Sociales, parte 2 (js/leccion-banco-soc2.js) — 27/11/2026
Geografía física, mapas históricos, períodos, Filosofía y Constitución. Cada uno con su práctica (`_x`).

| Motor | Qué muestra | Parámetros (`p`) |
|---|---|---|
| `relieve` / `relieve_x` | curvas de nivel → corte A–B → perfil topográfico; práctica: curva más alta | `forma`: cerro, dos, asim |
| `climograma` / `climograma_x` | barras de lluvia, línea de temperatura, amplitud y tipo de clima (valores aproximados) | práctica `modo`: (amplitud) o tipo |
| `biomas` / `biomas_x` | paisaje: clima → vegetación → fauna | — |
| `cuenca` / `cuenca_x` | partes de la cuenca y cursos del río; práctica: tocar en el mapa | — |
| `placas` / `placas_x` | bordes convergente, divergente y transformante, con caso real | `borde` |
| `tematico` / `tematico_x` | mapa coroplético: dato → rangos → colores → lectura | — |
| `mapa_historico` / `mapa_historico_x` | territorio que cambia con los años (Imperio inca) o ruta (Cruce de los Andes) | `modo`: (expansión) o ruta |
| `periodos` / `periodos_x` | comparar dos períodos por aspectos: cambios y continuidades | — |
| `argumento` / `argumento_x` | premisas, conclusión, indicadores; deductivo e inductivo | — |
| `falacias` / `falacias_x` | diálogo, sello con el nombre, la trampa y cómo responder | — |
| `corrientes` / `corrientes_x` | mesa de debate: una pregunta, tres pensadores (ética, conocimiento, política) | — |
| `constitucion` / `constitucion_x` | estructura de la Constitución; derechos y garantías | `modo`: (estructura) o garantias |
