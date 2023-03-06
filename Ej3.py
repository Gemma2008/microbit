# Imports go at the top
from microbit import *
import music

image1 = Image("00900:09990:99999:00900:00900")
image2 = Image("09990:99999:00900:00900:00000")
image3 = Image("99999:00900:00900:00000:00000")
image4 = Image("13713:00000:13731:00000:13731")
image5 = Image("00000:13731:00000:13731:00000")

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.is_pressed():
        display.show(Image.HEART)
        music.play(music.CHASE)
        sleep(400)
        
    elif button_b.is_pressed():
        display.show(Image.SMILE)
        music.play(music.POWER_UP)
        sleep(400)
        
    else:
        
        display.show(image1)
        sleep(200)
        display.show(image2)
        sleep(200)
        display.show(image3)
        sleep(200)
        display.show(image4)
        sleep(200)
        display.show(image5)
        sleep(200)
        music.play(music.JUMP_UP)
