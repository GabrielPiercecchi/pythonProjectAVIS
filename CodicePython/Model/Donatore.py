import datetime

from CodicePython.Model import Tessera
from CodicePython.Model.Donazione import Donazione
from CodicePython.Model.Utente import Utente


class Donatore(Utente):

    def __init__(self, cellulare: int, codice_fiscale: "", cognome: "", data_nascita: datetime.date,
                 email: "", nome: "", password: "", tessera: Tessera, gruppo_sanguigno: "", idoneita: bool):
        Utente.__init__(self, cellulare, codice_fiscale, cognome, data_nascita, email, nome, password)
        self.tessera = tessera
        self.gruppo_sanguigno = gruppo_sanguigno
        self.idoneita = idoneita

    def __getGruppo_sanguigno__(self):
        return self.gruppo_sanguigno

    def __setGruppo_sanguigno__(self, gruppo_sanguigno):
        self.gruppo_sanguigno = gruppo_sanguigno

    def __getIdoneita__(self):
        return self.idoneita

    def __setIdoneita__(self, idoneita):
        self.idoneita = idoneita

    def __getInfoDonatore__(self):
        return {
            "Nome": self.getNome(),
            "Cognome": self.getCognome(),
            "Codice Fiscale": self.getCodice_fiscale(),
            "Email": self.getEmail(),
            "Cellulare": self.getCellulare(),
            "Data di nascita": self.getData_nascita(),
            "Password": self.getPassword(),
            "Gruppo sanguigno": self.__getGruppo_sanguigno__(),
            "Idoneita": self.__getIdoneita__()
        }

    def __visualizzaDisponibilita__(self):
        donazioni = []
        disponibili = []
        with open('../orari.txt', 'r') as fp:
            for line in fp:  # problema
                donazione = Donazione(year, month, day, hour, minute, disponibile)  # aggiungere attributo???
                donazioni.append(donazione)
            for donazione in donazioni:
                if donazione.disponibile == True:
                    disponibili.append(donazione)
                    with open('../Controller/disponibilita.txt', 'w') as fp:
                        for donazione in donazioni:
                            fp.write(str(donazione.year) + ' ' + str(donazione.month) + ' ' + str(donazione.day) + ' ' +
                                     str(donazione.hour) + ' ' + str(donazione.minute) + ' ' + str(
                                donazione.disponibile))

"""
Metodo __visualizzaDisponibilità__ (alternativo che stampa solo il file orari.txt)
--> Per questo motivo bisognerà creare un metodo che permetta di salvare una data
    e fare in modo che non possa essere scelta ancora.
    
    def __visualizzaDisponibilita__(self):
            with open('orari.txt') as f:
                lines = f.read()
                print(lines)
                
--> IMPORTANTE: QUESTO METODO SU ENTERPRISE CE L'HA SIA IL "DONATORE" CHE "GESTIONE PRENOTAZIONE"
                DEVE ESSERE TENUTO SOLO SU "GESTIONE PRENOTAZIONE"
"""

