import re
from collections import OrderedDict

import numpy as np
import entrainement as ent


class Prediction:
    def __init__(self, matrice, dictionnaire, mots, nbrSynonyme):
        #self.methode = methode
        self.matrice = matrice
        self.dictionnaire = dictionnaire
        self.motsCherche = mots
        self.nbrSynonyme = nbrSynonyme


    def produitScalaire(self):


        matriceMot = self.matrice[self.dictionnaire[self.motsCherche]]

        matrice = np.dot(self.matrice, matriceMot)



        for i, item in self.dictionnaire.items():
            if i == self.motsCherche:
                #on met la valeur du mot que l'on cherhe a 0 puisqu'il ne nous interesse pas
                self.dictionnaire[i] = 0
            else:
                self.dictionnaire[i] = matrice[item]


        ##chat GPT
        sorted_d = sorted(self.dictionnaire.items(), key=lambda x: x[1], reverse=True)
        sorted_d


        print(sorted_d)


    def moindreCarre(self):
        matriceMot = self.matrice[self.dictionnaire[self.motsCherche]]


        m = (matriceMot - self.matrice) **2
        #m = np.linalg.norm(matriceMot - self.matrice) ** 2
        sums = m.sum(axis=1)
        sums


        for i, item in self.dictionnaire.items():
            if i == self.motsCherche:
                #on met la valeur du mot que l'on cherhe a 0 puisqu'il ne nous interesse pas
                self.dictionnaire[i] = 1000
            else:
                self.dictionnaire[i] = sums[item]

        sorted_d = sorted(self.dictionnaire.items(), key=lambda x: x[1])
        sorted_d


    def manhattan(self):
        matriceMot = self.matrice[self.dictionnaire[self.motsCherche]]

        m = abs(matriceMot - self.matrice)
        sums = m.sum(axis=1)
        sums

        for i, item in self.dictionnaire.items():
            if i == self.motsCherche:
                # on met la valeur du mot que l'on cherhe a 0 puisqu'il ne nous interesse pas
                self.dictionnaire[i] = 1000
            else:
                self.dictionnaire[i] = sums[item]

        sorted_d = sorted(self.dictionnaire.items(), key=lambda x: x[1])
        sorted_d


def main():
    matrice, dict = ent.main()
    prediction = Prediction(matrice, dict, "allo", 2)
    #prediction.moindreCarre()
    prediction.manhattan()


    pass

if __name__ == '__main__':
    quit(main())


