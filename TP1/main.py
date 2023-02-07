from sys import argv
import entrainement as ent
import prediction as pre


#class Main:
   # def __init__(self):
       # pass

def main():
    fenetre = int(argv[1])
    enc = argv[2]
    chemin = argv[3]

    entrainement = ent.Entrainement(fenetre, chemin, enc)
    matrice, dictio = entrainement.remplir_matrice()

    while True:
        mots = input("Entrez un mot, le nombre de synonymes que vous voulez et la methode de calcul, i.e produit scalaire: 0, least-square: 1, city-block: 2 \n\nTapper q pour quitter\n\n").split(' ')

        if mots[0] == "q":
            break
        else:
            if len(mots) == 3:
                prediction = pre.Prediction(matrice, dictio, mots[0], mots[1])
                if mots[2] == "0":
                    prediction.produitScalaire(mots[1])
                if mots[2] == "1":
                    prediction.moindreCarre(mots[1])
                if mots[2] == "2":
                    prediction.manhattan(mots[1])

if __name__ == '__main__':
    quit(main())