import datetime


class Tessera:

    contatore = 0

    def __init__(self):
        self.codice = 0
        self.nome_donatore = ""
        self.cognome_donatore = ""
        self.donazioni = datetime.datetime(year=2022, month=1, day=1)
        self.numero_donazioni = 0

    def __getCodice__(self):
        return self.codice

    def __setCodice__(self, contatore):
        self.codice = contatore
        contatore += 1