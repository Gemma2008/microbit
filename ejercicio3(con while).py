# Imports go at the top
from microbit import *

lista_numeros = [3 ,4 ,2 ,4 ,2]
total = 0
i = 0

while i < len(lista_numeros):
    total = total + lista_numeros[i]
    i = i + 1

display.scroll(total)
