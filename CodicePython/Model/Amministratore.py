import os.path
import pickle

from CodicePython.Model.Utente import Utente
import fileinput

from CodicePython.Model.Dipendente import Dipendente
from CodicePython.Model.Donazione import Donazione
from CodicePython.Model.Tessera import Tessera
from CodicePython.Model.Donatore import Donatore
import datetime

from CodicePython.Model.Volontario import Volontario


class Amministratore(Utente):
    conta_tessere = 1

    def __init__(self, cellulare, codice_fiscale, cognome,
                 data_nascita, email, nome, password):
        Utente.__init__(self, cellulare, codice_fiscale, cognome,
                        data_nascita, email, nome, password)
        self.elenco_donatori = []
        self.elenco_volontari = []
        self.elenco_dipendenti = []

    def __iscriviDonatore__(self, nome, cognome, codice_fiscale, data_nascita, cellulare, email,
                            password, gruppo_sanguigno, idoneita=True):
        donatore = Donatore(cellulare, codice_fiscale, cognome, data_nascita, email, nome, password,
                            self.conta_tessere, gruppo_sanguigno, True)

        if os.path.isfile('Model/Donatori.pickle'):
            with open('Model/Donatori.pickle', 'rb') as f:  # lettura
                self.elenco_donatori = pickle.load(f)
        self.elenco_donatori.append(donatore)
        with open('Model/Donatori.pickle', 'wb') as f:
            pickle.dump(self.elenco_donatori, f, pickle.HIGHEST_PROTOCOL)

    def ricercaDonatore(self, codice_fiscale):
        if os.path.isfile('Model/Donatori.pickle'):
            with open('Model/Donatori.pickle', 'rb') as f:
                donatori = list(pickle.load(f))
                for donatore in donatori:
                    if donatore.codice_fiscale == codice_fiscale:
                        return donatore
                return None
        else:
            return None

    def __eliminaDonatore__(self, codice_fiscale):
        if os.path.isfile('Model/Donatori.pickle'):
            with open('Model/Donatori.pickle', 'rb') as f:
                donatori = list(pickle.load(f))
                for donatore in donatori:
                    if donatore.codice_fiscale == codice_fiscale:
                        donatori.remove(donatore)
            with open('Model/Donatori.pickle', 'wb') as f:
                pickle.dump(donatori, f, pickle.HIGHEST_PROTOCOL)

    def __crea_tessera__(self, conta_tessere, nome, cognome):
        tessera = Tessera(conta_tessere, nome, cognome, donazioni=[], numero_donazioni=0)
        if os.path.isfile('Model/Tessere.pickle'):
            with open('Model/Tessere.pickle', 'rb') as f:  # lettura
                tessere = pickle.load(f)
        tessere.append(tessera)
        with open('Model/Tessere.pickle', 'wb') as f:
            pickle.dump(tessere, f, pickle.HIGHEST_PROTOCOL)
        conta_tessere += 1

    def __ricercaTessera__(self, numero):
        if os.path.isfile('Model/Tessere.pickle'):
            with open('Model/Tessere.pickle', 'rb') as f:
                tessere = dict(pickle.load(f))
                for tessera in tessere.values():
                    if tessera.codice == numero:
                        return tessera
                return None
        else:
            return None

    def __eliminaTessera__(self, numero):
        if os.path.isfile('Model/Tessera.pickle'):
            with open('Model/Tessera.pickle', 'wb+') as f:
                tessere = dict(pickle.load(f))
                for tessera in tessere.values():
                    if tessera.codice == numero:
                        tessere.pop(tessera)
                pickle.dump(tessere, f, pickle.HIGHEST_PROTOCOL)

    def __visualizzaDisponibilita__(self):
        orario = []
        with open('../orari.txt', 'r') as fp:
            for line in fp:
                orario.append(line)
        return orario

    def __modificaStatoDonazione__(self, anno, mese, giorno, ora, minuto,
                                   donatore):  # DA FARE!!!
        donazioni = []
        with open('../orari.txt', 'r') as fp:
            for line in fp:
                line = fp.readline()
                linea = line[0:17]
                year = linea[0:3]
                month = linea[5:6]
                day = linea[8:9]
                hour = linea[11:12]
                minute = linea[14:15]
                disponibile = linea[17]
                donazione = Donazione(int(year), int(month), int(day), int(hour), int(minute),
                                      bool(disponibile))  # aggiungere attributo codice???
                donazioni.append(donazione)
            for donazione in donazioni:
                if donazione.year == anno and donazione.month == mese and donazione.day == giorno and donazione.hour == ora and donazione.minute == minuto:
                    if donatore == 0:
                        Donazione.disponibile = "L"
                        # modifica tessera donatore
                    else:
                        Donazione.disponibile = "O"
                        # modifica tessera donatore
        with open('../orari.txt', 'w') as fp:
            for donazione in donazioni:
                fp.write(str(donazione.year) + ' ' + str(donazione.month) + ' ' + str(donazione.day) + ' ' + str(
                    donazione.hour) + ' ' + str(donazione.minute) + ' ' + str(donazione.disponibile))

    def iscriviDipendente(self, cellulare, codice_fiscale, cognome, data_nascita, email, nome, password, idoneita118, stato,
                          IBAN):
        dipendente = Dipendente(cellulare, codice_fiscale, cognome, data_nascita, email, nome, password, idoneita118, stato, IBAN)
        if os.path.isfile('Model/Dipendenti.pickle'):
            with open('Model/Dipendenti.pickle', 'rb') as f:  # lettura
                self.elenco_dipendenti = pickle.load(f)
        self.elenco_dipendenti.append(dipendente)
        with open('Model/Dipendenti.pickle', 'wb') as f:
            pickle.dump(self.elenco_dipendenti, f, pickle.HIGHEST_PROTOCOL)

    def ricercaDipendente(self, codice_fiscale):
        if os.path.isfile('Model/Dipendenti.pickle'):
            with open('Model/Dipendenti.pickle', 'rb') as f:
                dipendenti = list(pickle.load(f))
                for dipendente in dipendenti:
                    if dipendente.codice_fiscale == codice_fiscale:
                        return dipendente
                return None
        else:
            return None

    def eliminaDipendente(self, codice_fiscale):
        if os.path.isfile('Model/Dipendenti.pickle'):
            with open('Model/Dipendenti.pickle', 'rb') as f:
                dipendenti = list(pickle.load(f))
                for dipendente in dipendenti:
                    if dipendente.codice_fiscale == codice_fiscale:
                        dipendenti.remove(dipendente)
            with open('Model/Dipendenti.pickle', 'wb') as f:
                pickle.dump(dipendenti, f, pickle.HIGHEST_PROTOCOL)


    def iscriviVolontario(self, cellulare, codice_fiscale, cognome, data_nascita, email, nome, password, idoneita118, stato):
        volontario = Volontario(cellulare, codice_fiscale, cognome, data_nascita, email, nome, password, idoneita118, stato)
        if os.path.isfile('Model/Volontari.pickle'):
            with open('Model/Volontari.pickle', 'rb') as f:
                self.elenco_volontari = pickle.load(f)
        self.elenco_volontari.append(volontario)
        with open('Model/Volontari.pickle', 'wb') as f:
            pickle.dump(self.elenco_volontari, f, pickle.HIGHEST_PROTOCOL)

    def ricercaVolontario(self, codice_fiscale):
        if os.path.isfile('Model/Volontari.pickle'):
            with open('Model/Volontari.pickle', 'rb') as f:
                volontari = list(pickle.load(f))
                for volontario in volontari:
                    if volontario.codice_fiscale == codice_fiscale:
                        return volontario
                return None
        else:
            return None

    def eliminaVolontario(self, codice_fiscale):
        if os.path.isfile('Model/Volontari.pickle'):
            with open('Model/Volontari.pickle', 'rb') as f:
                volontari = list(pickle.load(f))
                for volontario in volontari:
                    if volontario.codice_fiscale == codice_fiscale:
                        volontari.remove(volontario)
            with open('Model/Volontari.pickle', 'wb') as f:
                pickle.dump(volontari, f, pickle.HIGHEST_PROTOCOL)

    def visualizzaRapporti(self, data):
        if os.path.isfile('Model/Rapportini.pickle'):
            with open('Model/Rapportini.pickle', 'rb') as f:
                rapportini = dict(pickle.load(f))
                for rapportino in rapportini.values():
                    if rapportino.data_servizio == data:
                        return data
                return None
        else:
            return None