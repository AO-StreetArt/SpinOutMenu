# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:58:11 2015

Spin Out Menu Example
@author: alex
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from spinoutmenu import SpinOutMenu, MenuButton

class SpinOutExampleWidget(GridLayout):
    def __init__(self, **kwargs):

        super(SpinOutExampleWidget, self).__init__(**kwargs)
        
        #Set the columns in the grid layout and add a label as the first widget        
        self.cols=3
        lbl1 = Label(text='Spin')
        self.add_widget(lbl1)
        
        #Create the spin out menu, using the available options
        spin = SpinOutMenu(connector_color=[1, 0.75, 0.5], center_text='Test')
        
        #Create the Menu Buttons
        opt1 = MenuButton(row=1, column=2, background_normal='img/drag_node_small.png', background_down='img/drag_node_down_small.png')
        opt2 = MenuButton(row=2, column=1, background_normal='img/drag_node_small.png', background_down='img/drag_node_down_small.png')
        opt3 = MenuButton(row=1, column=0, background_normal='img/drag_node_small.png', background_down='img/drag_node_down_small.png')
        opt4 = MenuButton(row=0, column=1, background_normal='img/drag_node_small.png', background_down='img/drag_node_down_small.png')
        opt5 = MenuButton(row=2, column=2, background_normal='img/drag_node_small.png', background_down='img/drag_node_down_small.png')
        opt6 = MenuButton(row=2, column=0, background_normal='img/drag_node_small.png', background_down='img/drag_node_down_small.png')
        opt7 = MenuButton(row=0, column=2, background_normal='img/drag_node_small.png', background_down='img/drag_node_down_small.png')
        opt8 = MenuButton(row=0, column=0, background_normal='img/drag_node_small.png', background_down='img/drag_node_down_small.png')
        
        spin.options = [opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8]        
        
        #Add the spin out menu to the grid layout
        self.add_widget(spin)
        
        #Add a second label to the grid layout
        lbl2 = Label(text='Spin')
        self.add_widget(lbl2)

class SpinOutExampleApp(App):
    def build(self):
        root = SpinOutExampleWidget()
        return root
  
if __name__ == '__main__':
    SpinOutExampleApp().run()
