import sys 
notes_score = {
	'W': 1.0,
	'H': 0.5,
	'Q': 0.25,
	'E': 0.125,
	'S': 0.0625,
    'T': 0.03125,
    'X': 0.015625,
}
inp = sys.stdin
while True:
    jingleLine=inp.readline().split("/")
    counterAmount=0
    counterGeneral=0
    if len(jingleLine)>2:
        del jingleLine[-1]
        del jingleLine[0]
    for sublist in jingleLine:
        counterAmount=0
        for value in sublist:
            if value in notes_score:
                counterAmount+=notes_score[value]
            else:
                sys.exit()
        if counterAmount==1 : counterGeneral+=1  
    print(counterGeneral)
