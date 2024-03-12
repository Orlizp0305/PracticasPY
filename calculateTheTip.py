cuenta = float(input("¿Cuánto es la cuenta? "))
propina = input("¿Cuánto vamos a dejar de propina?\n 1) 18%\n 2) 20%\n 3) 25%\n")

if propina == '1':
    porcentaje = 0.18
elif propina == '2':
    porcentaje = 0.20
elif propina == '3':
    porcentaje = 0.25
else:
    print("Eligue una opcion valida")
    exit()  

propinaC = cuenta * porcentaje
totalF=propinaC+cuenta

print("El total a pagar es de", totalF,"Con propina del:",porcentaje,"%","Su cuenta sin propina es de ",cuenta)