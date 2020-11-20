lscoreA = []
lscoreB = []
lscore = []

x=[0,0]
klubA= input('Klub A : ')
klubB= input('Klub B : ')

n=1
scoreA = 0
scoreB = 0

score=input(f'Pertandingan {n} : ').split()
while scoreA >= 0 and scoreB >= 0:
    lscore.append(score)
    lscoreA.append(scoreA)
    lscoreB.append(scoreB)
    n+=1
    score=list(map(int,input(f'Pertandingan {n} : ').split()))
    scoreA = (score[0])

    scoreB = (score[1])

for i in range(len(lscore)):
    if lscore[i][0]>lscore[i][1]:
        hasil= klubA
    elif lscore[i][0]<lscore[i][1]:
        hasil= klubB
    else:
        hasil= 'Draw'
        
    print(f'Hasil {i+1} :',hasil)

print('Pertandingan selesai')
