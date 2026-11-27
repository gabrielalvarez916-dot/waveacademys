# -*- coding: utf-8 -*-
"""PRUEBA EN EL NAVEGADOR de las actividades de Naturales (js/actividades-nat.js).
Arma preguntas con la misma estructura que dibuja js/materia.js, carga los scripts de la plataforma, toca cada actividad como un alumno
y verifica que lo que arma llegue al campo que se corrige. Falla con errores de JavaScript o si algo se sale del recuadro. Capturas en /tmp/prueba-act-nat/.
Uso: python3 tools/interactiva/prueba-act-nat.py"""
import asyncio, json, pathlib, sys, html as H
from playwright.async_api import async_playwright
RAIZ = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path('/tmp/prueba-act-' + (sys.argv[1] if len(sys.argv) > 1 else 'nat')); OUT.mkdir(exist_ok=True)
SCRIPTS = ['js/leccion-banco.js', 'js/leccion-banco2.js', 'js/leccion-banco-nat.js', 'js/leccion-banco-nat2.js', 'js/leccion-banco-nat3.js', 'js/leccion-banco-soc.js', 'js/leccion-banco-soc2.js', 'js/actividades-plus.js', 'js/actividades-nat.js', 'js/actividades-soc.js', 'js/actividades-medio.js']

def sel(i, k, ops): return '<select class="mt-sel" data-w="%d" data-k="%d"><option value="">Elegí…</option>%s</select>' % (i, k, ''.join('<option value="%s">%s</option>' % (H.escape(o), H.escape(o)) for o in ops))
def pares(i, izq, der): return '<div class="mt-pares">' + ''.join('<div class="mt-par"><span>%s</span>%s</div>' % (H.escape(x), sel(i, k, der)) for k, x in enumerate(izq)) + '</div>'
def preg(i, enun, cuerpo, p_tag=True): return '<div class="mt-preg" id="q%d"><div class="mt-tipo">tipo</div><div class="mt-preg-c">%s%s</div></div>' % (i, ('<p>%s</p>' % enun) if p_tag else enun, cuerpo)
def num(i): return '<div class="nu-fila"><input type="text" class="mt-txt nu-in" data-w="%d"></div>' % i
def txt(i): return '<input type="text" class="mt-txt" name="q%d">' % i
def radios(i, ops): return '<div class="mt-ops">' + ''.join('<label class="mt-op"><input type="radio" name="q%d" value="%s"><span>%s</span></label>' % (i, H.escape(o), H.escape(o)) for o in ops) + '</div>'
def checks(i, ops): return '<div class="mt-ops">' + ''.join('<label class="mt-op"><input type="checkbox" data-w="%d" value="%s"><span>%s</span></label>' % (i, H.escape(o), H.escape(o)) for o in ops) + '</div>'
def orden(i, ops): return '<small class="mt-ayuda">Usá las flechas.</small><ol class="mt-orden" data-w="%d">' % i + ''.join('<li data-v="%s"><span class="mt-orden-t">%s</span></li>' % (H.escape(o), H.escape(o)) for o in ops) + '</ol>'

