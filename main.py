#coding: utf-8

__author__ = 'Diego Braucks'

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
        #this function makes the exchange of Jogo instances to Tela whenever button
        #is pressed
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela())

class Tela(StackLayout):
    def __init__(self, **kwargs):
        super(Tela, self).__init__(**kwargs)
        for i in range(100):
            #create buttons in range(100) 0 to 99
            self.add_widget(Button(text='Test', size_hint=(0.1, 0.1),
                                   on_press=self.on_press_click))
    def on_press_click(self, bt):
        #all the buttons created with for loop shared this function
        print('test')

class MemoriaApp(App):
    def build(self):
        return Jogo()

janela = MemoriaApp()
janela.run()