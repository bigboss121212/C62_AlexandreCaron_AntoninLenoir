from sys import argv
from traceback import print_exc
from dao import DAO
from entrainementBD import EntrainementBD
from recherche import Recherche
from options import Options
from ui import demander
from time import time
from cluster import Cluster

def main() -> int:
    try:
        options = Options()
        with DAO() as bd:
            if options.b:
                bd.creer_tables()
            else:
                cerveau = EntrainementBD(options.chemin, options.enc, options.t, bd, options.v)
                if options.e:
                    t = time()
                    cerveau.entrainer()
                    if options.v:
                        print(f'\nEntraînement en {time()-t} secondes.\n')
                elif options.r:
                    cerveau.charger_donnees()
                    demander(Recherche(cerveau), options.v)
                elif options.c:
                    cerveau.charger_donnees()
                    clust = Cluster(options.n)
                    clust.dictioMots = cerveau.vocabulaire
                    # clust.matrice = cerveau.matrice
                    clust.randomCentroid(cerveau.matrice, options.k)

                    go = True
                    while go:
                        go = clust.associationAuCentroid(cerveau.matrice)
                        clust.reassigneCentroid(cerveau.matrice)

    except Exception as e:
        print(f'\n{e}\n')
        print_exc()
        return 1
    return 0

if __name__ == '__main__':
    quit(main())