import os
NIV = ['Productor', 'Consumidor primario', 'Consumidor secundario', 'Consumidor terciario']
Q = [
 ('rotular', preg(0, '[[rotular:celula_animal]] Rotulá la célula animal.', pares(0, ['1', '2', '3', '4', '5', '6', '7', '8'], ['Membrana plasmática', 'Citoplasma', 'Núcleo', 'Mitocondria', 'Retículo endoplasmático', 'Ribosomas', 'Aparato de Golgi', 'Lisosoma']))),
 ('red', preg(1, '[[red:pastizal]] Ubicá cada especie en su nivel trófico.', pares(1, ['Pasto', 'Liebre', 'Ratón', 'Zorro', 'Puma'], NIV))),
 ('recorrido', preg(2, '[[recorrido:digestion]] Ordená el recorrido del alimento.', orden(2, ['Estómago', 'Boca', 'Intestino grueso', 'Esófago', 'Intestino delgado', 'Ano']))),
 ('clave', preg(3, '[[clave:vertebrados]] El yacaré tiene escamas duras y pone huevos en tierra. ¿A qué grupo pertenece?', radios(3, ['Aves', 'Mamíferos', 'Peces', 'Anfibios', 'Reptiles']))),
 ('punnett', preg(4, '[[punnett:Aa,Aa]] ¿Qué porcentaje de los hijos será verde (aa)?', num(4))),
 ('adn', preg(5, '[[adn:TACGGA]] Escribí la cadena complementaria.', txt(5))),
 ('arn', preg(6, '[[arn:TACGGA]] Transcribí a ARN mensajero.', txt(6))),
 ('osmosis', preg(7, '[[osmosis:2:animal]] ¿Qué le pasa al glóbulo rojo?', radios(7, ['Se hincha', 'Se arruga', 'Queda igual']))),
 ('mezclas', preg(8, '[[mezclas]] Elegí el método para cada mezcla.', pares(8, ['Arena y agua', 'Sal disuelta en agua', 'Limaduras de hierro y arena'], ['Filtración', 'Evaporación', 'Imantación', 'Decantación']))),
 ('densidad', preg(9, '[[densidad:120:30]] Calculá la densidad del objeto en g/cm³.', num(9))),
 ('instrumento', preg(10, '[[instrumento:termometro:46]] ¿Qué temperatura marca?', num(10))),
 ('atomo', preg(11, '[[atomo]] Armá el átomo de oxígeno (Z = 8, A = 16). ¿Cuántos electrones tiene en la última capa?', num(11))),
 ('tabla', preg(12, '[[tabla]] Tocá el elemento del período 3 y grupo 2.', txt(12))),
 ('balancear', preg(13, '<p class="mt-hueco-p">[[balancear:CH4+O2>CO2+H2O]] <input class="mt-hueco"> CH₄ + <input class="mt-hueco"> O₂ → <input class="mt-hueco"> CO₂ + <input class="mt-hueco"> H₂O</p>', '', p_tag=False)),
 ('ph', preg(14, '[[ph]] Clasificá cada sustancia según su pH.', pares(14, ['Limón', 'Agua pura', 'Lavandina', 'Vinagre'], ['Ácida', 'Neutra', 'Básica']))),
 ('ohm', preg(15, '[[ohm:serie:6:4:2]] Si duplicás la pila, ¿qué pasa con la corriente?', radios(15, ['Se duplica', 'Se reduce a la mitad', 'No cambia']))),
 ('pista', preg(16, '[[pista:mruv:0:2]] ¿Qué posición tiene a los 4 s?', num(16))),
 ('dcl', preg(17, '[[dcl]] Marcá las fuerzas que actúan sobre la caja empujada.', checks(17, ['Peso hacia abajo', 'Normal hacia arriba', 'Fuerza aplicada hacia la derecha', 'Rozamiento hacia la izquierda', 'Fuerza misteriosa hacia arriba']))),
 ('graficar', preg(18, '[[graficar:0,-20;2,-10;4,0;6,0;8,0;10,25|tiempo (min)|temperatura (°C)]] ¿Cuántos minutos dura la meseta?', num(18))),
 ('experimento', preg(19, '[[experimento]] ¿La luz influye en el crecimiento?', pares(19, ['La luz', 'La altura de la planta', 'El tipo de tierra', 'La cantidad de agua'], ['Cambia (variable independiente)', 'Se mide (variable dependiente)', 'Queda igual (controlada)']))),
 ('luna', preg(20, '[[luna]] Ubicá cada fase.', pares(20, ['1', '2', '3', '4'], ['Luna nueva', 'Cuarto creciente', 'Luna llena', 'Cuarto menguante']))),
 ('plato', preg(21, '[[plato]] Ubicá cada alimento en su grupo.', pares(21, ['Manzana', 'Lentejas', 'Yogur', 'Pollo'], ['Verduras y frutas', 'Legumbres, cereales, papa, pan y pastas', 'Leche, yogur y quesos', 'Carnes y huevos']))),
]

