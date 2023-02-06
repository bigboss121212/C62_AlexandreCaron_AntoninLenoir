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
        matrice


        #sums = matrice.sum(axis=1)

        ##pas sur
        for i, item in self.dictionnaire.items():
            if i == self.motsCherche:
                #on met la valeur du mot que l'on cherhe a 0 puisqu'il ne nous interesse pas
                self.dictionnaire[i] = 0
            else:
                self.dictionnaire[i] = matrice[item]


        ##chat GPT
        sorted_d = sorted(self.dictionnaire.items(), key=lambda x: x[1], reverse=True)
        sorted_d

        ##pour retourner seulement le nbr de sysnonyme demande
        d = {}
  #      for i in range(self.nbrSynonyme):
 #           d.update({self.nbrSynonyme[i] : self.nbrSynonyme[i]})



    def moindreCarre(self):
        pass

    def manhattan(self):
        pass

def main():
    matrice, dict = ent.main()
    prediction = Prediction(matrice, dict, "allo", 2)
    prediction.produitScalaire()


    pass

if __name__ == '__main__':
    quit(main())


