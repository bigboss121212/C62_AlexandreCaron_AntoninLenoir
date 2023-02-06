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


    def afficherPrediction(self, dict, nbreSynonymes):

        index = 0
        for j, items in dict:
            if index < int(nbreSynonymes):
                print(f'{j} -->  {items}')
                index += 1

    def produitScalaire(self, nbreSynonymes):


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

        self.afficherPrediction(sorted_d, nbreSynonymes)




    def moindreCarre(self, nbreSynonymes):
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

        self.afficherPrediction(sorted_d, nbreSynonymes)


    def manhattan(self, nbreSynonymes):
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

        self.afficherPrediction(sorted_d, nbreSynonymes)


def main():
    matrice, dict = ent.main()
    prediction = Prediction(matrice, dict, "belle", 2)
    #prediction.moindreCarre()
    prediction.manhattan()


    pass

if __name__ == '__main__':
    quit(main())


