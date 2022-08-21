from CodicePython.Model.Rapportino import Rapportino
from CodicePython.Model.Utente import Utente
import datetime

class Personale(Utente):

    lista_rapportini = []
    
    def __init__(self, cellulare: int, codice_fiscale: "", cognome: "",
                 data_nascita: datetime.date, email: "", nome: "", password: "", idoneita118: bool,
                 orariolavorativo: datetime.date, stato: bool, turno: datetime.date):
        super().__init__(cellulare, codice_fiscale, cognome, data_nascita, email, nome, password)
        self.idoneita118 = idoneita118
        self.orariolavorativo = orariolavorativo
        self.stato = stato
        self.turno = turno
    
    def getinfoPersonale(self):
        info = self.getinfoUtente()
        info += {
            "Idoneità 118": self.idoneita118,
            "Orario lavorativo": self.orariolavorativo,
            "Stato": self.stato,
            "Turno": self.turno
        }
        return info

    def getIdoneita118(self):
        return self.idoneita118

    def getOrariolavorativo(self):
        return self.orariolavorativo

    def getStato(self):
        return self.stato

    def getTurno(self):
        return self.turno

    def setinfoPersonale(self, cellulare: int, codice_fiscale: "", cognome: "",
                 data_nascita: datetime.date, email: "", nome: "", password: "", idoneita118: bool,
                 orariolavorativo: datetime.date, stato: bool, turno: datetime.date):
        self.setinfoUtente(cellulare, codice_fiscale, cognome,
                 data_nascita, email, nome, password)
        self.idoneita118 = idoneita118
        self.orariolavorativo = orariolavorativo
        self.turno = turno
        self.stato = stato

    def setIdoneita118(self, idoneita: bool):
        self.idoneita118 = idoneita

    def setOrariolavorativo(self, orario: datetime.date):
        self.orariolavorativo = orario

    def setStato(self, stato: bool):
        self.stato = stato

    def setTurno(self, turno: datetime.date):
        self.turno = turno
        
    def __inserisciRapportino__(self, data, KM_inizio, KM_fine):
        rapportino = Rapportino(data_servizio=data, KM_inizio=KM_inizio, KM_fine=KM_fine)
        self.lista_rapportini.append(rapportino)
        return True

