import sys 
categoriesNum=4
inp = sys.stdin
categories={ 1:0, 2:0, 3:0, 4:0}
triedyears=int(inp.readline().strip())
palpitates=[]
vencedores=[]

for year in range(triedyears):
	inp.readline().strip()
	for x in range(categoriesNum):
		palpitates.append(inp.readline().strip())
	inp.readline().strip()
	for x in range(categoriesNum):
		vencedores.append(inp.readline().strip())

for x in range(len(palpitates)):
	if  palpitates[x]==vencedores[x]:
		categories.pop((x%4)+1, None)

keys=categories.keys()
print(*keys, sep=' ', end='\n', file=sys.stdout, flush=False)

	
		



