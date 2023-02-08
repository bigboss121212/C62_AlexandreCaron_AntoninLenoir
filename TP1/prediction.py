import re
from collections import OrderedDict
import numpy as np
import entrainement as ent

class Prediction:
    def __init__(self, matrice, dictionnaire, mots, nbrSynonyme, stopWords):
        self.matrice = matrice
        self.dictionnaire = dictionnaire
        self.motsCherche = mots
        self.nbrSynonyme = nbrSynonyme
        self.stopWords = stopWords

    def afficherPrediction(self, dict, nbreSyno, stopWords):
        filtered_dict = {}
        for k, v in dict:
            if k not in stopWords:
                filtered_dict[k] = v
        for i, (j, items) in enumerate(filtered_dict.items()):
            if i >= int(nbreSyno):
                break
            print(f'{j} -->  {items}')

    def produitScalaire(self):
        matriceMot = self.matrice[self.dictionnaire[self.motsCherche]]
        matrice = np.dot(self.matrice, matriceMot)
        dictionnairePrediction = {}
        dictionnairePrediction.update(self.dictionnaire)

        for i, item in self.dictionnaire.items():
            if i != self.motsCherche:
                dictionnairePrediction[i] = matrice[item]

        ##chat GPT
        sorted_d = sorted(dictionnairePrediction.items(), key=lambda x: x[1], reverse=True)

        self.afficherPrediction(sorted_d, self.nbrSynonyme, self.stopWords)

    def moindreCarre(self):

        matriceMot = self.matrice[self.dictionnaire[self.motsCherche]]
        m = (matriceMot - self.matrice) ** 2
        sums = m.sum(axis=1)
        dictionnairePrediction = {}
        dictionnairePrediction.update(self.dictionnaire)
        for i, item in self.dictionnaire.items():
            if i != self.motsCherche:
                dictionnairePrediction[i] = sums[item]

        sorted_d = sorted(dictionnairePrediction.items(), key=lambda x: x[1])

        self.afficherPrediction(sorted_d, self.nbrSynonyme, self.stopWords)


    def manhattan(self):
        matriceMot = self.matrice[self.dictionnaire[self.motsCherche]]
        m = abs(matriceMot - self.matrice)
        sums = m.sum(axis=1)
        dictionnairePrediction = {}
        dictionnairePrediction.update(self.dictionnaire)
        for i, item in self.dictionnaire.items():
            if i != self.motsCherche:
                dictionnairePrediction[i] = sums[item]

        sorted_d = sorted(dictionnairePrediction.items(), key=lambda x: x[1])

        self.afficherPrediction(sorted_d, self.nbrSynonyme, self.stopWords)

def main():
    pass



if __name__ == '__main__':
    quit(main())


