# Imports go at the top
from microbit import *

frutas = ["Fresas","Manzana","Aguacate"]

for f in frutas:
    display.scroll(f)
    sleep(500)