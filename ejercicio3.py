# Imports go at the top
from microbit import *

lista_numeros = [3 ,4 ,2 ,4 ,2]
z = 0

for i in lista_numeros:
    z = z + i
    display.scroll(z)

