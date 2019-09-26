import SortAlgorithms

lines_input = []

'catch the numberof ines to input'
numeroOperaciones = int(input())
for i in range(numeroOperaciones):
    'captura de cada renglon de par de fracciones'
    operation=input()
    lines_input.append(operation)

for i in range(numeroOperaciones):
    SortAlgorithms.bubble_sort(lines_input[i].split())