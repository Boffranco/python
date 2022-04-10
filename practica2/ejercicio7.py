from http.client import OK


palabra = input('ingrese una palabra: ')
repetidos = set()
metodo1=False
if(metodo1):
    for c in range(len(palabra)):
        char= palabra[c]
        if(palabra.find(char,c+1)>= 1 ):
            #print('la palabra no es un heterograma')
            repetidos.add(char)
    print (repetidos)        
    if(repetidos ==set()):
        print('la palabra es un heterograma')
    else:
        print('la palabra no es un heterograma')    

else:
#version2
    encontre= False
    for c in palabra:
        if(c not in repetidos):
            repetidos.add(c) 
        else:
            print('la palabra no se un heterograma')
            encontre=True
            break
    if(not encontre):
        print('la palabra es un hetorograma')