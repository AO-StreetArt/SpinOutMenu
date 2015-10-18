#Spin Out Menu

##Basics
This widget accepts a list of up to 8 option widgets.  When the center button is clicked, the option widgets are spun out around the sides.
The widget is based on a sparse grid layout, by Alexander Taylor

The widget is not really optimized for use with kv-language.  This was a conscious decision as I wanted the flexibility to use **Any** Widget as an option widget.  This is accomplished by passing in a list of option widgets that are previously defined.

##Option Widget Ordering
Option widgets are ordered in a 3x3 Sparse Grid Layout.

This means that you can specify a row and column numeric property for any widget and add it as an option widget.  Please see the MenuButton class as an example.

##Widget Sizing
Currently, the widget's overall size within a parent layout is the size of the widget fully expanded.

Please see the example for usage
