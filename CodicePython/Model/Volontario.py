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

    def getOre_annuali(self):
        return self.ore_annuali

    def getOre_settimanali(self):
        return self.ore_settimanali

    # correggere argomenti metodo su enterprise
    def setinfoVolonario(self, cellulare: int, codice_fiscale: "", cognome: "", data_nascita: datetime.date, email: "", nome: "", password: "", idoneita118: bool,
                 orario_lavorativo: datetime.date, stato: bool, turno: datetime.date, ore_annuali: int, ore_settimanali: int):
        self.setinfoPersonale(cellulare, codice_fiscale, cognome, data_nascita, email, nome, password,
                idoneita118, orario_lavorativo, stato, turno)
        self.ore_annuali = ore_annuali
        self.ore_settimanali = ore_settimanali

    def setOre_annuali(self, ore: int):
        self.ore_annuali = ore

    def setOre_settimanali(self, ore: int):
        self.ore_settimanali = ore
