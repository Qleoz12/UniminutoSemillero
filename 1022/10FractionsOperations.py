from fraction import fraction
from mathFractions import mathFractions


my_objects = []

'captura de numero de iteraciones'
numeroOperaciones = int(input())
for i in range(numeroOperaciones):
   'camptura de cada renglon de par de fracciones'
   operation=input()
   'se divide cada renglon por espacios'
   data = operation.split()
   'se arman fracciones'
   fr=fraction(int(data[0]),int(data[2]))
   fr2=fraction(int(data[4]),int(data[6]))
   'custom Objetc'
   teacher= mathFractions(data[3],fr,fr2)
   'add current instance'
   my_objects.append(teacher)

for i in range(numeroOperaciones):
   my_objects[i].result()