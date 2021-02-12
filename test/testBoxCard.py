import sys
sys.path.insert(0,'..')

from kivy.clock import Clock
from kivy.app import App
from kivy.uix.label import Label
from ngdisplay import AlignedLabel
from nginput import NumericInput
from ngcard import VerticalBoxCard

class MainApp(App):
    def build(self):
        self.tela = VerticalBoxCard(padding=5, spacing=5)
        self.label = AlignedLabel(text='Hello from Kivy')
        self.edit = NumericInput(10, 2)
        self.lb = Label(text="Extra")
        self.tela.add_widget(self.label)
        self.tela.add_widget(self.edit)
        self.tela.add_widget(self.lb)
        Clock.schedule_once (self.escondeLabel, 3.)
        return self.tela


    def escondeLabel(self, dt):
        self.tela.setVisible(self.edit, False)
        Clock.schedule_once(self.mostraLabel, 3.)

    def mostraLabel(self, dt):
        self.tela.setVisible(self.edit, True)


if __name__ == '__main__':
    MainApp().run()

