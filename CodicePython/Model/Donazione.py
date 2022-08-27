import datetime

from CodicePython.Model.Donatore import Donatore


class Donazione:

    def __init__(self, donatore: Donatore, id_donazione: int, tipo: bool, year: int, month: int, day: int, hour: int,
                 minute: int, disponibile: bool):
        self.donatore = donatore
        self.id_donazione = id_donazione
        self.tipo = tipo
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.disponibile = disponibile

    def __getDonatore__(self):
        return self.donatore

    def __setDonatore__(self, donatore):
        self.donatore = donatore

    def __getID_donazione__(self):
        return self.id_donazione

    def __setID_donazione__(self, id_donazione):
        self.id_donazione = id_donazione

    def __getTipo__(self):
        return self.tipo

    def __setTipo__(self, tipo):
        self.tipo = tipo

    def __getDisponibile__(self):
        return self.disponibile

    def __setDisponibile__(self, disponibile):
        self.disponibile = disponibile

    def __getDataPrenotazione__(self):
        return self.data_prenotazione

    def __setDataPrenotazione__(self, year: int, month: int, day: int, hour: int, minute: int):
        self.data_prenotazione = datetime.datetime(year, month, day, hour, minute)