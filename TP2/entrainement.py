import re
import numpy as np
import DAO

class Entrainement:
    def __init__(self, fenetre, chemin = None, encodage = 'utf-8'):
        self.chemin = chemin
        self.encodage = encodage
        self.text = tuple
        self.matrice = None
        self.dictionnaire = {}
        self.fenetre = fenetre

    def lire(self, chemin):
        f = open(chemin, 'r', encoding=self.encodage)
        text = f.read().lower()
        f.close()
        self.text = re.findall('\w+', text)
        return self.text

    def construireDictio(self):
        pass

    def remplir_matrice(self):
        pass

class EntrainementDB(Entrainement):
    def __init__(self, fenetre, chemin = None, encodage='utf-8'):
        self.dao = DAO.Dao()
        super().__init__(fenetre, chemin, encodage)

    def insereStopWord(self, chemin):
        stopWord = self.lire(chemin)

        index = 0
        for mot in stopWord:
            self.dao.insert_stop_words(index, mot)
            index += 1

    def construireDictio(self):
        data = []

        for mot in self.text:
            # pour enlever les doublons
            if mot not in self.dictionnaire:
                self.dictionnaire[mot] = len(self.dictionnaire)
                data.append((len(self.dictionnaire) -1, mot))

        self.dao.inserer_datas(data)

    def remplir_matrice(self):
        data = []
        # if len(self.matrice) == 0:
        #     self.matrice = np.zeros((len(self.dictionnaire), len(self.dictionnaire)))
        # on doit de nouveau fetch la matrice puisque le dictio est updater apres construire dictio()
        self.fetchDictioMatriceStopWord()
        print(self.dictionnaire)
        print(self.matrice)

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

    def fetchDictioMatriceStopWord(self):
        resultats = self.dao.fetch_all_unique_words()

        # for i, t in enumerate(resultats):
        #     self.dictionnaire[t[1]] = i

        for mot in resultats:
            self.dictionnaire[mot[1]] = mot[0]

        self.matrice = np.zeros((len(self.dictionnaire), len(self.dictionnaire)))
        list = self.dao.fetch_coocurrence()
        for y in list:
            ## mettre condition que la fenetre soit la mm que la notre
            if str(y[3]) == self.fenetre:
                self.matrice[y[0]][y[1]] = y[2]

        listTupleStopWords = self.dao.fetch_nom_stop_word()
        stopWords = []
        for mot in listTupleStopWords:
            stopWords.extend(mot)

        return self.matrice, self.dictionnaire, stopWords