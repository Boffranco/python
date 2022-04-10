#from collections import Counter

frase= input("ingrese una frase: ").lower()
palabra= input("ingrese una palabra: ").lower()
print(frase.count(palabra))
#print(Counter(frase.split())[palabra])

# parte 2

cadena = input( """Ingresa la clave (debe tener menos de 10 caracteres y no contener los simbolos:@ y !):""")
print(len(cadena))
if len(cadena) > 10:
    print("Ingresaste mas de 10 caracteres")
else:
    if cadena.find("@") >=0  or cadena.find("!") >=0:
        print("Ingresaste alguno de estos simbolos: @ o !")
    else:
       print("Clave valida")


cadena = input( """Ingresa la clave (debe tener menos de 10 caracteres y no contener los simbolos:@ y !):""")
if len(cadena) > 10:
    print("Ingresaste mas de 10 caracteres")
else:
    if("@" in cadena) or ("!" in cadena):
        print("Ingresaste alguno de estos simbolos: @ o !")
    else:
        print("Clave valida")