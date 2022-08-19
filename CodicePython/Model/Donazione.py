import datetime


class Donazione:

    def __init__(self, year: int, month: int, day: int, hour: int, minute: int):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.data_prenotazione = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
        self.idoneita = True

    def __getIdoneita__(self):
        return self.idoneita

    def __setIdoneita__(self, idoneita):
        self.idoneita = idoneita

    def __getDataPrenotazione__(self):
        return self.data_prenotazione

    def __setDataPrenotaione__(self, data_prenotazione, year: int, month: int, day: int, hour: int, minute: int):
        self.data_prenotazione = datetime.datetime(year, month, day, hour, minute)