import pickle


class GestioneFinanze:
    with open('Model/Rapportino.pickle', 'rb') as f:
        rapportini = list(pickle.load(f))
        for rapportino in rapportini:
            pass