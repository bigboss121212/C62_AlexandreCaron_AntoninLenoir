import argparse
import entrainement as ent
import prediction as pre
import DAO as d
import numpy as np



def main():
    cheminStopWord = "./stopWords.txt"

    parser = argparse.ArgumentParser(
        prog='TP2',
        description='Insere les coocurence dans la db')

    parser.add_argument('-e', action="store_true", help="Appeler la fonction entrainer")
    parser.add_argument("-t", nargs="?", help="pour avoir la grosseur de la fenetre")
    parser.add_argument("--enc", nargs="?", help="pour avoir le type d'encodage")
    parser.add_argument("--chemin", nargs="?", help="pour avoir le chemin du corpus d'entrainement")
    parser.add_argument("-r", action="store_true", help="pour appeler la fonction de recherche de recherche de synonyme")
    parser.add_argument("-b", action="store_true", help="pour regenerer la DB")

    args = parser.parse_args()
    dao = d.Dao()

    if args.b:
        # regenere la db
        dao.delete_and_recreate()
    if (args.e and args.t and args.enc and args.chemin) or (args.r and args.t):
        # construire diction mot unique en fonction de la fenetre

        resultats = dao.fetch_mots_selon_taille_fenetre(args.t)
        dictio = {}
        for i, t in enumerate(resultats):
            dictio[t[0]] = i

        #construire matrice de coocurence
        matrice = np.zeros((len(dictio), len(dictio)))
        list = dao.fetch_coocurrence()
        for y in list:
            ## mettre condition que la fenetre soit la mm que la notre
            if str(y[3]) == args.t:
                matrice[y[0] - 1][y[1] - 1] = y[2]

        # aller chercher les stopWord dans la db
        listTupleStopWords = dao.fetch_nom_stop_word()
        stopWords = []
        for mot in listTupleStopWords:
            stopWords.extend(mot)

        if args.e and args.t and args.enc and args.chemin:
            # Appel de la fonction d'entrainement
            entrainementDB = ent.EntrainementDB(args.t, args.chemin, args.enc)
            entrainementDB.remplir_matrice()
            stopWords = entrainementDB.lire(cheminStopWord)
            entrainementDB.insereStopWord(stopWords)
        if args.r and args.t:
            # Appel pour la recherche
            while True:
                mots = input(
                    "Entrez un mot, le nombre de synonymes que vous voulez et la methode de calcul, i.e produit scalaire: 0, least-square: 1, city-block: 2 \n\nTapper q pour quitter\n\n").split(
                    ' ')
                if mots[0] == "q":
                    break
                if mots[0] in dictio and mots[2] in ["0", "1", "2"]:
                    if len(mots) == 3:
                        pre.Prediction(matrice, dictio, mots[0], mots[1], stopWords, mots[2])
    else:
        ##parser.error("Argument manquant")
        print(parser.print_help())



# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    main()

