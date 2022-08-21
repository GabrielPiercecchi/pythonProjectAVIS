from CodicePython.Model.Personale import Personale
import datetime

class Dipendente(Personale):

    def __init__(self, cellulare: int, codice_fiscale: "", cognome: "",
                 data_nascita: datetime.date, email: "", nome: "", password: "", idoneita118: bool,
                 orariolavorativo: datetime.date, stato: bool, turno: datetime.date, IBAN: ""):
        super().__init__(cellulare, codice_fiscale, cognome, data_nascita, email, nome, password, idoneita118,
                 orariolavorativo, stato, turno)
        self.IBAN = IBAN

    def getIBAN(self):
        return self.IBAN

    def getinfoDipendente(self):
        info = self.getinfoPersonale()
        info += {
            "IBAN": self.IBAN
        }
        return info

    def setIBAN(self, iban: ""):
        self.IBAN = iban

    # correggere argomenti metodo su enterprise
    def setinfoDipendente(self, cellulare: int, codice_fiscale: "", cognome: "",
                 data_nascita: datetime.date, email: "", nome: "", password: "", idoneita118: bool,
                 orariolavorativo: datetime.date, stato: bool, turno: datetime.date, iban: "" ):
        self.setinfoPersonale(cellulare, codice_fiscale, cognome,
                 data_nascita, email, nome, password, idoneita118,
                 orariolavorativo, stato, turno)
        self.IBAN = iban