# Acciones de alumno (JS) y qué tiene que quedar en el campo que se corrige
ACC = {
 'rotular': ("b=>{const f=b.querySelector('.an-ficha');f.click();b.querySelector('[data-dest=\"2\"]').dispatchEvent(new MouseEvent('click',{bubbles:true}));return [...b.querySelectorAll('select')].map(s=>s.value).join('|')}", 'Membrana plasmática'),
 'red': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('[data-dest=\"0\"]').dispatchEvent(new MouseEvent('click',{bubbles:true}));return b.querySelector('select').value}", 'Productor'),
 'recorrido': ("b=>{b.querySelectorAll('[data-dest]')[1].dispatchEvent(new MouseEvent('click',{bubbles:true}));b.querySelectorAll('[data-dest]')[3].dispatchEvent(new MouseEvent('click',{bubbles:true}));return [...b.querySelectorAll('li')].map(l=>l.dataset.v).slice(0,2).join('|')}", 'Boca|Esófago'),
 'clave': ("b=>{for(const r of ['no','no','no','no']){b.querySelector('[data-r=\"'+r+'\"]').click()}return (b.querySelector('input:checked')||{}).value}", 'Reptiles'),
 'punnett': ("b=>{const i=[...b.querySelectorAll('.an-pun-in')];['AA','Aa','aA','aa'].forEach((v,k)=>{i[k].value=v;i[k].dispatchEvent(new Event('input',{bubbles:true}))});return b.querySelector('.an-val').textContent}", 'aa: 1 de 4'),
 'adn': ("b=>{'ATGCCT'.split('').forEach(x=>b.querySelector('[data-b=\"'+x+'\"]').click());return b.querySelector('input.mt-txt').value}", 'ATGCCT'),
 'arn': ("b=>{'AUGCCU'.split('').forEach(x=>b.querySelector('[data-b=\"'+x+'\"]').click());return b.querySelector('input.mt-txt').value}", 'AUGCCU'),
 'mezclas': ("b=>{b.querySelector('.an-ficha').click();b.querySelector('[data-dest=\"0\"]').click();return b.querySelector('select').value}", 'Filtración'),
 'densidad': ("b=>{[...b.querySelectorAll('.an-btn')].forEach(x=>x.click());return String(b.querySelectorAll('svg').length)}", '2'),
 'tabla': ("b=>{b.querySelector('[data-t=\"12\"]').dispatchEvent(new MouseEvent('click',{bubbles:true}));return b.querySelector('input.mt-txt').value}", 'Mg'),
 'balancear': ("b=>{const bs=[...b.querySelectorAll('[data-i=\"1\"][data-d=\"1\"]')];bs[0].click();b.querySelector('[data-i=\"3\"][data-d=\"1\"]').click();return [...b.querySelectorAll('.mt-hueco')].map(h=>h.value).join(',')+' '+b.querySelectorAll('.an-at.ok').length}", '1,2,1,2 3'),
 'ph': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('[data-dest=\"0\"]').dispatchEvent(new MouseEvent('click',{bubbles:true}));return b.querySelector('select').value}", 'Ácida'),
 'pista': ("b=>{for(let k=0;k<4;k++)b.querySelector('.an-btn').click();return b.querySelector('.an-tab').textContent}", '16'),
 'dcl': ("b=>{const c=b.querySelector('input[type=checkbox]');c.checked=true;c.dispatchEvent(new Event('change',{bubbles:true}));return String(b.querySelectorAll('.an-caja line').length)}", '2'),
 'experimento': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('.an-zona').click();return b.querySelector('select').value}", 'Cambia (variable independiente)'),
 'luna': ("b=>{b.querySelector('.an-ficha').click();b.querySelector('[data-dest=\"0\"]').dispatchEvent(new MouseEvent('click',{bubbles:true}));return b.querySelector('select').value}", 'Luna nueva'),
 'plato': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('[data-dest=\"0\"]').dispatchEvent(new MouseEvent('click',{bubbles:true}));return b.querySelector('select').value}", 'Verduras y frutas'),
}

