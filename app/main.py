from display.cli import *

init()

background_paint('Blue', "Hello, world!")
foreground_paint('Red', "Hello, world!")
style_paint('Dim', "Hello, world")

style_reset()
print("Hello, world")
foreground_reset()
print("Hello, world")
background_reset()
print("Hello, world")

deinit()
