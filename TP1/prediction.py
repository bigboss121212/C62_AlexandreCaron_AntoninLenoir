import re
import numpy as np


class Prediction:
    def __init__(self, methode, matrice, dictionnaire, mots, nbrSynonyme):
        self.methode = methode
        self.matrice = matrice
        self.dictionnaire = dictionnaire
        self.motsCherche = mots
        self.nbrSynonyme = nbrSynonyme


    def produitScalaire(self):

        matrice = self.matrice * self.matrice[self.dictionnaire[self.motsCherche]]
        sums = matrice.sum(axis=1)

        ##pas sur
        for i in self.dictionnaire:
            self.dictionnaire[i] = sums[i]

        ##chat GPT
        sorted_d = sorted(self.dictionnaire.items(), key=lambda x: x[1])

        ##pour retourner seulement le nbr de sysnonyme demande
        d = {}
        for i in range(self.nbrSynonyme):
            d.update({self.nbrSynonyme[i] : self.nbrSynonyme[i]})



    def moindreCarre(self):
        pass

    def manhattan(self):
        pass

def main():


    pass

if __name__ == '__main__':
    quit(main())