QS = [
 ('cronologia', preg(0, '[[cronologia]] Ordená los hechos.', orden(0, ['Constitución Nacional (1853)', 'Revolución de Mayo (1810)', 'Llegada de Colón (1492)', 'Declaración de la Independencia (1816)']))),
 ('coordenadas', preg(1, '[[coordenadas]] ¿Qué ciudad está a 36° N y 140° E?', txt(1))),
 ('escala', preg(2, '[[escala:1000000:6]] ¿Cuántos km separan A y B?', num(2))),
 ('husos', preg(3, '[[husos:-3:9:10]] En Buenos Aires son las 10. ¿Qué hora es en Tokio?', num(3))),
 ('piramide', preg(4, '[[piramide:2]] ¿Qué tipo de pirámide es?', radios(4, ['Joven', 'Adulta', 'Envejecida']))),
 ('fuente', preg(5, '[[fuente]] «Mendoza, 1816. Querida madre: seguimos preparando mulas para cruzar la cordillera…»', pares(5, ['Autor', 'Fecha', 'Tipo de fuente'], ['Un soldado', '1816', 'Primaria', 'Una historiadora', 'Secundaria']))),
 ('arbol', preg(6, '[[arbol:Revolución de Mayo]] Ubicá cada tarjeta.', pares(6, ['Invasión de Napoleón a España', 'Primera Junta', 'Ideas de la Ilustración', 'Guerras de independencia'], ['Causa', 'Consecuencia']))),
 ('dhondt', preg(7, '<p class="mt-hueco-p">[[dhondt:42000,31000,15000:5]] A obtiene <input class="mt-hueco"> bancas, B <input class="mt-hueco"> y C <input class="mt-hueco">.</p>', '', p_tag=False)),
 ('ley', preg(8, '[[ley]] Ordená el camino de la ley.', orden(8, ['Proyecto', 'Cámara de origen', 'Cámara revisora', 'Sanción', 'Promulgación o veto', 'Publicación']))),
 ('poderes', preg(9, '[[poderes]] ¿A qué poder pertenece?', pares(9, ['Presidente', 'Congreso', 'Corte Suprema', 'Intendente'], ['Ejecutivo', 'Legislativo', 'Judicial']))),
 ('sectores', preg(10, '[[sectores]] Ubicá cada actividad.', pares(10, ['Cultivo de soja', 'Fábrica de autos', 'Supermercado'], ['Primario', 'Secundario', 'Terciario']))),
 ('mercado', preg(11, '[[mercado:100,1:0,1]] ¿Cuál es el precio de equilibrio?', num(11))),
 ('carrito', preg(12, '[[carrito]] Pan $1800 $2700; Leche $1300 $1950; Yerba $4500 $6750. ¿Qué % aumentó la canasta?', num(12))),
 ('balanza', preg(13, '[[balanza]] ¿Uniforme obligatorio?', pares(13, ['Evita la competencia por marcas', 'Limita la expresión personal', 'Es un gasto extra'], ['A favor', 'En contra']))),
 ('dilema', preg(14, '[[dilema]] Encontrás una billetera. ¿Qué hacés y por qué?', '<textarea class="mt-txt" name="q14"></textarea>')),
 ('chequeo', preg(15, '[[chequeo]] ¡¡URGENTE!! Comprobado: el agua con limón cura todo. ¡Compartí antes de que lo borren!', checks(15, ['No dice la fuente', 'Usa mayúsculas y urgencia', 'Pide compartir rápido', 'Está bien escrito']))),
 ('sociedad', preg(16, '[[sociedad]] Armá la pirámide feudal.', orden(16, ['Campesinos y siervos', 'Rey', 'Caballeros y bajo clero', 'Nobleza y alto clero']))),
 ('comparativa', preg(17, '[[comparativa]] Completá.', '<div class="mt-tabla-w"><table class="mt-tabla"><thead><tr><th>Aspecto</th><th>Grecia</th><th>Roma</th></tr></thead><tbody><tr><td>Gobierno</td><td><input class="mt-celda"></td><td><input class="mt-celda"></td></tr></tbody></table></div>')),
]
ACCS = {
 'cronologia': ("b=>{b.querySelectorAll('[data-dest]')[2].dispatchEvent(new MouseEvent('click',{bubbles:true}));b.querySelector('[data-dest=\"1\"]').dispatchEvent(new MouseEvent('click',{bubbles:true}));return [...b.querySelectorAll('li')].map(l=>l.dataset.v).slice(0,2).join('|')}", 'Llegada de Colón (1492)|Revolución de Mayo (1810)'),
 'coordenadas': ("b=>{b.querySelector('[data-t=\"8\"]').dispatchEvent(new MouseEvent('click',{bubbles:true}));return b.querySelector('input.mt-txt').value}", 'Tokio'),
 'husos': ("b=>{for(let k=0;k<10;k++)b.querySelector('[data-d=\"1\"]').click();return b.querySelector('input.nu-in').value}", '22'),
 'fuente': ("b=>{b.querySelector('[data-o]').click();b.querySelector('[data-k=\"0\"]').click();return b.querySelector('select').value}", 'Un soldado'),
 'arbol': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('.soa-zona').click();return b.querySelector('select').value}", 'Causa'),
 'dhondt': ("b=>{['0-0','1-0','0-1','1-1','2-0'].forEach(k=>b.querySelector('[data-k=\"'+k+'\"]').click());return [...b.querySelectorAll('.mt-hueco')].map(h=>h.value).join(',')}", '2,2,1'),
 'ley': ("b=>{b.querySelectorAll('[data-dest]')[0].dispatchEvent(new MouseEvent('click',{bubbles:true}));return [...b.querySelectorAll('li')][0].dataset.v}", 'Proyecto'),
 'poderes': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('.soa-zona').click();return b.querySelector('select').value}", 'Ejecutivo'),
 'mercado': ("b=>{const r=b.querySelector('input[type=range]');r.value=50;r.dispatchEvent(new Event('input',{bubbles:true}));return b.querySelector('input.nu-in').value+' '+b.textContent.includes('Equilibrio')}", '50 true'),
 'carrito': ("b=>{for(let i=0;i<3;i++)b.querySelector('[data-i=\"'+i+'\"]').click();return b.querySelector('.soa-tot').textContent}", '11.400'),
 'balanza': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('.soa-zona').click();return b.querySelector('select').value}", 'A favor'),
 'dilema': ("b=>{b.querySelector('[data-v=\"Estoy a favor\"]').click();b.querySelector('.soa-mir').click();const t=b.querySelector('.soa-razon');t.value='porque es lo justo';t.dispatchEvent(new Event('input',{bubbles:true}));return b.querySelector('textarea[name=q14]').value}", 'Estoy a favor. Lo pienso'),
 'chequeo': ("b=>{const c=b.querySelector('input[type=checkbox]');c.checked=true;c.dispatchEvent(new Event('change',{bubbles:true}));return b.querySelector('.soa-sellos').textContent}", 'No dice la fuente'),
 'sociedad': ("b=>{b.querySelectorAll('[data-dest]')[1].dispatchEvent(new MouseEvent('click',{bubbles:true}));return [...b.querySelectorAll('li')][0].dataset.v}", 'Rey'),
}
if len(sys.argv) > 1 and sys.argv[1] == 'soc': Q, ACC = QS, ACCS

