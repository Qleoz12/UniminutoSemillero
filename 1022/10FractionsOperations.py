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
   fr=fraction(data[0],data[2])
   fr2=fraction(data[4],data[6])
   'custom Objetc'
   teacher= mathFractions(data[3],fr,fr2)
   'add current instance'
   my_objects.append(teacher)

for i in range(numeroOperaciones):
   my_objects[i].determinate_operation()
   print(my_objects[i].__dict__)