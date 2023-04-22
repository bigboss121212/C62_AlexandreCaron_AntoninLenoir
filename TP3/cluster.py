import numpy as np
import time

from numpy import float32


class Cluster():
    def __init__(self, nbrMaxMot: int):
        self.nbrMaxMot = nbrMaxMot
        self.listCentroid = []
        self.matrice = None
        self.matriceResultat = None
        self.resultat = []
        self.tour = 0
        self.start_time = 0

    def randomCentroid(self, matrice, kCentroid: int):
        self.start_time = time.time()

        for i in range(kCentroid):
            random_y = np.random.randint(matrice.shape[0])
            y_values = matrice[random_y, :]
            self.listCentroid.append(y_values)

    def associationAuCentroid(self, matrice):
        resultats = []

        for i in range(matrice.shape[0]):
            y_values = matrice[i, :]
            # Initialiser la liste des distances pour chaque centroid
            distances = []
            for centroid in self.listCentroid:
                # Calculer la distance entre les valeurs de y_values et le centroid courant
                dist = np.linalg.norm(y_values - centroid, axis=0)
                # Ajouter la distance à la liste des distances
                distances.append(dist)
            # Trouver l'index du centroid le plus proche
            centroid_index = np.argmin(distances)
            # Assigner chaque coordonnée au centroid le plus proche
            resultats.append(centroid_index)

        #faire des set pour comparer notre resultat precendant
        if(self.resultat != []):
            combined_list = zip(self.resultat, resultats)

            # Utiliser la fonction filter() pour filtrer les éléments différents
            diff_list = list(filter(lambda x: x[0] != x[1], combined_list))
            end_time = time.time()
            duration = end_time - self.start_time
            self.start_time = time.time()
            print("Itération " + str(self.tour) + " effectuée en " + str(duration) + " secondes (" + str(len(diff_list)) + " changements)")
            self.tour += 1


        if (self.resultat == resultats):
            print("stable")
            return False
        self.resultat = resultats
        # print(self.resultat)
        for i in range(len(self.listCentroid)):
            count_ones = self.resultat.count(i)
            print("Il y a " + str(count_ones) + " mots appartenant au centroïde" + str(i))

        return True




    def ReassigneCentroid(self, matrice):
        for i in range(len(self.listCentroid)):
            indices = np.where(np.array(self.resultat) == i)[0]
            x_coords = matrice[indices, :]
            self.listCentroid[i] = np.sum(x_coords, axis=0) / x_coords.shape[0]


def main():
    matrix = np.random.randint(0, 100, size=(10000, 10000)).astype(float) / 1
    cluster = Cluster(6)
    cluster.randomCentroid(matrix, 2)
    # print(cluster.listCentroid)

    go = True
    while go:
        go = cluster.associationAuCentroid(matrix)
        cluster.ReassigneCentroid(matrix)



if __name__ == '__main__':
    quit(main())



