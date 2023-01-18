from microbit import *

bola1 = Image("30099:99999:00003:99999:99000")
bola2 = Image("99900:00003:99999:30000:00999")
bola3 = Image("99900:00000:00000:00000:00999")
bola4 = Image("00999:30000:00000:00003:99900")
bola5 = Image("00000:99999:99999:99999:00000")

while True:
    display.show(bola1)
    sleep(200)
    display.show(bola2)
    sleep(200)
    display.show(bola3)
    sleep(200)
    display.show(bola4)
    sleep(200)
    display.show(bola5)
    sleep(200)

