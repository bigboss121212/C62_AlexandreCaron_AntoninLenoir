from sys import argv
import re
import numpy as np
import entrainement as ent
import prediction as pre


#class Main:
   # def __init__(self):
       # pass


def main():
    enc = argv[1]
    chemin = argv[2]
    motListes = []

    entrainement = ent.Entrainement(chemin, enc)
    matrice, dictio = entrainement.remplir_matrice()

    while True:
        mots = input("Entrez un mot, le nombre de synonymes que vous voulez et la methode de calcul, i.e produit scalaire: 0, least-square: 1, city-block: 2 \n\nTapper q pour quitter\n").split(' ')
        if mots == "q":
            break
        else:
            motListes.append(mots)

            if len(motListes[0][0:]) == 3:
                motListes[0]
                prediction = pre.Prediction(matrice, dictio, motListes[0][0], motListes[0][1])
                if motListes[0][2] == "0":
                    prediction.produitScalaire()
                if motListes[0][2] == "1":
                    prediction.moindreCarre()
                if motListes[0][2] == "2":
                    prediction.manhattan()

    #question = input("Entrez un mot, le nombre de synonymes que vous voulez et la methode de calcul, i.e produit scalaire: 0, least-square: 1, city-block: 2 \n \n Tapper q pour quitter")

    print(motListes)



if __name__ == '__main__':
    quit(main())