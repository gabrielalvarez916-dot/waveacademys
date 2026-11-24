# -*- coding: utf-8 -*-
"""Dibujos para los PDF de Ciencias Sociales 2 (Nivel Medio, primeros años).
Reusa los de Lengua 2 (carteles, tiras, objetos dibujados, láminas, fichas)."""
import os, importlib.util
_s = importlib.util.spec_from_file_location('figuras_leng2', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lengua-2', 'figuras.py'))
_L = importlib.util.module_from_spec(_s); _s.loader.exec_module(_L)
nombres, tiras, letras, lista, objetos, ficha, lamina, dibujo_palabra = _L.nombres, _L.tiras, _L.letras, _L.lista, _L.objetos, _L.ficha, _L.lamina, _L.dibujo_palabra
png, lienzo, F = _L.png, _L.lienzo, _L.F
