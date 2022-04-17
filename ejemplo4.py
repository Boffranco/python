from functools import reduce 

#cadena = ["a", "e", "i"]
#vocales = reduce((lambda x, y: x + y), cadena)
#print(vocales)
#print(cadena)
#producto = reduce((lambda x, y: x * y), [1, 2, 3, 4])
#print(producto)

def my_add(a, b):
  result = a + b
  print(f"{a} + {b} = {result}")
  return result

#print(my_add(5, 5))
numbers = [0, 1, 2, 3, 4]
#reduce(my_add, numbers)

#def uno():
#    print("uno")
#    print(f"El nombre de este módulo es {__name__}")

#if __name__ == "__main__":
#    uno()

#import json
#archivo = open("bandas.txt", "w")
#datos = [{"nombre": "William Campbell", "ciudad": "La Plata", "ref": "www.instagram.com/williamcampbellok"},{"nombre": "Buendia", "ciudad": "La Plata", "ref":"https://buendia.bandcamp.com/"},
#{"nombre": "Lúmine", "ciudad": "La Plata", "ref": "https://www.instagram.com/luminelp/"} ]
#print(json.dump(datos, archivo))
#archivo.close()

import csv
import json
ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "teorias", "ejemplos","clase4",␣
↪"netflix_titles.csv")

archivo = open(ruta_archivo, "r")
csvreader = csv.reader(archivo, delimiter=',')
#encabezado = csvreader.__next__()
encabezado = next(csvreader)
print(encabezado)
for linea in csvreader:
     if linea[1] == "TV Show" and linea[5] == "Argentina":
         print(f"{linea[2]:<40} {linea[3]}")
archivo.close()
