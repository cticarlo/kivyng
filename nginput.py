#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Widgets de entrada de dados customizado
Classe NumericInput - Entrada de dados numérica

__author__   = "Carlos R Rocha"
__license__  = "LGPL"
__version__  = "20210203-1000"
__email__    = "cticarlo@gmail.com"
__status__   = "Prototype"
"""
#TODO Incluir definição do alinhamento vertical (valign) em versão futura

from kivy.uix.textinput import TextInput
from kivy.properties import BoundedNumericProperty, DictProperty
import kivyng.ngstyle as ngstyle


class NumericInput(TextInput):
    """
    Estende TextInput para aceitar apenas entradas numéricas inteiras ou reais.
    No caso de reais, ainda é possível delimitar o número de casas decimais aceitas
    Gera exceção de o valor estiver fora de uma faixa definida (0-100 como padrão)
    O tipo é definido pelo parâmetro decimals. Se for nulo, é inteiro, senão é real
    """
    value = BoundedNumericProperty(0.0, min=0.0, max=100.0)
    style = DictProperty()

    def __init__(self, value=0, decimals=None, vMin=0, vMax=100, style=None, **kwargs):
        """
        Construtor do NumericInput, acrescentando características próprias a ele:
        :param value: Valor inicial do número. Default = 0
        :param decimals: Número de casas decimais permitidas. Se None, o número é inteiro, senão, é real
        :param vMin: Menor valor admissível para o valor numérico
        :param vMax: Maior valor admissível para o valor numérico
        :param style: Padrão de estilo a ser utilizado no desenho do componente
        :param kwargs: Demais parâmetros de um TextInput
        """
        kwargs['input_filter'] = 'int' if decimals is None else 'float'
        if style is None:
            self.style = ngstyle.getDefault().get('NumericInput', {})
        else:
            self.style = style.get('NumericInput', {}) 
            
            
        if 'border_color' in kwargs:
            self.style['border_color'] = kwargs['border_color']
            del kwargs['border_color']
        if 'border_width' in kwargs:
            self.style['border_width'] = kwargs['border_width']
            del kwargs['border_width']
            
        if 'foreground_color' in kwargs:
            self.style['foreground_color'] = kwargs['foreground_color']
        elif 'foreground_color' in self.style:
            kwargs['foreground_color'] = self.style['foreground_color']
            
        if 'background_color'  in kwargs:  
            self.style['background_color'] = kwargs['background_color']
        elif 'background_color' in self.style:
            kwargs['background_color'] = self.style['background_color']
        
        if 'halign' in kwargs:
            self.style['halign'] = kwargs['halign']
        elif 'halign' in self.style:
            kwargs['halign'] = self.style['halign']
        
        if 'write_tab' in kwargs:
            self.style['write_tab'] = kwargs['write_tab']
        elif 'write_tab' in self.style:
            kwargs['write_tab'] = self.style['write_tab']

        kwargs['multiline'] = False
        super().__init__(**kwargs)

        self._decimals = decimals
        self.property('value').set_min(self, vMin)
        self.property('value').set_max(self, vMax)
        self.value = int(value) if decimals is None else float(value)

        self.bind(size=self._updSize)
        self.bind(focus=self._onFocus)


    def on_value(self, *args):
        """
        Sempre que a propriedade valor mudar, atualiza o texto mostrado no Input
        :param args: Não utilizado. É o padrão dos métodos de resposta a eventos
        :return: Nada
        """
        if self._decimals is not None:
            f = "{{:.{}f}}".format(self._decimals)
            self.text = f.format(self.value)
        else:
            self.text = str(self.value)


    def _updSize(self, *args):
        """
        Atualiza o padding para manter o texto centralizado na vertical
        :param args: Ignorado. É padrão dos métodos de resposta a eventos
        :return: Nada
        """
        self.padding = [2, (self.height - self.line_height) / 2 + 2]


    def insert_text(self, substring, from_undo=False):
        """
        Estende o método pai insert_text, controlando o número de decimais inseridos
        :return: O texto realmente a ser inserido no input
        """
        if self._decimals is not None:
            p = self.text.find('.')
            if p == -1:  # Ainda nao tem ponto decimal
                x = substring.find('.')
                if x != -1 and len(substring.split('.')[1]) > self._decimals:
                    return super().insert_text('', from_undo=from_undo)
            else:
                if self.cursor_col >= p:
                    if len(substring) + len(self.text.split('.')[1]) > self._decimals:
                        return super().insert_text('', from_undo=from_undo)

        return super().insert_text(substring, from_undo=from_undo)


    def on_text_validate(self, *args):
        """
        Estende o método on_text_validate para considerar os limites de valor numérico
        Quando excedido, ele mantém o valor numérico atual, atualizando o texto
        Seria mais interessante disparar uma exceção???
        :param args: Padrão de métodos de resposta a eventos
        :return: Nada
        """
        x = int(self.text) if self._decimals is None else float(self.text)
        if self.property('value').get_min(self) <= x <= self.property('value').get_max(self):
            self.value = x
        else:
            self.text = str(self.value)


    def _onFocus(self, instance, value):
        """
        Se houver estilo definido e cores diferentes de fundo para o input com e sem o foco
        este método alternará as cores de acordo com o estado de foco
        :param instance: Padrão deste tipo de resposta a evento (não usado)
        :param value: Padrão deste tipo de resposta a evento (não usado)
        :return: Nada
        """
        if 'background_color' in self.style and 'focus_bg_color' in self.style \
           and self.style['background_color'] and self.style['focus_bg_color']:
            self.background_color = self.style['focus_bg_color'] if value else self.style['background_color']

