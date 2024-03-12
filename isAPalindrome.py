def es_Palindromo(palabra):
    return palabra == palabra[::-1]

palabras = []
for i in range(5):
    palabra = input(f"Ingrese la palabra #{i + 1}: ")
    palabras.append(palabra.lower()) 

palindromos = []
no_Palindromos = []
for palabra in palabras:
    if es_Palindromo(palabra):
        palindromos.append(palabra)
    else:
        no_Palindromos.append(palabra)

print("\nPalíndromos:")
for palindromos in palindromos:
    print(palindromos)

print("\nNo palíndromos:")
for no_Palindromos in no_Palindromos:
    print(no_Palindromos)