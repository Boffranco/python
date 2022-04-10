arch_nombre= open("nombres.txt", "r", encoding="utf-8")
arch_eval1= open("eval1.txt","r", encoding="utf-8")
arch_eval2= open("eval2.txt","r", encoding="utf-8")

nombres= arch_nombre.read().replace(',', "").replace('\'',"").split()
eval1= arch_eval1.read().replace(',', "").replace('\'',"").split()
eval2= arch_eval2.read().replace(',', "").replace('\'',"").split()

estudiantes=[]
total= 0

for i in range(0,len(nombres)):
     estudiante= {"nombre": nombres[i], "nota": int(eval1[i]) + int(eval2[i]) }
     estudiantes.append(estudiante)
     total+= estudiante["nota"]
#for n in nombre:
#    for nota1 in eval1:
#        for nota2 in eval2:
#            estudiante= {"nombre": nombre, "nota evaluacion 1 y evaluacion 2": int(nota1) + int(nota2) }
#            estudiantes.append(estudiante)
#            total+= estudiante["nota evaluacion 1 y evaluacion 2"]

#for nombre, nota1, nota2 in zip(nombres, eval1, eval2):
#      estudiante = {"nombre": nombre, "nota": int(nota1) + int(nota2)}
#      estudiantes.append(estudiante)
#      total += estudiante["nota"]

promedio= total  / len (estudiantes)
print(promedio)
#print(estudiantes)

menor_al_promedio=[]
for estudiante in  estudiantes:
     if(estudiante["nota"] < promedio):
           menor_al_promedio.append(estudiante["nombre"])      
print(menor_al_promedio)

arch_nombre.close()
arch_eval1.close()
arch_eval2.close()