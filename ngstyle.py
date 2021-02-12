#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Definição de um estilo básico
Outros estilos podem ser incluídos aqui
Os estilos são definidos por dicionários

__author__   = "Carlos R Rocha"
__license__  = "LGPL"
__version__  = "20210203-1000"
__email__    = "cticarlo@gmail.com"
__status__   = "Prototype"
"""


style0 = {
    "FormCard": {
        "background_color": (.12, .12, .12, 1.)
    },
    "NumericInput": {
        "background_color": (.118, .118, .118, 1.),
        "foreground_color": (.875, .847, .804, 1.),
        "focus_bg_color": (.18, .18, .18, 1.),
        "halign": "right",
        "write_tab": False
    },
    "TextInput": {
        "background_color": (.118, .118, .118, 1.),
        "foreground_color": (.875, .847, .804, 1.),
        "focus_bg_color": (.18, .18, .18, 1.),
        "halign": "right",
        "write_tab": False
    },
    "AlignedLabel": {
       # "background_color": None,
        "foreground_color": (.875, .847, .804, 1.),
        "halign": "right",
        "valign": "center"
    },           
    "BoxCard": {
        "background_color": (.12, .12, .12, 1.),
        "border_color": (.9, .9, .9, 1.),
        "border_width": 1
    },        
    "GridCard": {
        "background_color": (.12, .12, .12, 1.),
        "border_color": (.9, .9, .9, 1.),
        "border_width": 1
    },        
    "background_color": (.12, .12, .12, 1.)
}



def getDefault():
    return style0