QM = [
 ('armar', preg(0, '[[armar:MANZANA:🍎]] Armá la palabra.', txt(0))),
 ('silabas', preg(1, '[[silabas:MARIPOSA:🦋]] ¿Cuántas sílabas tiene?', num(1))),
 ('escuchar', preg(2, '[[escuchar:PERRO]] Escuchá y tocá el dibujo.', radios(2, ['🐶 PERRO', '🐱 GATO', '🐟 PEZ']))),
 ('escuchar_en', preg(3, '[[escuchar:dog:en]] Listen and tap.', radios(3, ['🐱 cat', '🐶 dog', '🐦 bird']))),
]
ACCM = {
 'armar': ("b=>{for(const c of 'MANZANA'){const l=[...b.querySelectorAll('[data-l]')].find(x=>!x.disabled&&x.textContent===c);l.click();}return b.querySelector('input.mt-txt').value}", 'MANZANA'),
 'silabas': ("b=>{for(let k=0;k<4;k++)b.querySelector('[data-c=\"1\"]').click();return b.querySelector('input.nu-in').value}", '4'),
 'escuchar': ("b=>{b.querySelectorAll('.amd-dib')[0].click();return [...b.querySelectorAll('input[type=radio]')].find(r=>r.checked).value}", '🐶 PERRO'),
 'escuchar_en': ("b=>{b.querySelectorAll('.amd-dib')[1].click();return [...b.querySelectorAll('input[type=radio]')].find(r=>r.checked).value}", '🐶 dog'),
}
if len(sys.argv) > 1 and sys.argv[1] == 'medio': Q, ACC = QM, ACCM

