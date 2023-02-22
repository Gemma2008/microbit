from microbit import *
#importamos radio
import radio
'''
Configuración RADIO
'''
radio.on()
radio.config(channel=3)

#Siempre en ejecución
while True:
    message = radio.receive()
    sleep(20)
    if message is not None:
        display.scroll(str(message))
    
