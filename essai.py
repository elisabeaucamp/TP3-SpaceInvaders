liste = [[1,2,3],[4,5,6],[7,8,9]]

for j,k in enumerate (liste) :
    longueur = len(k)
    mot = liste[j][longueur-1]
    print(mot)