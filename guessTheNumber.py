
import random

numero = random.randrange(1,50)
pregunta = int(input("Adivinna un numero entre 1 - 50:  "))

while pregunta != numero:
    if (pregunta < numero):
        print("Elije un numero mas alto. Intentalo otra vez")
        pregunta = int(input("\nAdivina un numero entre 1 - 50:  "))
    else:
        print("Elije un numero mas bajo. Intentalo otra vez")
        pregunta = int(input("\nAdivina un numero entre 1 - 50:  "))
print("Adivinaste el numero")