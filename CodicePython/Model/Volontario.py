from CodicePython.Model.Personale import Personale
import datetime

class Volontario(Personale):
    def __init__(self, cellulare: int, codice_fiscale: "", cognome: "",
                 data_nascita: datetime.date, email: "", nome: "", password: "", idoneita118: bool,
                 orariolavorativo: datetime.date, stato: bool, turno: datetime.date, oreAnnuali: int,
                 oreSettimanali: int):
        super().__init__(cellulare, codice_fiscale, cognome, data_nascita, email, nome, password, idoneita118,
                 orariolavorativo, stato, turno)
        self.oreAnnuali = oreAnnuali
        self.oreSettimanali = oreSettimanali

    def getinfoVolontario(self):
        info = self.getinfoPersonale()
        info += {
            "Ore annuali": self.oreAnnuali,
            "Ore settimanali": self.oreSettimanali
        }
        return info

    def getOreAnnuali(self):
        return self.oreAnnuali

    def getOreSettimanali(self):
        return self.oreSettimanali

    # correggere argomenti metodo su enterprise
    def setinfoVolonario(self, cellulare, codice_fiscale, cognome, data_nascita, email, nome, password, idoneita118,
                 orariolavorativo, stato, turno, oreAnnuali, oreSettimanali):
        self.setinfoPersonale(cellulare, codice_fiscale, cognome, data_nascita, email, nome, password,
                idoneita118, orariolavorativo, stato, turno)
        self.oreAnnuali = oreAnnuali
        self.oreSettimanali = oreSettimanali

    def setOreAnnuali(self, ore: int):
        self.oreAnnuali = ore

    def setOreSettimanali(self, ore: int):
        self.oreSettimanali = ore
