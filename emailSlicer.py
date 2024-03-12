correo = input("ingresa tu correo electronico:  ").strip()
usuario= correo[:correo.index('@')]
dominio = correo[correo.index('@')+1:]
if dominio == "gmail.com":
    dom = "tu dominio es de google"
elif dominio == "yahoo.com":
    dom = "tu dominio es de yahoo"
elif dominio == "hotmail.com":
    dom = "tu dominio es de microsoft"
else:
    dom = "tu dominio es perzonalizado"
resultado = "Tu nombre de ususario es: "+usuario+"\nTu dominio es: "+dominio+" "+dom
print(resultado)