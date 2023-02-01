from sys import argv
import re
import numpy as np

class Entrainement:
    def __init__(self, chemin, encodage = 'utf-8'):
        self.chemin = chemin
        self.encodage = encodage
        self.text = None
        self.matrice = None
        self.new_list = []
        self.file_path = r"X:\Session6\Donnees, Megadonnees, Intelligence Artificielle\semaine2\test.txt"

    def lire(self):
        f = open(self.chemin, 'r', encoding=self.encodage)
        text = f.read()
        f.close()
        self.text = text
        return text

    def compter_mots(self):
        return len(re.findall('/w+', self.text))

    def retirer_mots(self, texte):
        d = {}
        mots = re.split(' |\n|\.|\?', texte)
        list = ' '.join(mots).split()

        index = 0
        for i in list:
            #pour enlever les doublons
            if i not in self.new_list:
                d.update({i : index})
                self.new_list.append(i)
                index += 1

        print(d)

        self.matrice = np.zeros((len(self.new_list), len(self.new_list)))

        print(self.matrice)

    def remplir_matrice(self):
        sentences = []
        for i in self.new_list:
            #faire une liste de phrase
            #chatgp regarder la focntion strip()
            sentences = re.split(r'[.!?]+', self.text)
            sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
            sentences


        pass


def main():
    chemin = r"X:\Session6\Donnees, Megadonnees, Intelligence Artificielle\semaine2\test.txt"
    # chemin = argv[1]
    #enc = argv[2]
    #souschaine = argv[3]
    entrainement = Entrainement(chemin)
    text = entrainement.lire()
    entrainement.retirer_mots(text)
    entrainement.remplir_matrice()


if __name__ == '__main__':
    quit(main())