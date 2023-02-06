from microbit import *

number = 1
while number < 101:
    display.scroll(number)
    number = number + 2
display.scroll('finish')
