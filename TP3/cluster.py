import numpy as np
import time
from scipy.spatial.distance import cdist
import csv

from numpy import float32

def uniq(ordre, distance): return 1
def harm(ordre, distance): return 1 / (ordre + 1)
def dist(ordre, distance): return 1 / (distance ** 2 + 1)

PONDERATION = [uniq, harm, dist]


class Cluster():
    def __init__(self, nbrMaxMot: int, nbrKnn: int):
        self.nbrMaxMot = nbrMaxMot
        self.nbrKnn = nbrKnn
        self.start_time = 0
        self.tour = 0
        self.matrice = None
        self.listCentroid = []
        self.resultat = []
        self.dictioMots = {}

    def randomCentroid(self, matrice, kCentroid: int):
        self.start_time = time.time()

        for i in range(kCentroid):
            random_y = np.random.randint(matrice.shape[0])
            y_values = matrice[random_y, :]
            self.listCentroid.append(y_values)

    def associationAuCentroid(self, matrice):

        distance = np.array(cdist(matrice, np.array(self.listCentroid)))
        resultats = np.argmin(distance, axis=1).tolist()

        # for i in range(matrice.shape[0]):
        #     y_values = matrice[i, :]
        #     # Initialiser la liste des distances pour chaque centroid
        #     distances = []
        #     for centroid in self.listCentroid:
        #         # Calculer la distance entre les valeurs de y_values et le centroid courant
        #         dist = np.linalg.norm(y_values - centroid, axis=0)
        #         # Ajouter la distance à la liste des distances
        #         distances.append(dist)
        #     # Trouver l'index du centroid le plus proche
        #     centroid_index = np.argmin(distances)
        #     # Assigner chaque coordonnée au centroid le plus proche
        #     resultats.append(centroid_index)

        if self.resultat:
            self.calculDiffIteration(resultats)
        if self.resultat == resultats:
            self.affichageMotClusterFinal(resultats, distance)
            return False

        self.resultat = resultats
        self.calculAppartenanceCentro()
        return True


    def reassigneCentroid(self, matrice):
        for i in range(len(self.listCentroid)):
            indices = np.where(np.array(self.resultat) == i)[0]
            x_coords = matrice[indices, :]
            self.listCentroid[i] = np.sum(x_coords, axis=0) / x_coords.shape[0]

    def affichageMotClusterFinal(self, resultats, distance):
        #A REVOIR, p-e probleme si le dictionnaire ne se transpose pas en ordre
        mes_cles = list(self.dictioMots.keys())

        #dictio mot/distance
        listeDictio = [{} for _ in range(len(self.listCentroid))]
        for i in range(len(resultats)):
            listeDictio[resultats[i]][(mes_cles[i])] = float(np.min(distance[self.dictioMots[(mes_cles[i])],:]))

        dico, liste_valeurs = self.extraireCsv(mes_cles)
        #ajouter la categorie UNK
        liste_valeurs.append("UNK")

        #p-e choisir une autre ponderation
        pond = PONDERATION[2]

        #pour trier les dictios
        for index, dict in enumerate(listeDictio):
            listeDictio[index] = sorted(dict.items(), key=lambda x: x[1])


        #afficher le KNN pour chaque centroid
        for i in range(len(self.listCentroid)):
            votes = {cGrams: 0 for cGrams in liste_valeurs}
            for ordre, (mot, dist) in enumerate(listeDictio[i][:self.nbrKnn]):
                if mot in dico:
                    votes[dico[mot]] += pond(ordre, dist)
                else:
                    votes["UNK"] += pond(ordre, dist)
            votes = sorted(votes.items(), key=lambda t: t[1], reverse=True)
            for nom, vote in votes[:1]:
                print(f'Centroide {i} -> cgram {nom} ({vote} votes)')
            for i, (cle, valeur) in enumerate(listeDictio[i][:self.nbrMaxMot]):
                if cle in dico:
                    print(f"       {cle} ({dico[cle]}) --> {valeur}")
                else:
                    print(f"       {cle} (UNK) --> {valeur}")
            print("\n")
        print("stable")

    def calculDiffIteration(self, resultats):
        combined_list = zip(self.resultat, resultats)

        # Utiliser la fonction filter() pour filtrer les éléments différents
        diff_list = list(filter(lambda x: x[0] != x[1], combined_list))
        end_time = time.time()
        duration = end_time - self.start_time
        self.start_time = time.time()
        print("Itération " + str(self.tour) + " effectuée en " + str(duration) + " secondes (" + str(
            len(diff_list)) + " changements)")
        self.tour += 1

    def calculAppartenanceCentro(self):
        for i in range(len(self.listCentroid)):
            count_ones = self.resultat.count(i)
            print("Il y a " + str(count_ones) + " mots appartenant au centroïde " + str(i))
        print("\n")

    def extraireCsv(self, mes_cles):
        dico = {}
        with open("Lexique382.csv", "r", encoding="utf-8") as f:

            lines = f.read().splitlines()
            for line in lines[1:]:
                line = line.split('\t')
                if line[0] in mes_cles:
                    dico[line[0]] = line[3]

            liste_valeurs = list(set(dico.values()))

            return dico, liste_valeurs





