import os
import pickle
import random

from CodicePython import Controller


class Amministratore:

    def __init__(self, utente):
        self.utente = utente
        self.accesso = Accesso.Accesso()
