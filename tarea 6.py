from microbit import *
import speech
notas_musicales = ["Do","Re","Mi","Fa","Sol","La","Si"]

for i in notas_musicales:
    speech.say(i)
    sleep(500)
