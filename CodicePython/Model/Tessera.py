import datetime


class Tessera:
    contatore = 0

    def __init__(self):
        self.codice = 0
        self.nome_donatore = ""
        self.cognome_donatore = ""
        self.donazioni = []  # elenco delle donazioni passate
        self.numero_donazioni = 0

    def __getCodice__(self):
        return self.codice

    def __setCodice__(self, contatore):
        self.codice = contatore
        contatore += 1

    def __getNomeDonatore__(self):
        return self.nome_donatore

    def __setNomeDonatore__(self, nome):
        self.nome_donatore = nome

    def __getCognomeDonatore__(self):
        return self.cognome_donatore

    def __setCognomeDonatore__(self, cognome):
        self.cognome_donatore = cognome

    def __getNumeroDonazioni__(self):
        return self.numero_donazioni

    def __setNumeroDonazioni__(self, numero_donazioni):
        numero_donazioni += 1

    def __getDonazioni(self):
        return self.donazioni

    def __setDonazioni__(self, year, month, day, donazioni):
        data = datetime.datetime(year, month, day)
        donazioni.append(data)

    def __getInfoTessera__(self) -> str:
        return super().__str__(self.__getCodice__(), self.__getNomeDonatore__(), self.__getCognomeDonatore__(),
                               self.__getDonazioni(), self.__getNumeroDonazioni__())

    def __setinfoTessera__(self, codice, nome, cognome, year, month, day, numero_donazioni):
        Tessera.__setCodice__(self, codice)
        Tessera.__setNomeDonatore__(self, nome)
        Tessera.__setCognomeDonatore__(self, cognome)
        Tessera.__setDonazioni__(self, year, month, day)
        Tessera.__setNumeroDonazioni__(self, numero_donazioni)
