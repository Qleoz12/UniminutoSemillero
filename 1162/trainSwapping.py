import SortAlgorithms

lengvagons=50
vagon = [None]*50
vagonStore = [None]*50

'cases'
numeroOperaciones = int(input())
for i in range(numeroOperaciones):
    'captura de tamaño del tren'
    lengvagons=int(input())
    vagon=[int(x) for x in input().split()]
    vagonStore[i]=vagon

for i in range(numeroOperaciones):
    print("Optimal train swapping takes {} swaps.".format(SortAlgorithms.bubble_sort(vagonStore[i])))