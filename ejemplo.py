#cadena = "Python "
#otra_cadena = "es lo más!"
#print(cadena + otra_cadena)
#print(cadena * 5)
#print(len(cadena))

#palabra = input("Ingresá una palabra")
#if "a" in palabra:
#      print("Hay letras a")
#else:
#      print("No hay letras a ")

#for i in range(3, 14, 3):
#     print(i)

#intento = 3
#print( 'Hola {} !!! Ganaste! y necesitaste {} intentos!!!'.format("claudia", intento))
     
#intento = 3
#nombre = "claudia"
#print(f'Hola {nombre} !!! Ganaste! y necesitaste {intento} intentos!!!')
#x = 4
#print(f"{x:2d} {x*x:3d} {x*x*x:4d}")

#cad1 = "Cadena alineada a izquierda"
#cad2 = "Cadena alineada a derecha"
#cad3 = "Cadena centrada"
#print(f"\n{cad1:<30}\n{cad2:>30}")
#print(f"\n{cad3:^30}")
#print(f"\n{cad3:*^30}")

#for i in range(4):
#   cadena = input("Ingresá una palabra")
#   if "r" in cadena:
#     print(f"{cadena} tiene una letra r")

#x = int(input("Ingresá un número "))
#y = int(input("Ingresá un número "))
#maximo = x if x > y else y
#maximo
#print(maximo)  

#x = 1
#y = 0
#if True or x/y:
#     print("No hay error!!!!")

#varios = [1, "dos", [3, "cuatro"], True]
#print(len(varios))

#varios = [ 17, "hola", [1, "dos"], 5.5, True]
#print(varios[0])
#print(varios[2][1] )
#print(varios[-3])

#vocales = [ "a", "e","i", "o", "u"]
#print(vocales[1:5] )
#for indice in range(len(vocales)):
#    print(vocales[indice])
#print( vocales[ :2] )
#print( vocales[2:] )

#rock = ["Riff", "La Renga", "La Torre"]
#blues = ["La Mississippi", "Memphis"]
#musica = rock
#print(musica)
#otra_musica = rock[:]
#print(otra_musica)
#print(id(rock))
#print(id(otra_musica))
#print(id(musica))

#rock = ["Riff", "La Renga", "La Torre"]
#blues =["La Mississippi", "Memphis"]
#musica = rock + blues
#mas_rock = rock * 3
#print(musica)
#print(mas_rock)

#lista = [[1,2]] * 3
#print(lista)
#lista [0][1] = 'cambio'
#print(lista)

#lista = [[1,2], 8, 9]
#lista2 = lista.copy()
#print(id(lista), id(lista2))

#palabras = "En esta clase aparecen grandes músicos".split("a")
#print(palabras)

#tupla = (1, 2)
#print(len(tupla))

#tupla = (1, 2, 3, "hola")
#print(tupla[1:4])
#nueva_tupla = ("nueva",) + tupla[1:3]
#print(nueva_tupla)

#meses = {"enero": 31, "febrero": 28, "marzo": 31}
#print(meses)
#meses["febrero"] = 29
#meses["abril"] = 30
#print(meses)

#musica = {"rock": ["Riff", "La Renga", "La Torre"],"blues": ["La Mississippi", "Memphis", "violeta"]}
#for elem in musica:
#   print(elem)
#print("*" * 10)
# los valores
#for elem in musica:
#    print(musica[elem])

#claves = musica.keys()
#valores = musica.values()
#items = musica.items()
#print(claves)
#claves

#musica = {"rock": ["Riff", "La Renga", "La Torre"],
#"blues": ["La Mississippi", "Memphis", "violeta"]}
#"rock" in musica
#print(musica)

def ingreso_notas():

   nombre = input("Ingresa un nombre (<FIN> para finalizar) ")
   dicci = {}
   while nombre != "FIN":
         nota = int(input(f"Ingresa la nota de {nombre} "))
         dicci[nombre] = nota
         nombre = input("Ingresa un nombre (<FIN> para finalizar) ")
   return dicci
notas_de_estudiantes = ingreso_notas()
print(notas_de_estudiantes)
