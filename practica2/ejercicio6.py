
from keyword import iskeyword
from re import S


frase = """ Nono no no si si la casa kassadin casa la"""
#pa =  frase.lower().split()
#pal_sd =list(set(pa))
#print(pa)
#print(pa - pal_sd)
#print(palabras)

s= set()
repetidos= set()
for c in frase.split():
    if(c in s):
       repetidos.add(c)
    if (c.islower()):   
       s.add(c)
print(s-repetidos)        
 