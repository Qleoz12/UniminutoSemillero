
MAX = 25010
diciplineProblems = []
lifeProblems = []
matrixSize = []

lifeletter="V"
matrixSize = input().split()
for i in range(int(matrixSize[0])):
    row=input().split()
    for r in row:
        if r in lifeletter:
            lifeProblems.append(r)
        else:
            diciplineProblems.append(r)

lifeProblems.sort(reverse=True)
for j in lifeProblems:
    print(j)
print("1\n")
diciplineProblems.sort(reverse=True)
for i in diciplineProblems:
    print(i)
print("2\n")
lifeProblems.extend(diciplineProblems)

for x in lifeProblems:
    print(x)
