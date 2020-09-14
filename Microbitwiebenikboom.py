# Add your Python code here. E.g.
from microbit import *

while True:
    boom = Image("03930:"
             "39993:"
             "69996:"
             "00900:"
             "00900")

    if button_a.is_pressed():
        display.scroll('Ik ben Tijmen')
    elif button_b.is_pressed():
        display.show(boom)
    else: display.scroll('Hello, You!', wait=True, loop=False)
