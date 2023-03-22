from sys import argv
import re
import numpy as np
from time import time
import DAO

class Entrainement:
    def __init__(self, fenetre, chemin, encodage = 'utf-8'):
        self.chemin = chemin
        self.encodage = encodage
        self.text = tuple
        self.matrice = None
        self.dictionnaire = None
        self.new_list = []
        # self.file_path = r"X:\Session6\Donnees, Megadonnees, Intelligence Artificielle\semaine2\test.txt"
        self.fenetre = fenetre
        self.lire(self.chemin)
        self.construireDictio(self.text)

    def lire(self, chemin):
        f = open(chemin, 'r', encoding=self.encodage)
        text = f.read().lower()
        f.close()
        self.text = re.findall('\w+', text)
        return self.text

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

        # print(f"temps Construire DICO :  {time() - t}")
        return self.matrice, self.dictionnaire

class EntrainementDB(Entrainement):
    def __init__(self, fenetre, chemin, encodage='utf-8'):
        self.dao = DAO.Dao()
        super().__init__(fenetre, chemin, encodage)

    def insereStopWord(self, stopWord):
        index = 0
        for mot in stopWord:
            self.dao.insert_stop_words(index, mot)
            index += 1

    def construireDictio(self, texte):
        self.dictionnaire = {}
        data = []
        list = self.dao.fetch_all_unique_words()
        index = 0

        for mot in list:
            self.dictionnaire[mot[1]] = mot[0]
            index += 1

        for mot in texte:
            # if mot not in list and mot not in self.dictionnaire:
            # pour enlever les doublons
            if mot not in self.dictionnaire:
                self.dictionnaire[mot] = len(self.dictionnaire)
                data.append((len(self.dictionnaire) -1, mot))

        self.dao.inserer_datas(data)

    def remplir_matrice(self):
        data = []
        self.matrice = np.zeros((len(self.dictionnaire), len(self.dictionnaire)))
        list = self.dao.fetch_coocurrence()

        for y in list:
            ## mettre condition que la fenetre soit la mm que la notre
            if str(y[3]) == self.fenetre:
                self.matrice[y[0] - 1][y[1] - 1] = y[2]

        #self.dao.delete_table_coocurrence()

        for i, mot in enumerate(self.text):
            for j in range(1, int(self.fenetre) // 2 + 1):
                if i + j < len(self.text):
                    self.matrice[self.dictionnaire[self.text[i]], self.dictionnaire[self.text[i + j]]] += 1
                if i - j >= 0:
                    self.matrice[self.dictionnaire[self.text[i]], self.dictionnaire[self.text[i - j]]] += 1

        matrice = np.argwhere(self.matrice > 0)
        for x, y in matrice:
            freq = int(self.matrice[x,y])
            data.append((int(x), int(y), int(self.fenetre), freq))

        self.dao.insert_coocurrences(data)
        return self.matrice, self.dictionnaire
