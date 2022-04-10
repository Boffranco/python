#Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha
#letra. En caso que no se haya ingresado una letra, indique el error.

from collections import Counter
with open("readme.txt", "r") as text:
    words = set(text.read().lower().split())
    myChar = input("Escriba una letra...: ")
    if (myChar.isalpha()):
        for w in words:
            if w.startswith(myChar):
                print(w)
    else:
        print('no has ingresado ninguna letra')