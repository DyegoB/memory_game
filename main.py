#coding: utf-8

__author__ = 'Diego Braucks'

import kivy
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import random

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
        self.list_id = []
        x = 1
        for i in range(100):
            #create buttons in range(100) 0 to 99
            #variavel ID = x #contador
            bt = Button(id=str(x), text=str(x), size_hint=(0.1, 0.1))
            bt.bind(on_press=self.on_press_click)
            #bt.bind(on_release=self.on_release_click)
            self.list_id.append(str(x))
            x += 1
            self.add_widget(bt)

        #raffle pictures
        list_img = ['poker.jpg', 'poker_1.jpg']
        self.dc = dict()
        for id in self.list_id:
            img = random.choice(list_img)
            self.dc[id] = img
    def on_press_click(self, bt):
        print(self.dc[bt.id])

    def on_release_click(self, bt):
        print('deselect')

class MemoriaApp(App):
    def build(self):
        return Jogo()

janela = MemoriaApp()
janela.run()