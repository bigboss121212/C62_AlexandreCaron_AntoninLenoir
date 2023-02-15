from sys import argv
import re
import numpy as np
from time import time

class Entrainement:
    def __init__(self, fenetre, chemin, encodage = 'utf-8'):
        self.chemin = chemin
        self.encodage = encodage
        self.text = tuple
        self.matrice = None
        self.dictionnaire = None
        self.new_list = []
        self.file_path = r"X:\Session6\Donnees, Megadonnees, Intelligence Artificielle\semaine2\test.txt"
        self.fenetre = fenetre
        self.lire(self.chemin)
        self.construireDictio(self.text)

    def lire(self, chemin):
        f = open(chemin, 'r', encoding=self.encodage)
        text = f.read()
        f.close()
        self.text = re.findall('\w+', text)
        return self.text

    def compter_mots(self):
        return len(re.findall('\w+', self.text))

    def construireDictio(self, texte):
        self.dictionnaire = {}

        index = 0
        for mot in texte:
            #pour enlever les doublons
            if mot not in self.dictionnaire:
                self.dictionnaire[mot] = index
                index += 1


    def remplir_matrice(self):
        t = time()

        self.matrice = np.zeros((len(self.dictionnaire), len(self.dictionnaire)))

        for i, mot in enumerate(self.text):
            for j in range(1, self.fenetre // 2 + 1):
                if i + j < len(self.text):
                    self.matrice[self.dictionnaire[self.text[i]], self.dictionnaire[self.text[i + j]]] += 1
                if i - j >= 0:
                    self.matrice[self.dictionnaire[self.text[i]], self.dictionnaire[self.text[i - j]]] += 1

        print(f"temps Construire DICO :  {time() - t}")
        return self.matrice, self.dictionnaire


def main():
    pass

if __name__ == '__main__':
    quit(main())