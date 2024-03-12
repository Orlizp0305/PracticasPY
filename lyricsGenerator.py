import lyrics

cancion = {
    "Natanael Cano - O mevoy o te vas": lyrics.o_me_voy_o_te_vas,
    "Natanael Cano - Amor tumbado": lyrics.amor_Tumbado_letra,
    "Natanael Cano - Mi bello angel": lyrics.mi_Bello_Angel,
    "Natanael Cano - Morritas": lyrics.morritas,
    "Natanael Cano- Diamantes": lyrics.diamantes,
    "Natanael Cano- Brillo": lyrics.brillo,
    "Natanael Cano - Gracias": lyrics.gracias,
    "Natanael Cano - Carnal": lyrics.carnal,
    "Natanael Cano - Ella!": lyrics.ella,
    "Natanael Cano - PCR": lyrics.pcr,  
}

print("Lista de canciones:")
for i, can in enumerate(cancion, 1):
    print(f"{i}. {can}")

opc = int(input("Elige una canción (1-10): "))

if opc < 1 or opc > 10:
    print("Opción inválida")
else:
  cancionT = list(cancion.keys())[opc-1]
  cancionL = cancion[cancionT]
    
  print(f"\nElejiste: '{cancionT}' Aqui tienes. \n  {cancionT} \n{cancionL}")