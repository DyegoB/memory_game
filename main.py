#coding: utf-8


#Projeto jogo da memoria
import time
import kivy
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require('1.10.0')
class Jogo(BoxLayout):
    def __init__(self, **kwargs):
        super(Jogo, self).__init__(**kwargs)

    def on_press_click(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela())

class Tela(StackLayout):
    def __init__(self, **kwargs):
        super(Tela, self).__init__(**kwargs)
        for i in range(100):
            self.add_widget(Button(text='Test', size_hint=(0.1, 0.1),
                                   on_press=self.on_press_click))
    def on_press_click(self, bt):
        print('test')

class MemoriaApp(App):
    def build(self):
        return Jogo()

janela = MemoriaApp()
janela.run()