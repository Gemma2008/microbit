# Imports go at the top
from microbit import *

name = 'Gemma'
display.scroll(name)

while True:
    display.show(Image.ARROW_E)
    sleep(1000)
    display.show(Image.ARROW_S)
    sleep(1000)
