bandera=True
while bandera==True:
    nom= input("Ingresa tu nombre:")
    if nom.isalpha():
        print("Contesta la siguiente pregunta","\n")
        bandera= False
    else:
        print("captura letras solamente")

fecha= input("Captura fecha de nacimiento")
dire= input("Captura tu direccion")
logro=input("Captura alguna meta que tengas")

print("-Nombre:",nom)
print("-Tu fecha es:",fecha)
print("-Tu direccion es:",dire)
print("-Tu meta enn la vida es ",logro)


