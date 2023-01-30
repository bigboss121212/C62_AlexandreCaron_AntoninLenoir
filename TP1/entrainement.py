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

    def lire(self):
        f = open(self.chemin, 'r', encoding=self.encodage)
        text = f.read()
        f.close()
        return text

    def compter_mots(self):
        return len(re.findall('/w+', self.text))

    def retirer_mots(self, texte):
        d = {}
        mots = re.split(' |\n|\.|\?', texte)
        list = ' '.join(mots).split()


        index = 0
        for i in list:
            if i not in self.new_list:
                d.update({i : index})
                self.new_list.append(i)
                index += 1

        print(d)

        self.matrice = np.zeros((len(self.new_list), len(self.new_list)))

        print(self.matrice)

    def remplir_matrice(self):



        pass


def main():
    chemin = argv[1]
    #enc = argv[2]
    #souschaine = argv[3]
    entrainement = Entrainement(chemin)
    text = entrainement.lire()
    entrainement.retirer_mots(text)


if __name__ == '__main__':
    quit(main())