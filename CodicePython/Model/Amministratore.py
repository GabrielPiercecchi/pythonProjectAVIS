import Utente
from CodicePython.Model.Tessera import Tessera
import datetime


class Amministratore(Utente):
    # conta_tessere = 1
    elencoTessere = []

    def __init__(self, cellulare, codice_fiscale, cognome,
                 data_nascita, email, nome, password):
        Utente.Utente.__init__(self, cellulare, codice_fiscale, cognome,
                               data_nascita, email, nome, password)

    def __iscrivi_donatore__(self):
        pass  # al momento vuoto, da compilare in seguito

    def __crea_tessera__(self, conta_tessere):
        num = Tessera.__setCodice__(contatore=conta_tessere)
        conta_tessere += 1
        tessera = Tessera(codice=num, nome_donatore=nome, cognome_donatore=cognome, donazioni=[], numero_donazioni=0)
        self.elencoTessere.append(tessera)
