from sys import argv
import re
import numpy as np

class Entrainement:
    def __init__(self, chemin, encodage = 'utf-8'):
        self.chemin = chemin
        self.encodage = encodage
        self.text = None
        self.matrice = None
        self.dictionnaire = None
        self.new_list = []
        self.file_path = r"X:\Session6\Donnees, Megadonnees, Intelligence Artificielle\semaine2\test.txt"
        self.fenetre = 7
        self.lire()
        self.construireDictio(self.text)

    def lire(self):
        f = open(self.chemin, 'r', encoding=self.encodage)
        text = f.read()
        f.close()
        self.text = re.findall('\w+', text)
        #return text

    def compter_mots(self):
        return len(re.findall('\w+', self.text))

    ##chat GPT
    def remove_duplicates(self, words):
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        return unique_words

    def construireDictio(self, texte):
        d = {}
        #mots = re.split(' |\n|\.|\?', texte)
        #list = ' '.join(mots).split()

        index = 0
        for i in texte:
            #pour enlever les doublons
            if i not in self.new_list:
                d.update({i : index})
                self.new_list.append(i)
                index += 1

        self.dictionnaire = d
        self.matrice = np.zeros((len(self.new_list), len(self.new_list)))

    def remplir_matrice(self):

        for i in range(len(self.text)):
            for j in range(1,self.fenetre//2 + 1):
                if(i+j < len(self.text)) and self.dictionnaire[self.text[i]] != self.dictionnaire[self.text[i + (j)]]:
                    self.matrice[self.dictionnaire[self.text[i]], self.dictionnaire[self.text[i + (j)]]] += 1
                if (i - j >= 0 ) and self.dictionnaire[self.text[i]] != self.dictionnaire[self.text[i - (j)]]:
                    self.matrice[self.dictionnaire[self.text[i]], self.dictionnaire[self.text[i - (j)]]] += 1

        return self.matrice, self.dictionnaire


def main():
    chemin = r"X:\Session6\Donnees, Megadonnees, Intelligence Artificielle\semaine2\test.txt"
    entrainement = Entrainement(chemin)
    matrice, dictio = entrainement.remplir_matrice()

    return matrice, dictio


if __name__ == '__main__':
    quit(main())