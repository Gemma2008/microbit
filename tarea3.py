from microbit import *
contador = 0
while True:
    if button_a.get_presses():
        contador = contador + 1
    elif button_b.get_presses():
        contador = contador - 1
    elif button_a.get_presses() and button_b.get_presses():
       contador = 0
    elif pin_logo.is_touched():
        display.show(Image.HEART)
    else:
        display.show(contador)
    
    

