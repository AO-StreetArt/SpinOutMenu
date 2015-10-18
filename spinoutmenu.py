# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:22:21 2015
Spin Out Menu
@author: alex
"""

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.properties import ObjectProperty, BooleanProperty, ListProperty, NumericProperty, StringProperty, ReferenceListProperty
from kivy.uix.image import Image
from kivy.uix.button import Button

#A button that can be used with the spin out menu
class MenuButton(Button):
    row = NumericProperty(1)
    column = NumericProperty(1)

#SparseGrid taken from Alexander Taylor & modified
class SparseGridLayout(FloatLayout):

    rows = NumericProperty(1)
    columns = NumericProperty(1)
    shape = ReferenceListProperty(rows, columns)

    def do_layout(self, *args):
        shape_hint = (1. / self.columns, 1. / self.rows)
        for child in self.children:
            child.size_hint = shape_hint
            if not hasattr(child, 'row'):
                child.row = 0
            if not hasattr(child, 'column'):
                child.column = 0

            child.pos_hint = {'x': shape_hint[0] * child.row,
                              'y': shape_hint[1] * child.column}
        super(SparseGridLayout, self).do_layout(*args)

#This class defines the line drawn between two nodes
class MenuConnector(Widget):
    
    #Front and Back vertices, the line is drawn in between
    #2 Entry Lists
    front = ListProperty([0, 0])
    back = ListProperty([1, 1])
    
    #The color of the lines
    #3 Entry Lists
    line_color = ListProperty([1, 1, 1])
    
    ellipse_diameter = NumericProperty(20)
    
    def __init__(self, **kwargs):
        super(MenuConnector, self).__init__(**kwargs)
        self.bind(front=self.set_front, back=self.set_back, line_color=self.set_color)
    
    def set_front(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(self.line_color[0], self.line_color[1], self.line_color[2])
            Line(points=[self.front[0], self.front[1], self.back[0], self.back[1]])
    
    def set_back(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(self.line_color[0], self.line_color[1], self.line_color[2])
            Line(points=[self.front[0], self.front[1], self.back[0], self.back[1]])
    
    def set_color(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(self.line_color[0], self.line_color[1], self.line_color[2])
            Line(points=[self.front[0], self.front[1], self.back[0], self.back[1]])
    
#This defines a spin out menu
class SpinOutMenu(SparseGridLayout):
    
    #Property exposed to set the list of option widgets
    options = ListProperty([])    

    #The color of the connection lines in rgb
    connector_color = ListProperty([1, 1, 1])
    
    #The normal background of the center button
    center_background_normal=StringProperty('img/press_node_small.png')
    
    #The pressed background of the center button
    center_background_down=StringProperty('img/press_node_down_small.png')
    
    #The text of the center button
    center_text=StringProperty('')
    
    #Internal Properties
    #The Center Widget
    center_node = ObjectProperty(None)
    
    #Internal property to track the connections
    connect = ListProperty([])
    
    def __init__(self, **kwargs):
        super(SpinOutMenu, self).__init__(**kwargs)
        self.rows=3
        self.columns=3
        #create the center button & bind the properties
        c_node = MenuButton(row=1, column=1, background_normal=self.center_background_normal, background_down=self.center_background_down, text=self.center_text)
        c_node.bind(pos=self.set_front, on_press=self.press_front)
        self.bind(center_background_normal=self.setcenterbackgroundnormal, center_background_down=self.setcenterbackgrounddown)
        self.center_node = c_node
        self.add_widget(self.center_node)
        
    def setcenterbackgroundnormal(self, *args):
        self.center.background_normal=self.center_background_normal
        
    def setcenterbackgrounddown(self, *args):
        self.center.background_normal=self.center_background_normal        
        
    def set_front(self, *args):
        for con in self.connect:
            con.front = self.center_node.center
        
    def set_back(self, *args):
        i=0
        for con in self.connect:
            con.back = self.options[i].center
            i+=1
        
    def press_front(self, *args):
        #Add the option nodes and connectors to the widget if it's closed
        #Otherwise, close the widget
        if len(self.connect) == 0:
            for option in self.options:
                connector = MenuConnector(line_color=self.connector_color)
                self.connect.append(connector)
        if len(self.children) == 1:
            i=0
            self.clear_widgets()
            for con in self.connect:
                self.add_widget(con)
            for option in self.options:
                option.bind(pos=self.set_back)
                self.add_widget(option)
                i += 1
            self.add_widget(self.center_node)
                
            for con in self.connect:
                con.front = self.center_node.center
        else:
            self.clear_widgets()
            self.add_widget(self.center_node)