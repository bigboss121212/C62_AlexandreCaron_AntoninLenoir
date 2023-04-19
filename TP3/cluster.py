import numpy as np

class Cluster():
    def __init__(self, taille: int, nbrMaxMot: int):
        self.taille, self.nbrMaxMot = taille, nbrMaxMot
        self.listCentroid = []
        self.matrice = None
        self.matriceResultat = None
        self.resultat = []
        self.tour = 0

    def randomCentroid(self, matrice, kCentroid: int):

        for i in range(kCentroid):
            random_y = np.random.randint(matrice.shape[0])
            y_values = matrice[random_y, :]
            self.listCentroid.append(y_values)

    def associationAuCentroid(self, matrice):
        resultats = []
        # resultats = np.zeros_like(matrice)
        #
        # # Parcourir chaque coordonnée de la matrice
        # for i in range(matrice.shape[0]):
        #     y_values = matrice[i, :]
        #     # Calculer les distances entre les valeurs de y_values et les deux points
        #     dist1 = np.linalg.norm(y_values - self.listCentroid[0], axis=0)
        #     dist2 = np.linalg.norm(y_values - self.listCentroid[1], axis=0)
        #     # Assigner chaque coordonnée au point le plus proche
        #     resultats[i] = np.where(dist1 < dist2, 1, 2)
        #
        # # Afficher les résultats
        # print(resultats)
        # self.matriceResultat = resultats


#version pour k centroid
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

        if (self.resultat == resultats):
            print("stable")
            return False
        self.resultat = resultats
        print(self.resultat)
        print("**************" + str(self.tour) + "tour")
        self.tour+=1



    def ReassigneCentroid(self, matrice):
        for i in range(len(self.listCentroid)):
            indices = np.where(np.array(self.resultat) == i)[0]
            x_coords = matrice[indices, :]
            self.listCentroid[i] = np.sum(x_coords, axis=0) / x_coords.shape[0]



        # print(self.listCentroid)

        #
        # y_coordsCentroid1 = np.where(np.any(self.matriceResultat == 1, axis=1))[0]
        # y_coordsCentroid2 = np.where(np.any(self.matriceResultat == 2, axis=1))[0]
        #
        # x_coords = []
        # for y in y_coordsCentroid1:
        #     x_coords.append(matrice[y, :])
        # x_coordsCentroid1 = np.array(x_coords)
        #
        # self.listCentroid[0] = self.updateCentroid(x_coordsCentroid1)
        #
        # x_coords = []
        # for y in y_coordsCentroid2:
        #     x_coords.append(matrice[y, :])
        # x_coordsCentroid2 = np.array(x_coords)
        #
        # self.listCentroid[1] = self.updateCentroid(x_coordsCentroid2)



    # def updateCentroid(self, matricePointAssocieCentroid):
    #     return np.sum(matricePointAssocieCentroid, axis= 0)/ matricePointAssocieCentroid.shape[0]

def main():

    matrix = np.random.randint(0, 100, size=(10000, 10000)).astype(float) / 1

    cluster = Cluster(5, 6)
    cluster.randomCentroid(matrix, 10)

    # print(cluster.listCentroid)


    while True:

        cluster.associationAuCentroid(matrix)

        cluster.ReassigneCentroid(matrix)

    # cluster.associationAuCentroid(matrix)
    #
    # cluster.ReassigneCentroid(matrix)


if __name__ == '__main__':
    quit(main())