QS2 = [
 ('climograma', preg(0, '[[climograma:3]] ¿Cuál es la amplitud térmica de Mendoza?', num(0))),
 ('placas', preg(1, '[[placas]] ¿Qué borde es?', pares(1, ['Cordillera de los Andes', 'Dorsal del Atlántico', 'Falla de San Andrés'], ['Convergente', 'Divergente', 'Transformante']))),
 ('cuenca', preg(2, '[[cuenca]] Ubicá cada parte.', pares(2, ['Naciente', 'Afluente', 'Desembocadura'], ['1', '2', '6']))),
 ('argumento', preg(3, '[[argumento]] Armá el argumento.', pares(3, ['Todos los mamíferos tienen pulmones', 'La ballena es un mamífero', 'La ballena tiene pulmones'], ['Premisa', 'Conclusión']))),
 ('falacia', preg(4, '[[falacia]] —Hay que cuidar el agua. —¿Y vos qué sabés, si sos un chico?', radios(4, ['Ad hominem (contra la persona)', 'Falso dilema', 'Falsa causa']))),
 ('constitucion', preg(5, '[[constitucion]] ¿Derecho o garantía?', pares(5, ['Enseñar y aprender', 'Hábeas corpus'], ['Derecho', 'Garantía']))),
 ('periodos', preg(6, '[[periodos:Colonia:Después de 1810]] ¿Cambio o continuidad?', pares(6, ['Gobierno', 'Religión oficial'], ['Cambio', 'Continuidad']))),
 ('bioma', preg(7, '[[bioma]] ¿Dónde vive?', pares(7, ['Cactus', 'Mono aullador', 'Musgo y líquenes'], ['Desierto', 'Selva', 'Tundra']))),
]
ACCS2 = {
 'climograma': ("b=>{const s=b.querySelector('svg'),r=s.getBoundingClientRect();s.dispatchEvent(new MouseEvent('click',{bubbles:true,clientX:r.left+r.width*(70/460),clientY:r.top+r.height/2}));return b.querySelector('.an-val').textContent}", 'Mes 1'),
 'placas': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('.soa-zona').click();return b.querySelector('select').value}", 'Convergente'),
 'cuenca': ("b=>{b.querySelector('[data-sp]').click();[...b.querySelectorAll('[data-t]')].find(g=>g.textContent.trim()==='1').dispatchEvent(new MouseEvent('click',{bubbles:true}));return b.querySelector('select').value}", '1'),
 'argumento': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('.soa-zona').click();return b.querySelector('select').value}", 'Premisa'),
 'falacia': ("b=>{b.querySelector('.soa-mir').click();return [b.querySelectorAll('.soc2-chat p').length, [...b.querySelectorAll('input[type=radio]')].filter(r=>r.checked).length].join(',')}", '2,1'),
 'constitucion': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('.soa-zona').click();return b.querySelector('select').value}", 'Derecho'),
 'periodos': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('.soa-zona').click();return b.querySelector('select').value+b.querySelector('.soa-puente').textContent}", 'CambioColonia'),
 'bioma': ("b=>{b.querySelector('[data-sp]').click();b.querySelector('.soa-zona').click();return b.querySelector('select').value}", 'Desierto'),
}
if len(sys.argv) > 1 and sys.argv[1] == 'soc2': Q, ACC = QS2, ACCS2

