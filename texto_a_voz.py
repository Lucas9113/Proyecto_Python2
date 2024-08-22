"Escript que convierte el archivo de texto en audio usando la libreria pyttsx3"

import pyttsx3

# Abrimos arichivo de texto

with open(r'book.txt') as texto:
    texto = texto.read()



# inicializamos la biblioteca
engine = pyttsx3.init()

# Configuramos los parametros de voz y velocidad y volumen
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

rate = engine.setProperty('rate', 120 )

volumen = engine.setProperty('volumen', 1.0)

# Le pasamos el que anteriromente abrimos para que lo reproduzca.

engine.say(texto)


engine.runAndWait()