diciplineProblems = []
lifeProblems = []
matrixSize = []

lifeletter="V"
matrixSize = input().split()
for i in range(int(matrixSize[0])):
    row=input().split()
    for r in row:
        lifeProblems.append(r) if lifeletter in r else diciplineProblems.append(r) 

lifeProblems.sort(reverse=True)
diciplineProblems.sort(reverse=True)
lifeProblems.extend(diciplineProblems)

for x in lifeProblems:
    print(x)