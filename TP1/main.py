from sys import argv
import re
import numpy as np
import entrainement as ent


class Main:
    def __init__(self):
        pass


def main():
    enc = argv[1]
    chemin = argv[2]
    motListes = []


    while True:
        mots = input("Entrez un mot, le nombre de synonymes que vous voulez et la methode de calcul, i.e produit scalaire: 0, least-square: 1, city-block: 2 \n \n Tapper q pour quitter")
        if mots == "q":
            break
        else: motListes.append(mots)

    #question = input("Entrez un mot, le nombre de synonymes que vous voulez et la methode de calcul, i.e produit scalaire: 0, least-square: 1, city-block: 2 \n \n Tapper q pour quitter")

    print(motListes)



if __name__ == '__main__':
    quit(main())