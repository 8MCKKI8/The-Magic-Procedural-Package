import hou

def show_message(text):
    hou.ui.displayMessage(text, title="YoKo ORGANIC Guide")


def run():

    title = "HELLO! and Thank you for choosing YoKo ORGANIC for Houdini!"

    guide = """
This guide will help you navigate the tools and buttons.

-----------------------------------------
:::AGUAWARP:::
-----------------------------------------
Creates an automatic oceanic plane with customizable wave features.

-----------------------------------------
:::GUIDE:::
-----------------------------------------
You are reading it right now — explains all tool functions.

-----------------------------------------
:::MORPHER::: 
-----------------------------------------

Creates a custom poly-morph object that is easy to alter and deform.

-----------------------------------------
:::PLANE:::
-----------------------------------------

Creates a simple, extrudable grid.

-----------------------------------------
:::PLANTTOPOINT:::
-----------------------------------------

Creates a surface that can automatically copy geometry to points '(When data is given)'

-----------------------------------------
:::DOTTER:::
-----------------------------------------

Creates a cutomizable altered grid for particle creation.

-----------------------------------------
:::ORGANICRINGER:::
-----------------------------------------

Creates a instant poly ringer. (Default is flower)

-----------------------------------------
:::IMAGETOMOD:::
-----------------------------------------

Creates an instant image to 3D poly '(When data is given)'
"""

    show_message(title + "\n\n" + guide)