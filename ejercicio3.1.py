# Imports go at the top
from microbit import *

lista_palabras = ["a","b","c"]
palabra = ""
for i in lista_palabras:
    palabra = palabra + i

display.scroll(palabra)
    