async def main():
    page = OUT / 'p.html'
    page.write_text('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="%s"><style>body{margin:0;padding:10px}.wvp{width:560px}.mt-preg{margin:0 0 18px;padding:10px;border:1px solid #ddd}</style></head><body><div class="wvp act">%s</div>%s</body></html>' % (
        RAIZ / 'css/styles.css', ''.join(q[1] for q in Q), ''.join('<script src="%s"></script>' % (RAIZ / s) for s in SCRIPTS)), encoding='utf-8')
    malos = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = await b.new_page(viewport={'width': 600, 'height': 900})
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append(m.text) if m.type == 'warning' and 'Naturales' in m.text else None)
        await pg.goto(page.as_uri()); await pg.wait_for_timeout(600)
        for i, (nom, _) in enumerate(Q):
            blk = f'#q{i}'
            ok = await pg.evaluate(f"!!document.querySelector('{blk} .an-caja')")
            if not ok: malos.append(f'{nom}: no se armó la actividad'); continue
            if '[[' in await pg.inner_text(blk): malos.append(f'{nom}: quedó la marca a la vista')
            if nom in ACC:
                js, esperado = ACC[nom]
                r = await pg.evaluate(f"(()=>{{const b=document.querySelector('{blk}');return ({js})(b)}})()")
                if esperado not in str(r): malos.append(f'{nom}: el alumno armó y el campo quedó «{r}» (esperaba «{esperado}»)')
            sale = await pg.evaluate(f"""() => {{ const c = document.querySelector('{blk}').getBoundingClientRect(); const f = [];
                document.querySelectorAll('{blk} .an-caja *').forEach(e => {{ const q = e.getBoundingClientRect(); if (q.width && !e.closest('.an-lupa') && (q.right > c.right + 2 || q.left < c.left - 2)) f.push(e.tagName + ':' + (e.textContent||'').slice(0,25)); }});
                document.querySelectorAll('{blk} svg text').forEach(t => {{ const s = t.closest('svg').getBoundingClientRect(), q = t.getBoundingClientRect(); if (q.width && (q.right > s.right + 1 || q.left < s.left - 1 || q.top < s.top - 1 || q.bottom > s.bottom + 1)) f.push('texto fuera: ' + t.textContent.slice(0,25)); }});
                return f.slice(0,3); }}""")
            if sale: malos.append(f'{nom}: se sale → {sale}')
            await (await pg.query_selector(blk)).screenshot(path=str(OUT / f'{nom}.png'))
        for e in errs: malos.append('error: ' + e)
        await b.close()
    for x in malos: print('  ✘', x)
    print(f'{len(malos)} problema(s) en {len(Q)} actividades. Capturas en {OUT}/')
    sys.exit(1 if malos else 0)
asyncio.run(main())
