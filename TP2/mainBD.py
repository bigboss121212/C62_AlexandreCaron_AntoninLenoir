import argparse
import entrainement as ent
import prediction as pre
import DAO as d

def main():
    cheminStopWord = "./stopWords.txt"

    parser = argparse.ArgumentParser(prog='TP2', description='Insere les coocurence dans la db')
    parser.add_argument('-e', action="store_true", help="Appeler la fonction entrainer")
    parser.add_argument("-t", nargs="?", help="pour avoir la grosseur de la fenetre")
    parser.add_argument("--enc", nargs="?", help="pour avoir le type d'encodage")
    parser.add_argument("--chemin", nargs="?", help="pour avoir le chemin du corpus d'entrainement")
    parser.add_argument("-r", action="store_true", help="pour appeler la fonction de recherche de recherche de synonyme")
    parser.add_argument("-b", action="store_true", help="pour regenerer la DB")

    args = parser.parse_args()
    dao = d.Dao()

    if args.b:
        dao.delete_and_recreate()
    if (args.e and args.t and args.enc and args.chemin) or (args.r and args.t):

        entrainementDB = ent.EntrainementDB(args.t)
        dictio = entrainementDB.fetchDictio()
        matrice = entrainementDB.fetchMatrice()
        stopWords = entrainementDB.fetchStopWord()

        if args.e and args.t and args.enc and args.chemin:
            entrainementDB.encodage = args.enc
            entrainementDB.lire(args.chemin)
            entrainementDB.construireDictio()
            entrainementDB.remplir_matrice()
            entrainementDB.insereStopWord(cheminStopWord)
        if args.r and args.t:
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
        print(parser.print_help())

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    main()

