dias=input ("ingrese los dias:")
a=int(dias)
horas=input ("ingrese las horas:")
b=int(horas)
minutos=input ("ingrese los minutos:")
c=int(minutos)
seg= a*60+60*60*b+60*60*60*c
print("para",dias,",",horas,"horas","y",minutos,seg,"segundos")