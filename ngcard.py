#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Widgets derivados dos layouts, para criação de cards organizando outros
componentes. Se diferenciam dos layouts por implementarem cor de fundo e
propriedades de visibilidade/invisibilidade (em alguns deles)

__author__   = "Carlos R Rocha"
__license__  = "LGPL"
__version__  = "20210204-2030"
__email__    = "cticarlo@gmail.com"
__status__   = "Prototype"
"""

from kivy.properties import DictProperty
from kivy.graphics import Rectangle, Line, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import kivyng.ngstyle as ngstyle

class BoxCard(BoxLayout):
    """
    Especialização do BoxLayout, com definição de cor de fundo (opcional)
    e definição de uma borda
    """
    style = DictProperty()
    
    def __init__(self, style=None, **kwargs):
        """
        Construtor do BoxCard, acrescentando características próprias a ele:
        :param style: Padrão de estilo a ser utilizado no desenho do componente
        :param background_color: Cor de fundo do Widget (lista de 4 componentes)
        :param border_color: Cor da borda do Widget (lista de 4 componentes)
        :param kwargs: Demais parâmetros de um BoxLayout
        """
        if style is None:
            self.style = ngstyle.getDefault().get('BoxCard', {})
        else:
            self.style = style.get('BoxCard', {})        
        if 'background_color' in kwargs:
            self.style['background_color'] = kwargs['background_color']
            del kwargs['background_color']
        if 'border_color' in kwargs:
            self.style['border_color'] = kwargs['border_color']
            del kwargs['border_color']
        if 'border_width' in kwargs:
            self.style['border_width'] = kwargs['border_width']
            del kwargs['border_width']
        self._widgets = [] #  Relacao de widgets do card (todos)
        
        super().__init__(**kwargs)
        
        with self.canvas.before:
            if 'background_color' in self.style and self.style['background_color']:
                Color(rgba=self.style['background_color'])
                self._rect = Rectangle(pos=self.pos, size=self.size)
            else:
                self._rect = None
            if 'border_color' in self.style and 'border_width' in self.style \
                and self.style['border_color'] and self.style['border_width']:
                Color(rgba=self.style['border_color'])
                self._border = Line(rectangle=(self.x, self.y, self.width, self.height),
                                    width=self.style['border_width'])
            else:
                self._border = None

        self.bind(size=self._update_rect, pos=self._update_rect)


    def _update_rect(self, *args):
        """
        Atualiza o canvas do card, ajustando dimensões do fundo e da borda,
        se estes estiverem definidos
        """
        if self._rect:
            self._rect.pos = self.pos
            self._rect.size = self.size
        if self._border:
            self._border.rectangle = (self.x, self.y, self.width, self.height)


    def add_widget(self, widget, index=0, canvas=None):
        """
        Sobrecarga do método add_widget, para montar a lista de widgets auxiliar,
        que será utilizado para tornar os componentes visíveis e invisíveis
        
        """
        if index:
            self._widgets.insert(index, widget)
        else:
            self._widgets.insert(0, widget)
           
        super().add_widget(widget, index, canvas)


    def remove_widget(self, widget):
        """
        Sobrecarga do método remove_widget, para atualizar a lista de widgets auxiliar,
        que será utilizado para tornar os componentes visíveis e invisíveis
        """
        if widget in self._widgets:
            self._widgets.remove(widget)            
        
        super().remove_widget(widget)


    def setVisible(self, widget=None, visible=True):
        """
        Implementa uma propriedade de visibilidade de um widget. Se ele for
        visível, será parte dos children do BoxCard. Do contrário, só existirá
        na lista auxiliar. Ao tornar um componente visível, ele será inserido 
        novamente no BoxCard
        :param widget: Widget cuja visibilidade será definida
        :param visible: Definne a visibilidade do componente
        """
        if widget in self._widgets:
            if visible:
                if widget not in self.children:
                    super().add_widget(widget, self._widgets.index(widget))
            else:
                if widget in self.children:
                    super().remove_widget(widget)
                    


class VerticalBoxCard(BoxCard):
    """
    Especialização do BoxCard, que trabalha com layout vertical.
    Nada demais, apenas um atalho
    """

    def __init__(self, style=None, **kwargs):
        kwargs['orientation'] = 'vertical'
        super().__init__(style, **kwargs)


        
class HorizontalBoxCard(BoxCard):
    """
    Especialização do BoxCard, que trabalha com layout horizontal.
    Nada demais, apenas um atalho
    """

    def __init__(self, style=None, **kwargs):
        kwargs['orientation'] = 'horizontal'
        super().__init__(style, **kwargs)
        


class FormCard(GridLayout):
    """
    Especialização do GridLayout, com definição de cor de fundo (opcional)
    e definição de uma borda e limitado a 2 colunas (label + input)
    """
    style = DictProperty()
    
    def __init__(self, style=None, **kwargs):
        """
        Construtor do FormCard, acrescentando características próprias a ele:
        :param style: Padrão de estilo a ser utilizado no desenho do componente
        :param background_color: Cor de fundo do Widget (lista de 4 componentes)
        :param border_color: Cor da borda do Widget (lista de 4 componentes)
        :param kwargs: Demais parâmetros de um GridLayout
        """
        if style is None:
            self.style = ngstyle.getDefault().get('GridCard', {})
        else:
            self.style = style.get('GridCard', {})        
        if 'background_color' in kwargs:
            self.style['background_color'] = kwargs['background_color']
            del kwargs['background_color']
        if 'border_color' in kwargs:
            self.style['border_color'] = kwargs['border_color']
            del kwargs['border_color']
        if 'border_width' in kwargs:
            self.style['border_width'] = kwargs['border_width']
            del kwargs['border_width']
        self._widgets = [] #  Relacao de widgets do card (todos)
        kwargs['cols'] = 2
        
        super().__init__(**kwargs)
        
        with self.canvas.before:
            if 'background_color' in self.style and self.style['background_color']:
                Color(rgba=self.style['background_color'])
                self._rect = Rectangle(pos=self.pos, size=self.size)
            else:
                self._rect = None
            if 'border_color' in self.style and 'border_width' in self.style \
                and self.style['border_color'] and self.style['border_width']:
                Color(rgba=self.style['border_color'])
                self._border = Line(rectangle=(self.x, self.y, self.width, self.height),
                                    width=self.style['border_width'])
            else:
                self._border = None

        self.bind(size=self._update_rect, pos=self._update_rect)


    def _update_rect(self, *args):
        """
        Atualiza o canvas do card, ajustando dimensões do fundo e da borda,
        se estes estiverem definidos
        """
        if self._rect:
            self._rect.pos = self.pos
            self._rect.size = self.size
        if self._border:
            self._border.rectangle = (self.x, self.y, self.width, self.height)


    def add_widget(self, widget, index=0, canvas=None):
        """
        Sobrecarga do método add_widget, para montar a lista de widgets auxiliar,
        que será utilizado para tornar os componentes visíveis e invisíveis        
        """
        if index:
            self._widgets.insert(index, widget)
        else:
            self._widgets.insert(0, widget)
           
        super().add_widget(widget, index, canvas)


    def remove_widget(self, widget):
        """
        Sobrecarga do método remove_widget, para atualizar a lista de widgets auxiliar,
        que será utilizado para tornar os componentes visíveis e invisíveis
        """
        if widget in self._widgets:
            self._widgets.remove(widget)            
        
        super().remove_widget(widget)


    def setVisible(self, widget=None, visible=True):
        """
        Implementa uma propriedade de visibilidade de um widget. Se ele for
        visível, será parte dos children do BoxCard. Do contrário, só existirá
        na lista auxiliar. Ao tornar um componente visível, ele será inserido 
        novamente no BoxCard
        :param widget: Widget cuja visibilidade será definida
        :param visible: Definne a visibilidade do componente
        """
        if widget in self._widgets:
            if visible:
                if widget not in self.children:
                    pos = self._widgets.index(widget)
                    super().add_widget(widget, pos)
                    if (pos%2):
                        super().add_widget(self._widgets[pos-1], pos-1)
                    else:
                        if pos < len(self._widgets)-1:
                            super().add_widget(self._widgets[pos+1], pos+1)
            else:
                if widget in self.children:
                    pos = self._widgets.index(widget)
                    super().remove_widget(widget)
                    if (pos%2):
                        super().remove_widget(self._widgets[pos-1])
                    else:
                        if pos < len(self._widgets)-1:
                            super().remove_widget(self._widgets[pos+1])
