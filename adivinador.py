from operator import truediv
import random
numero_aleatorio= random.randrange(100)
gane= False
print("tenes 5 oportunidades para adivinar el numero")
intento= 1
while( intento <6) and (not gane):
     numero_ingresado=int(input('ingresa tu numero'))
     if( numero_ingresado==numero_aleatorio):
         print('ganaste y necesitas {} intentos!!!'.format(intento))
         gane:True
     else:
         print('ese numero no es segui intentado')
         intento+=1
if(not gane):
    print('\n perdiste:(\ el numero era: {}' .format(numero_aleatorio) )

         