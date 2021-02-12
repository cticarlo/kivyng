#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Widgets de apresentação de dados (somente leitura)
Classe NumericInput - Entrada de dados numérica

__author__   = "Carlos R Rocha"
__license__  = "LGPL"
__version__  = "20210204-1400"
__email__    = "cticarlo@gmail.com"
__status__   = "Prototype"
"""

from kivy.properties import DictProperty
from kivy.graphics import Rectangle, Color
from kivy.uix.label import Label
import kivyng.ngstyle as ngstyle


class AlignedLabel (Label):
    """
    Estende o widget Label, fazendo com que o texto dele assuma
    toda a área disponível, e assim possa trabalhar com alinhamento
    Além disso, inclui um preenchimento de fundo opcional
    """
    style = DictProperty()
    
    def __init__(self, style=None, **kwargs):
        """
        Construtor do AlignedDisplay, acrescentando características próprias a ele:
        :param style: Padrão de estilo a ser utilizado no desenho do componente
        :param background_color: Cor de fundo do Widget (lista de 4 componentes)
        :param kwargs: Demais parâmetros de um Label
        """
        if style is None:
            self.style = ngstyle.getDefault().get('AlignedLabel', {})
        else:
            self.style = style.get('AlignedLabel', {})  

        if 'color' in kwargs:
            self.style['color'] = kwargs['color']
        elif 'color' in self.style:
            kwargs['color'] = self.style['color']
            
        if 'halign' in kwargs:
            self.style['halign'] = kwargs['halign']
        elif 'halign' in self.style:
            kwargs['halign'] = self.style['halign']
        
        if 'valign' in kwargs:
            self.style['valign'] = kwargs['valign']
        elif 'valign' in self.style:
            kwargs['valign'] = self.style['valign']
                    
        if 'background_color' in kwargs:  
            self.style['background_color'] = kwargs['background_color']
            del kwargs['background_color']
            
        super().__init__(**kwargs)
        
        if 'background_color' in self.style:
            with self.canvas.before:
                Color(rgba=self.style['background_color'])
                self._rect = Rectangle(pos=self.pos, size=self.size)                
        
        self.bind(size=self._updTextSize, pos=self._updTextSize)
     
        
    def _updTextSize(self, *args):
        """
        Atualiza as dimensões do texto e do retângulo de fundo (se houver)
        cada vez que o widget é redimensionado ou reposicionado
        :param args - Lista de argumentos padrão para gerenciador de eventos
        não empregado nesta função
        """
        self.text_size = self.size
        if 'background_color' in self.style and self.style['background_color']:
            self._rect.pos = self.pos
            self._rect.size = self.size
        
 
        