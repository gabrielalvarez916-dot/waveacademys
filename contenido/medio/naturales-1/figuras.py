# -*- coding: utf-8 -*-
"""Dibujos para los PDF de Ciencias Naturales 1 (Nivel Medio, primeros años). Reusa los carteles de Lengua 1 y la base de Matemática 1."""
import os, importlib.util
_s = importlib.util.spec_from_file_location('figuras_leng1', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lengua-1', 'figuras.py'))
_L = importlib.util.module_from_spec(_s); _s.loader.exec_module(_L)
nombres, tiras, letras, lista = _L.nombres, _L.tiras, _L.letras, _L.lista
