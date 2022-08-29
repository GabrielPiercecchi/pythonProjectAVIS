import os.path
import pickle

 #from Tools.scripts.make_ctype import values  da vedere

from CodicePython.Model.Donatore import Donatore

from CodicePython.Model.Amministratore import Amministratore
from CodicePython.View.LoginNuovoDonatore import LoginNuovoDonatore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QListView, \
    QWidget, QPushButton
from CodicePython.View.VistaInserisciDonatore import VistaInserisciDonatore


class VistaDonatori(QWidget):
    def __init__(self, parent=None):
        self.windowTemp = QWidget
        super(VistaDonatori, self).__init__(parent)
        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_donatori()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()  #layout verticale
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton('Nuovo')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Donatori")

    def load_donatori(self):
        if os.path.isfile('Model/Donatori.pickle'):
            with open('Model/Donatori.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.donatori.extend(current, values())

    def update_donatori(self):
        self.donatori = []
        self.load_donatori()
        listview_model = QStandardItemModel(self.list_view)  #definisce come è fatta una riga
        for donatore in self.donatori:
            item = QStandardItem()
            nome = f"{donatore.nome} {donatore.cognome} {donatore.codice_fiscale} {donatore.gruppo_sanguigno}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.list_view.setModel(listview_model)

    def show_selected_info(self):
        amministratore = Amministratore(3473984100, "AMMINISTRATORESTUPIDO", "Paniccia",
                 25/12/0000, "osvaldopaniccia@boh.sium", "Osvaldo", "password")
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            codice_fiscale = selected.split("-")[1].strip().split(" ")[1]
            donatore = None
            if tipo == "Donatore":
                donatore = amministratore.ricercaDonatore(donatore)
            self.vista_donatore = VistaInserisciDonatore(donatore, elimina_callback = self.update_donatori)
            self.vista_donatore.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def show_new(self):
        self.login = LoginNuovoDonatore(callback=LoginNuovoDonatore.log)  #controllare
        self.login.show()
