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

    print(argv[1])

    entrainement = ent.Entrainement(chemin, enc)
    matrice, dictio = entrainement.remplir_matrice()

    while True:
        mots = input("Entrez un mot, le nombre de synonymes que vous voulez et la methode de calcul, i.e produit scalaire: 0, least-square: 1, city-block: 2 \n\nTapper q pour quitter\n").split(' ')
        if mots == "q":
            break
        else:
            print(mots)
            motListes.append(mots)

            if len(mots) == 3:
                motListes[0]
                print("debug")
                print(dictio)
                prediction = pre.Prediction(matrice, dictio, mots[0], mots[1])
                if mots[2] == "0":
                    prediction.produitScalaire(mots[1])
                if mots[2] == "1":
                    prediction.moindreCarre(mots[1])
                if mots[2] == "2":
                    prediction.manhattan(mots[1])

    #question = input("Entrez un mot, le nombre de synonymes que vous voulez et la methode de calcul, i.e produit scalaire: 0, least-square: 1, city-block: 2 \n \n Tapper q pour quitter")

    print(motListes)



if __name__ == '__main__':
    quit(main())