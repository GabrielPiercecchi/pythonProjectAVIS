import datetime
import os.path
import pickle
import random

from CodicePython.Model.Amministratore import Amministratore
from CodicePython.Controller.GestioneFinanze import GestioneFinanze
from CodicePython.View.LoginNuovoDonatore import LoginNuovoDonatore
from CodicePython.View.VistaVisualizzaDonatore import VistaVisualizzaDonatore
from CodicePython.View.VistaVisualizzaPagamento import VistaVisualizzaPagamento
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QListView, \
    QWidget, QPushButton
from CodicePython.Model import Amministratore


# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sample_users = [
        ["user1", "password1"],
        ["user2", "password2"],
        ["user3", "password3"]
    ]

    with open("./users.txt", "w") as users_file:
        for sample_user in sample_users:
            username = sample_user[0]
            password = sample_user[1]
            users_file.write(username + ';' + password + '\n')

    """"with open('./users.txt', 'w') as f:
        pickler = pickle.Pickler(f)
        for sample_user in sample_users:
            pickler.dump(sample_user)"""


def loginFunction():
    userEntry = ""
    foundName = False

    while userEntry == "":
        userEntry = input("Enter your username: \n")
        usersFile = open("users.txt", "r")
        for line in usersFile:
            print("This is the line I read:%s", line, )
            # Read line by line instead of loading the whole file into memory
            # In this case, it won't matter, but it's a good practice to avoid
            # running out of memory if you have reaaaally large files
            line_without_newline = line.rstrip('\n')  # Remove ending \n DA PRENDERE
            user_record = line_without_newline.split(';')  # Separate into username FORSE
            # and password (make the line a list again)
            userName = user_record[0]  # DA PRENDERE
            password = user_record[1]
            # Might as well do userName, password = line_without_newline.split(';')
            if userName == userEntry:
                foundName = True
                print("User found. Verifying password.")
                passwordEntry = input("Enter your password: \n")
                if passwordEntry == password:
                    print("Username and passwords are correct")
                    break
                else:
                    print("incorrect")
                    userEntry = ""

        if not foundName:
            print("Username not recognised")
            userEntry = ""


def loginFunction2():
    userEntry = ""

    while userEntry == "":
        userEntry = input("Enter your username: ")
        usersFile = open("users.txt", "r")
        unpickler = pickle.Unpickler(usersFile)
        while True:
            try:
                user_record = unpickler.load()
                userName = user_record[0]
                password = user_record[1]
                if userName == userEntry:
                    print("User found. Verifying password.")
                    passwordEntry = input("Enter your password: ")
                    if passwordEntry == password:
                        print("Username and passwords are correct")
                    else:
                        print("incorrect")
                        userEntry = ""
                    # Watch out for the indentation here!!
                    break  # Break anyway if the username has been found
            except EOFError:
                # Oh oh... the call to `unpickler.load` broke
                # because we reached the end of the file and
                # there's nothing else to load...
                print("Username not recognised")
                userEntry = ""
                break


if __name__ == "__main__":
    elenco_volontari = []
    elenco_dipendenti = []
    elenco_personale_idoneo = []

    with open('/home/gabriel/PycharmProjects/pythonProjectAVIS/CodicePython/Model/Volontari.pickle', 'rb') as f:  # lettura
        elenco_volontari = pickle.load(f)
    with open('/home/gabriel/PycharmProjects/pythonProjectAVIS/CodicePython/Model/Dipendenti.pickle.pickle', 'rb') as f:  # lettura
        elenco_dipendenti = pickle.load(f)

    print(elenco_dipendenti)
    print(elenco_volontari)
    elenco_personale_idoneo = elenco_dipendenti + elenco_volontari
    if len(elenco_personale_idoneo) >= 1:
        print(random.choices(elenco_personale_idoneo, k=1))
    else:
        print("Personale Insufficiente!!\n"
              "Assumerne dei nuovi.")
