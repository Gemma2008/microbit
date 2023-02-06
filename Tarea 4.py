from microbit import *

bola1 = Image("00900:09090:90009:09090:00900")
bola2 = Image("00090:00909:09009:90009:09090")
bola3 = Image("00009:00090:00900:09000:90000")
bola4 = Image("00090:00909:09009:90009:09090")
bola5 = Image("00900:09090:90009:09090:00900")

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
