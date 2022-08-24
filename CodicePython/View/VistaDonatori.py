import os.path
import pickle

from Tools.scripts.make_ctype import values

from CodicePython.Model.Donatore import Donatore
from CodicePython.View.PyQt5.QtGui import QStandardItemModel, QStandardItem
from CodicePython.View.PyQt5.QtWidgets import QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QListView


class VistaDonatori:
    def __init__(self, donatore, elimina_callback,):
        super(VistaDonatori, self).__init__()
        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_donatori()
        h_layout.addWidget(self.list_view)

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
