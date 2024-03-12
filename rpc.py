import random

def juego(user):
    opccion = ["piedra", "papel", "tijeras"]
    pc = random.choice(opccion)
    print("Tu elección:", user)
    print("Elección de la computadora:", pc)
    if user == pc:
        print("¡Empate!")
    elif (user == "piedra" and pc == "tijeras") or \
         (user == "papel" and pc == "piedra") or \
         (user == "tijeras" and pc == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
        
user = input("Elige piedra, papel o tijeras: ").lower()
if user in ["piedra", "papel", "tijeras"]:
    juego(user)