import pickle
from CodicePython import Model


class GestioneFinanze:
    with open('../Model/Rapportino.pickle', 'rb') as f:
        rapportini = list(pickle.load(f))
        for rapportino in rapportini:
            pass


if __name__ == '__main__':
    with open('../Model/Rapportino.pickle', 'rb') as f:
        rapportini = pickle.load(f)
        print(rapportini)
