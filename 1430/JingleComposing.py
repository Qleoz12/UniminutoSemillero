from sys import stdin
notes_score = {
	'W': 1.0,
	'H': 0.5,
	'Q': 0.25,
	'E': 0.125,
	'S': 0.0625,
    'T': 0.03125,
    'X': 0.01562,
}
inp = stdin
jingleLine=inp.readline().strip().split("/")
counterAmount=0
counterGeneral=0
for sublist in jingleLine:
    counterAmount=0
    for value in sublist:
        counterAmount+=notes_score[value]
    if counterAmount==1 : counterGeneral+=1  
print(counterGeneral)
