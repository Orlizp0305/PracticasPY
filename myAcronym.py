def creaA(frase):
    palabras = frase.split()
    acronimo = ""
    for palabra in palabras:
        
        acronimo += palabra[0].upper()
    return acronimo

frase = input("Ingresa una frase: ")
acr = creaA(frase)
print("El acrónimo es:", acr)