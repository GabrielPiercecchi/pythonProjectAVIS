import Utente
from CodicePython.Model.Tessera import Tessera
from CodicePython.Model.Donatore import Donatore
import datetime


class Amministratore(Utente):
    # conta_tessere = 1
    elenco_tessere = []
    elenco_donatori = []
    donatore = ""

    def __init__(self, cellulare, codice_fiscale, cognome,
                 data_nascita, email, nome, password):
        Utente.Utente.__init__(self, cellulare, codice_fiscale, cognome,
                               data_nascita, email, nome, password)

    def __iscrivi_donatore__(self):
        donatore = Donatore()
        self.elenco_donatori.append(donatore)
        pass  # al momento vuoto, da compilare in seguito

    def __crea_tessera__(self, conta_tessere):
        num = Tessera.__setCodice__(contatore=conta_tessere)
        conta_tessere += 1
        donatore = elenco_donatori.append()
        tessera = Tessera(codice=num, nome_donatore=donatore.nome, cognome_donatore=donatore.cognome, donazioni=[], numero_donazioni=0)
        self.elenco_tessere.append(tessera)
