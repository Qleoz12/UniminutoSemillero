from fraction import fraction
from mathFractions import mathFractions


my_objects = []

fr=fraction(1,2)
fr2=fraction(2,4)
teacher= mathFractions()
teacher.sumar_fracciones(fr,fr2)


'''numeroOperaciones = int(input())
for i in range(numeroOperaciones):
   operation=input()
   data = operation.split()
   fr=fraction(data[0],data[2])
   fr2=fraction(data[4],data[6])

   
   my_objects.append(fr)
   my_objects.append(fr2)
'''

print(len(my_objects))
