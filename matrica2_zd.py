'''
Zadatak 2
Napisati program koji generira kvadratnu matricu dimenzija 7x7.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na rubovima matrice.

'''
import random

r = 7
s = 7
zbroj = 0

matrica = []

for i in range(r):
    red = [0]* s
    matrica.append(red)
    for j in range(s):
        nasumicni_br = random.randint(1,10)
        matrica[i][j] = nasumicni_br

duljina = len(matrica)
for i in range(duljina):
    zbroj += matrica[0][i]  
    zbroj += matrica[duljina-1][i] 
    if i != 0 and i != duljina - 1:
        zbroj += matrica[i][0] 
        zbroj += matrica[i][duljina-1]

for i in matrica:
    print(i)

print("Zbroj elemenata na rubovima:", zbroj)
