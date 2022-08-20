import datetime

from CodicePython.Model.Donazione import Donazione
from CodicePython.Model.Utente import Utente


class Donatore(Utente):

    def __init__(self, cellulare: int, codice_fiscale: "", cognome: "",
                 data_nascita: datetime.date, email: "", nome: "", password: "", gruppo_sanguigno: "", idoneita: bool ):
        Utente.__init__(self, cellulare, codice_fiscale, cognome,
                 data_nascita, email, nome, password)
        self.gruppo_sanguigno = gruppo_sanguigno
        self.idoneita = idoneita

        #### INSERIRE METODI GET E SET

    def __visualizzaDisponibilita__(self):
        donazioni = []
        disponibili = []
        with open('orari.txt', 'r') as fp:
            for line in fp:  # problema
                donazione = Donazione(year=, month=, day=, hour=, minute=, disponibile=)  # aggiungere attributo???
                donazioni.append(donazione)
            for donazione in donazioni:
                if donazione.disponibile == True:
                    disponibili.append(donazione)
                    with open('disponibilita.txt', 'w') as fp:
                        for donazione in donazioni:
                            fp.write(str(donazione.year) + ' ' + str(donazione.month) + ' ' + str(donazione.day) + ' ' +
                                     str(donazione.hour) + ' ' + str(donazione.minute) + ' ' + str(donazione.disponibile))