from CodicePython.Model.Rapportino import Rapportino

class Personale:

    lista_rapportini = []

    def __inserisciRapportino__(self, data, KM_inizio, KM_fine):
        rapportino = Rapportino(data_servizio=data, KM_inizio=KM_inizio, KM_fine=KM_fine)
        self.lista_rapportini.append(rapportino)
        return True

