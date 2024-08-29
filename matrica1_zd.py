'''
Zadatak 1
Napisati program koji generira kvadratnu matricu dimenzija 5x5.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na glavnoj dijagonali
matrice(glavna dijagonala ide od gornjeg lijevog u donji desni kut matrice).
'''

import random

r = 5
s = 5
zbroj = 0

matrica = []

for i in range(r):
    red = [0]* s
    matrica.append(red)
    for j in range(s):
        nasumicni_br = random.randint(1,10)
        matrica[i][j] = nasumicni_br
        
for i in matrica:
    print(i)

for i in range(len(matrica)):
    zbroj += matrica[i][i]

print("Zbroj:", zbroj)
