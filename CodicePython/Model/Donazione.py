import datetime


class Donazione:

    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, disponibile: bool):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.disponibile = disponibile

    def __getDisponibile__(self):
        return self.disponibile

    def __setDisponibile__(self, disponibile):
        self.disponibile = disponibile

    def __getDataPrenotazione__(self):
        return self.data_prenotazione

    def __setDataPrenotazione__(self, data_prenotazione, year: int, month: int, day: int, hour: int, minute: int):
        self.data_prenotazione = datetime.datetime(year, month, day, hour, minute)