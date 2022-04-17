from operator import truediv
import random
from webbrowser import Galeon
numero_aleatorio= random.randrange(5)
gana= False
print("tenes 3 intentos para adivinar entre 0 y 5")
intento=1

while (intento<=5) and not gana:
         ingresado=int(input('Ingrese un numero'))
         if( ingresado== numero_aleatorio):
            gana=True
         else:
            print('Mmmm ... No.. ese número no es... Seguí intentando.') 
            intento+=1
if not gana:
   print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))

