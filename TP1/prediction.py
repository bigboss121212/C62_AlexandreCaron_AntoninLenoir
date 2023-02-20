import numpy as np
from time import time

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
        print("")


    def produitGeneral(self, param):
        t = time()
        matriceMot = self.matrice[self.dictionnaire[self.motsCherche]]

        if param == 1:
            matrice = np.dot(self.matrice, matriceMot)
        if param == 2:
            matrice = np.sum(np.square(matriceMot - self.matrice), axis=1)
        if param == 3:
            matrice = sum(abs(val1 - val2) for val1, val2 in zip(matriceMot, self.matrice))


        dictionnairePrediction = {}
        dictionnairePrediction.update(self.dictionnaire)

        for i, item in self.dictionnaire.items():
            if i != self.motsCherche:
                dictionnairePrediction[i] = matrice[item]

        ##chat GPT
        dictionnairePrediction.pop(self.motsCherche)
        sorted_d = sorted(dictionnairePrediction.items(), key=lambda x: x[1], reverse=True)

        self.afficherPrediction(sorted_d, self.nbrSynonyme, self.stopWords)
        print(f"temps Construire produitScalaire :  {time() - t}")

def main():
    pass



if __name__ == '__main__':
    quit(main())


