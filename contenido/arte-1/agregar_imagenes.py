# -*- coding: utf-8 -*-
"""Pone en las clases animadas de Arte las mismas imágenes que tiene el PDF (plantilla "imagen": aparece la imagen y se señala cada parte
mientras se nombra). Idempotente. Correr después de mision-N.py y antes de armar.py."""
import json, os, base64, io
import numpy as np
from PIL import Image
AQUI = os.path.dirname(os.path.abspath(__file__)); LEC = os.path.join(AQUI, '..', '..', 'tools', 'clase', 'lecciones')

def foto(m, nivel):
    d = json.load(open(os.path.join(AQUI, f'mision-{m}', f'mision-{m}.json'), encoding='utf-8'))
    for s in d['niveles'][str(nivel)]['secciones']:
        for b in s['bloques']:
            if b['tipo'] == 'imagen': return b['png_base64'], b['titulo']

def centro(b64, hexa, tol=14):
    im = np.array(Image.open(io.BytesIO(base64.b64decode(b64))).convert('RGB')).astype(int)
    c = np.array([int(hexa[i:i + 2], 16) for i in (1, 3, 5)]); ys, xs = np.where(np.abs(im - c).sum(axis=2) < tol)
    return round(float(xs.mean()) / im.shape[1], 3), round(float(ys.mean()) / im.shape[0], 3)

def escena(b64, titulo, marcas, voz):
    im = Image.open(io.BytesIO(base64.b64decode(b64)))
    return {'t': 'imagen', 'src': 'data:image/png;base64,' + b64, 'ancho': im.size[0], 'alto': im.size[1], 'titulo': titulo, 'marcas': [{'x': x, 'y': y, 'txt': t} for x, y, t in marcas], 'voz': voz}

def poner(slug, esc):
    p = os.path.join(LEC, slug + '.json'); d = json.load(open(p, encoding='utf-8'))
    d['escenas'] = [e for e in d['escenas'] if e.get('t') != 'imagen']
    k = next((i for i, e in enumerate(d['escenas']) if e['t'] == 'pregunta'), len(d['escenas']) - 1)
    d['escenas'].insert(k, esc); json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

b, _ = foto(1, 2)
poner('arte1-m1-n2', escena(b, 'PUNTO, LÍNEA Y PLANO', [(0.15, 0.5, 'Puntos: marcas mínimas'), (0.5, 0.6, 'Líneas: recorridos'), (0.83, 0.55, 'Planos: superficies')],
      ['Mirá los tres elementos juntos.', 'Los *puntos*: marcas mínimas.', 'Las *líneas*: recorridos que guían.', 'Y los *planos*: superficies que se superponen.']))
b, _ = foto(1, 3)
poner('arte1-m1-n3', escena(b, '¿UN VASO O DOS ROSTROS?', [(0.5, 0.55, 'Figura: el vaso'), (0.14, 0.5, 'Fondo: los rostros')],
      ['Mirá este famoso dibujo.', 'Si ves el *vaso*, la figura es el vaso.', 'Si ves los *rostros*, el vaso pasa a ser el fondo.']))
b, _ = foto(2, 2)
poner('arte1-m2-n2', escena(b, 'LUZ Y SOMBRA EN UNA ESFERA', [(0.37, 0.23, 'Luz'), (0.59, 0.43, 'Sombra propia'), (0.68, 0.68, 'Sombra proyectada'), (0.54, 0.57, 'Luz reflejada')],
      ['Mirá una esfera iluminada.', 'La *luz* llega desde arriba.', 'La *sombra propia* está del lado opuesto.', 'La *sombra proyectada* cae sobre el piso.', 'Y la *luz reflejada* aclara el borde de la sombra.']))
b, _ = foto(2, 3)
poner('arte1-m2-n3', escena(b, 'PERSPECTIVA DE UN PUNTO DE FUGA', [(0.5, 0.45, 'Punto de fuga'), (0.88, 0.45, 'Línea de horizonte'), (0.18, 0.82, 'Cerca: se ve grande')],
      ['Mirá una calle en perspectiva.', 'El *punto de fuga* está en el centro del horizonte.', 'La *línea de horizonte* está a la altura de los ojos.', 'Lo *cercano* se ve grande y lo lejano se achica.']))
b, _ = foto(3, 1)
R, A, Z, NA, VI = centro(b, '#e63946'), centro(b, '#f9c22e'), centro(b, '#2b7fd1'), centro(b, '#f4722b'), centro(b, '#4a4ec9')
poner('arte1-m3-n1', escena(b, 'CÍRCULO CROMÁTICO', [(*R, 'Primario: rojo'), (*A, 'Primario: amarillo'), (*Z, 'Primario: azul')],
      ['Mirá el círculo cromático completo.', 'El *rojo* es un primario.', 'El *amarillo* también.', 'Y el *azul* es el tercer primario.']))
poner('arte1-m3-n2', escena(b, 'CÍRCULO CROMÁTICO', [(*NA, 'Cálidos'), (*VI, 'Fríos'), (*Z, 'Azul y naranja: complementarios')],
      ['Volvé al círculo cromático.', 'Estos son los *cálidos*.', 'Y estos, los *fríos*.', 'El *azul* está enfrentado al *naranja*: son complementarios.']))
b, _ = foto(4, 1)
poner('arte1-m4-n1', escena(b, 'TEXTURAS VISUALES', [(0.16, 0.29, 'Rugosa'), (0.84, 0.29, 'Punteada'), (0.49, 0.78, 'Ondulada')],
      ['Mirá seis texturas visuales.', 'La *rugosa*, hecha con trazos cortos.', 'La *punteada*, hecha con puntos.', 'Y la *ondulada*, con líneas curvas.']))
b, _ = foto(5, 1)
poner('arte1-m5-n1', escena(b, 'TRES FORMAS DE COMPONER', [(0.17, 0.55, 'Simétrica'), (0.43, 0.47, 'Asimétrica'), (0.83, 0.38, 'Regla de tercios')],
      ['Mirá tres formas de componer.', 'La *simétrica*: partes iguales a ambos lados.', 'La *asimétrica*: elementos distintos que se compensan.', 'Y la regla de *tercios*: el interés va en una intersección.']))
b, _ = foto(5, 2)
poner('arte1-m5-n2', escena(b, 'PLANOS DE UNA IMAGEN', [(0.165, 0.7, 'Plano general'), (0.5, 0.5, 'Plano medio'), (0.83, 0.5, 'Primer plano')],
      ['Mirá la misma figura en tres planos.', 'En el *plano general* se ve chica.', 'En el *plano medio* se ve de la cintura.', 'Y en el *primer plano* ocupa casi todo el cuadro.']))
b, _ = foto(6, 4)
poner('arte1-m6-n4', escena(b, 'DESARROLLO PLANO DE UN CUBO', [(0.16, 0.5, 'Caras'), (0.49, 0.65, 'Pliegues'), (0.955, 0.5, 'Solapa para pegar')],
      ['Mirá el desarrollo plano de un cubo.', 'Las *caras* son seis cuadrados.', 'Los *pliegues* se marcan antes de doblar.', 'Y la *solapa* se pega para cerrar el cubo.']))
print('ok')
