colores=[ ]
n=input (" el color ingresado es: ")
cant=0
m= "end"
while n!=m:
  #print (n)
  colores.append(n)
  n=input (" el color ingresado es: ")
  cant+=1
print(colores)
#for i in range(cant):
#  if i % 2 ==1:
 #   print ( colores[i]);

#if cant==1 or cant==3 or cant==5 or cant==7 or cant==9:
 # guardar=n
#cant+=1
 # for i in cant:
  #  print (guardar)      
i=1
while i < cant:
  print (colores[i])
  i+=2