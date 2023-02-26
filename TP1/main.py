from sys import argv
import entrainement as ent
import prediction as pre


def main():
    fenetre = int(argv[1])
    enc = argv[2]
    chemin = argv[3]
    cheminStopWord = "./stopWords.txt"

    entrainement = ent.Entrainement(fenetre, chemin, enc)
    matrice, dictio = entrainement.remplir_matrice()
    stopWords = entrainement.lire(cheminStopWord)

    while True:
        mots = input("Entrez un mot, le nombre de synonymes que vous voulez et la methode de calcul, i.e produit scalaire: 0, least-square: 1, city-block: 2 \n\nTapper q pour quitter\n\n").split(' ')

        if mots[0] == "q":
            break
        if mots[0] in dictio and mots[2] in ["0", "1", "2"]:
            if len(mots) == 3:
                pre.Prediction(matrice, dictio, mots[0], mots[1], stopWords, mots[2])

if __name__ == '__main__':
    quit(main())