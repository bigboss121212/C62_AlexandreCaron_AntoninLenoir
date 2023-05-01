from cProfile import label
import numpy as np
from options import Options

SEP = ';'


def uniq(ordre, distance): return 1
def harm(ordre, distance): return 1 / (ordre + 1)
def dist(ordre, distance): return 1 / (distance ** 2 + 1)

PONDERATION = [uniq, harm, dist]

class KNN():
    def __init__(self, k, ch_feat, ch_label, enc, norm):
        self.k = k
        self.noms_features, self.features = self.extract(ch_feat, enc, self.extract_feature)
        self.noms_labels, self.labels = self.extract(ch_label, enc, self.extract_label)
        if norm:
            self.features = self.normalize(self.features)

    def extract(self, ch, enc, fonc):
        with open(ch, encoding=enc) as f:
            lines = f.read().splitlines()
        noms = lines[0].split(SEP)
        data = np.array([fonc(line) for line in lines[1:]])

        return noms, data

    def extract_feature(self, line):
        return [float(x) for x in line.split(SEP)]

    def extract_label(self, line):
        return int(line)

    def normalize(self, features):
        return (features.transpose() / np.linalg.norm(features, axis=1)).transpose()

    def knn(self, id, pond):
        distances = []
        for index, coord in enumerate(self.features):
            if index != id:
                d = np.linalg.norm(self.features[index] - self.features[id])
                distances.append((d, self.noms_labels[self.labels[index]]))
        distances = sorted(distances)

        votes = {nom: 0 for nom in self.noms_labels}
        for ordre, (distance, label) in enumerate(distances[:self.k]):
            votes[label] += pond(ordre, distance)
        votes = sorted(votes.items(), key=lambda t: t[1], reverse=True)

        for d, nom in distances:
            print(f'{nom} : {d}')
        print(f'\n\nReal label: {self.noms_labels[self.labels[id]]}')
        for nom, vote in votes:
            print(f'{nom} : {vote}')


def main():
    opts = Options()
    knn = KNN(opts.k, opts.features, opts.labels, opts.enc, opts.normalize)
    # print(knn.noms_features)
    # print(knn.features)
    # print(knn.noms_labels)
    # print(knn.labels)

    knn.knn(opts.id, PONDERATION[opts.weighting])

    return 0


if __name__ == '__main__':
    quit(main())