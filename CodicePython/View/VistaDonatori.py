import os.path
import pickle

from Tools.scripts.make_ctype import values

from CodicePython.Model.Donatore import Donatore
from CodicePython.View.PyQt5.QtGui import QStandardItemModel, QStandardItem
from CodicePython.View.PyQt5.QtWidgets import QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QListView, \
    QWidget, QPushButton
from CodicePython.View.VistaInserisciDonatore import VistaInserisciDonatore


class VistaDonatori(QWidget):
    def __init__(self, parent=None):
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
        pass

    def show_new(self):
        self.iscrivi_donatore = VistaInserisciDonatore(callback=self.update_donatori)
        self.iscrivi_donatore.show()