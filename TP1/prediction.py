import re
from collections import OrderedDict
import numpy as np
import entrainement as ent

class Prediction:
    def __init__(self, matrice, dictionnaire, mots, nbrSynonyme):
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
        dictionnairePrediction = {}
        dictionnairePrediction.update(self.dictionnaire)
        for i, item in self.dictionnaire.items():
            if i == self.motsCherche:
                #on met la valeur du mot que l'on cherhe a 0 puisqu'il ne nous interesse pas
                dictionnairePrediction[i] = 0
            else:
                dictionnairePrediction[i] = matrice[item]

        ##chat GPT
        sorted_d = sorted(dictionnairePrediction.items(), key=lambda x: x[1], reverse=True)

        self.afficherPrediction(sorted_d, nbreSynonymes)

    def moindreCarre(self, nbreSynonymes):

        matriceMot = self.matrice[self.dictionnaire[self.motsCherche]]
        m = (matriceMot - self.matrice) ** 2
        sums = m.sum(axis=1)
        dictionnairePrediction = {}
        dictionnairePrediction.update(self.dictionnaire)
        for i, item in self.dictionnaire.items():
            if i == self.motsCherche:
                #on met la valeur du mot que l'on cherhe a 0 puisqu'il ne nous interesse pas
                dictionnairePrediction[i] = 1000
            else:
                dictionnairePrediction[i] = sums[item]

        sorted_d = sorted(dictionnairePrediction.items(), key=lambda x: x[1])

        self.afficherPrediction(sorted_d, nbreSynonymes)


    def manhattan(self, nbreSynonymes):
        matriceMot = self.matrice[self.dictionnaire[self.motsCherche]]
        m = abs(matriceMot - self.matrice)
        sums = m.sum(axis=1)
        dictionnairePrediction = {}
        dictionnairePrediction.update(self.dictionnaire)
        for i, item in self.dictionnaire.items():
            if i == self.motsCherche:
                # on met la valeur du mot que l'on cherhe a 0 puisqu'il ne nous interesse pas
                dictionnairePrediction[i] = 1000
            else:
                dictionnairePrediction[i] = sums[item]

        sorted_d = sorted(dictionnairePrediction.items(), key=lambda x: x[1])

        print("debug")
        print(self.dictionnaire)

        self.afficherPrediction(sorted_d, nbreSynonymes)

def main():
    matrice, dict = ent.main()
    prediction = Prediction(matrice, dict, "belle", 2)
    #prediction.moindreCarre()
    prediction.manhattan()



if __name__ == '__main__':
    quit(main())


