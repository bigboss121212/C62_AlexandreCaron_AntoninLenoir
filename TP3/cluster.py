import numpy as np

class Cluster():
    def __init__(self, taille: int, nbrMaxMot: int):
        self.taille, self.nbrMaxMot = taille, nbrMaxMot
        self.listCentroid = []
        self.matrice = None
        self.matriceResultat = None

    def randomCentroid(self, matrice, kCentroid: int):

        for i in range(kCentroid):
            random_y = np.random.randint(matrice.shape[0])
            y_values = matrice[random_y, :]
            self.listCentroid.append(y_values)

    def associationCentroid(self, matrice):

        resultats = np.zeros_like(matrice)

        # Parcourir chaque coordonnée de la matrice
        for i in range(matrice.shape[0]):
            y_values = matrice[i, :]
            # Calculer les distances entre les valeurs de y_values et les deux points
            dist1 = np.linalg.norm(y_values - self.listCentroid[0], axis=0)
            dist2 = np.linalg.norm(y_values - self.listCentroid[1], axis=0)
            # Assigner chaque coordonnée au point le plus proche
            resultats[i] = np.where(dist1 < dist2, 1, 2)

        # Afficher les résultats
        print(resultats)
        self.matriceResultat = resultats

    def assignePointAuCentroid(self, matrice):
        y_coordsCentroid1 = np.where(np.any(self.matriceResultat == 1, axis=1))[0]
        y_coordsCentroid2 = np.where(np.any(self.matriceResultat == 2, axis=1))[0]

        x_coords = []
        for y in y_coordsCentroid1:
            x_coords.append(matrice[y, :])
        x_coordsCentroid1 = np.array(x_coords)

        self.listCentroid[0] = self.updateCentroid(x_coordsCentroid1)

        x_coords = []
        for y in y_coordsCentroid2:
            x_coords.append(matrice[y, :])
        x_coordsCentroid2 = np.array(x_coords)

        self.listCentroid[1] = self.updateCentroid(x_coordsCentroid2)
        yo


    def updateCentroid(self, matricePointAssocieCentroid):
        return np.sum(matricePointAssocieCentroid, axis= 0)/ matricePointAssocieCentroid.shape[0]






def main():

    matrix = np.random.randint(0, 100, size=(50, 50))

    cluster = Cluster(5, 6)
    cluster.randomCentroid(matrix, 2)

    print(cluster.listCentroid)

    cluster.associationCentroid(matrix)
    cluster.assignePointAuCentroid(matrix)


if __name__ == '__main__':
    quit(main())



