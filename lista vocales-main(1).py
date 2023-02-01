# Imports go at the top
from microbit import *

lista_vocales = ["a","e","i","o","u"]

for i in lista_vocales:
    display.show(i)
    sleep(1000)
    display.show(len(lista_vocales))
