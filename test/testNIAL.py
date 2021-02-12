import sys
sys.path.insert(0,'..')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from ngdisplay import AlignedLabel
from nginput import NumericInput

class MainApp(App):
    def build(self):
        tela = BoxLayout(orientation='vertical')
        label = AlignedLabel(text='Hello from Kivy')
        edit = NumericInput(10, 2)
        tela.add_widget(label)
        tela.add_widget(edit)
        return tela


if __name__ == '__main__':
    MainApp().run()

