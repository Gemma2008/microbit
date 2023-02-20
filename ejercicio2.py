# Imports go at the top
from microbit import *
animales = ["Vaca","Caballo","Elefante","Tigre"]
for f in animales:
    display.scroll(f)
    sleep(500)
