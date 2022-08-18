import os
import pickle
import random
from CodicePython.Model.Tessera import Tessera


class Amministratore:
    # conta_tessere = 1
    elencoTessere = []

    def __init__(self, utente):
        self.utente = utente

    def __iscrivi_donatore__(self):
        pass  # al momento vuoto, da compilare in seguito

    def __crea_tessera__(self, conta_tessere):
        num = Tessera.__setCodice__(contatore=conta_tessere)
        conta_tessere += 1
        tessera = Tessera(codice=num, nome_donatore=nome, cognome_donatore=cognome, donazioni=[], numero_donazioni=0)
        self.elencoTessere.append(tessera)
