from sys import argv
import re
import numpy as np

class Entrainement:
    def __init__(self, chemin, encodage = 'utf-8'):
        self.chemin = chemin
        self.encodage = encodage
        self.text = None

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

        new_list = []
        index = 0
        for i in list:
            if i not in new_list:
                d.update({i : index})
                new_list.append(i)
                index += 1

        print(d)

        matrice = np.zeros((len(new_list), len(new_list)))

        print(matrice)



def main():
    chemin = argv[1]
    #enc = argv[2]
    #souschaine = argv[3]
    entrainement = Entrainement(chemin)
    text = entrainement.lire()
    entrainement.retirer_mots(text)


if __name__ == '__main__':
    quit(main())