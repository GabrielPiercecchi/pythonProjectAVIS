import os.path
import pickle

import Utente
import fileinput

from CodicePython.Model.Donazione import Donazione
from CodicePython.Model.Tessera import Tessera
from CodicePython.Model.Donatore import Donatore
import datetime


class Amministratore(Utente):

    conta_tessere = 1
    donatore = ""
    elenco_donatori = []

    def __init__(self, cellulare, codice_fiscale, cognome,
                 data_nascita, email, nome, password):
        Utente.Utente.__init__(self, cellulare, codice_fiscale, cognome,
                               data_nascita, email, nome, password)

    def __iscriviDonatore__(self, nome, cognome, codice_fiscale, data_nascita, cellulare, email, password,
                            gruppo_sanguigno):
        donatore = Donatore(nome, cognome, codice_fiscale, data_nascita, cellulare, email, password,
                            gruppo_sanguigno, idoneita= True)
        if os.path.isfile('Model/Donatori.pickle'):
            with open('Model/Donatori.pickle', 'rb') as f:  #lettura
                elenco_donatori = pickle.load(f)
        elenco_donatori.append(donatore)
        with open('Model/Donatori.pickle', 'wb') as f:
            pickle.dump(elenco_donatori, f, pickle.HIGHEST_PROTOCOL)

    def __ricercaDonatore__(self, codice_fiscale):
        if os.path.isfile('Model/Donatori.pickle'):
            with open('Model/Donatori.pickle', 'rb') as f:
                donatori = dict(pickle.load(f))
                for donatore in donatori.values():
                    if donatore.codice_fiscale == codice_fiscale:
                        return donatore
                return None
        else:
            return None

    def __eliminaDonatore__(self, codice_fiscale):
        if os.path.isfile('Model/Donatori.pickle'):
            with open('Model/Donatori.pickle', 'wb+') as f:
                donatori = dict(pickle.load(f))
                for donatore in donatori.values():
                    if donatore.codice_fiscale == codice_fiscale:
                        donatori.pop(donatore)
                pickle.dump(donatori, f, pickle.HIGHEST_PROTOCOL)


    def __crea_tessera__(self, conta_tessere, nome, cognome):
        tessera = Tessera(conta_tessere, nome, cognome, donazioni = [], numero_donazioni=0)
        #continua dopo

        if os.path.isfile('Model/Tessere.pickle'):
            with open('Model/Tessere.pickle', 'rb') as f:  # lettura
                tessere = pickle.load(f)
        tessere[conta_tessere] = Tessera()
        with open('Model/Tessere.pickle', 'wb') as f:
            pickle.dump(tessere, f, pickle.HIGHEST_PROTOCOL)
        conta_tessere += 1


    def __ricercaTessera__(self, numero, elenco_tessere=elenco_tessere): #todo
                for tessera in elenco_tessere:
                    if tessera.codice == numero:
                        return tessera
                    else:
                         return None

    def __eliminaTessera__(self, numero, elenco_tessere=elenco_tessere): #todo
        for tessera in elenco_tessere:
            if tessera.codice == numero:
                del tessera


    def __visualizzaDisponibilita__(self):
        orario = []
        with open('orari.txt', 'r') as fp:
            for line in fp:
                orario.append(line)
        return orario


    def __modificaStatoDonazione__(self, anno: int, mese: int, giorno: int, ora: int, minuto: int, donatore: int):  #DA FARE!!!
        donazioni = []
        with open('orari.txt', 'r') as fp:
            for line in fp: #problema
                donazione = Donazione(year= , month= , day= , hour= , minute= , disponibile= )  #aggiungere attributo???
                donazioni.append(donazione)
            for donazione in donazioni:
                if donazione.year == anno and donazione.month == mese and donazione.day == giorno and donazione.hour == ora and donazione.minute == minuto:
                    if donatore == 0:
                        Donazione.disponibile = True
                        #modifica tessera donatore
                    else:
                        Donazione.disponibile = False
                        #modifica tessera donatore
        with open('orari.txt', 'w') as fp:
            for donazione in donazioni:
                fp.write(str(donazione.year) + ' ' + str(donazione.month) + ' ' + str(donazione.day) + ' ' + str(donazione.hour) + ' ' + str(donazione.minute) + ' ' + str(donazione.disponibile))






