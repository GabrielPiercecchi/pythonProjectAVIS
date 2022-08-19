import os.path
import pickle

import Utente
import fileinput
from CodicePython.Model.Tessera import Tessera
from CodicePython.Model.Donatore import Donatore
import datetime


class Amministratore(Utente):
    conta_tessere = 1
    elenco_tessere = []
    elenco_donatori = []
    donatore = ""

    def __init__(self, cellulare, codice_fiscale, cognome,
                 data_nascita, email, nome, password):
        Utente.Utente.__init__(self, cellulare, codice_fiscale, cognome,
                               data_nascita, email, nome, password)

    def __iscriviDonatore__(self, nome, cognome, codice_fiscale, data_nascita, cellulare, email, password,
                            gruppo_sanguigno, idoneita, num_donatori=conta_tessere):
        self.__iscriviUtente__()
        self.gruppo_sanguigno = gruppo_sanguigno
        self.idoneita = True
        if os.path.isfile('Model/Donatori.pickle'):
            with open('Model/Donatori.pickle', 'rb') as f:  #lettura
                elenco_donatori = pickle.load(f)
        elenco_donatori[num_donatori] = self
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

    def __eliminaDonatore__(self):
        if os.path.isfile('Model/Donatori.pickle'):
            with open('Model/Donatori.pickle', 'wb+') as f:
                donatori = pickle.load(f)
                del donatori[self.codice]
                pickle.dump(donatori, f, pickle.HIGHEST_PROTOCOL)
        self.__eliminaUtente__()
        self.gruppo_sanguigno = ""
        self.idoneita = ""
        del self


    def __crea_tessera__(self, conta_tessere, donatori=elenco_donatori):
        num = Tessera.__setCodice__(contatore=conta_tessere)
        conta_tessere += 1
        donatore = donatori.append()
        tessera = Tessera(codice=num, nome_donatore=donatori.nome, cognome_donatore=donatori.cognome, donazioni=[], numero_donazioni=0)
        self.elenco_tessere.append(tessera)

    def __ricercaTessera__(self, numero, elenco_tessere=elenco_tessere):
                for tessera in elenco_tessere:
                    if tessera.codice == numero:
                        return tessera
                    else:
                         return None

    def __eliminaTessera__(self, numero, elenco_tessere=elenco_tessere):
        for tessera in elenco_tessere:
            if tessera.codice == numero:
                del tessera


    def __visualizzaDisponibilita__(self):
        with open('orari.txt', 'r') as fp:
            for line in fp:
                print(line)

    def __modificaStatoDonazione__(self):  #DA FARE!!!
        replacements = {'Search1': 'Replace1', 'Search2': 'Replace2'}
        for line in fileinput.input('orari.txt', inplace=True):
            for search_for in replacements:
                replace_with = replacements[search_for]
        line = line.replace(search_for, replace_with)
        print(line, end='')
