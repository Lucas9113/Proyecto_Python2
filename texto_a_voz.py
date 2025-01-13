"Escript that converts the text file to audio using the pyttsx3 library"

import pyttsx3

# Open text file

with open(r'book.txt') as texto:
    texto = texto.read()



# Initialize the library

engine = pyttsx3.init()

# Configure voice, rate, and volume parameters

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

rate = engine.setProperty('rate', 120 )

volumen = engine.setProperty('volumen', 1.0)

# Pass the text we opened earlier for it to play.

engine.say(texto)


engine.runAndWait()