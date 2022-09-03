import os
import pickle

from CodicePython.View.VistaVisualizzaDonazione import VistaVisualizzaDonazione
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from CodicePython.Model.Amministratore import Amministratore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton


class VistaDonazioni(QWidget):
    def __init__(self, parent=None):
        self.windowTemp = QWidget
        super(VistaDonazioni, self).__init__(parent)
        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_donazioni()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()  # layout verticale
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Donazioni")

    def load_donazioni(self):  # RICONTROLLO
            if os.path.isfile('Model/Donazioni.pickle'):
                with open('Model/Donazioni.pickle', 'rb') as f:
                    current = list(pickle.load(f))
                    self.donazioni.extend(current)

    def update_donazioni(self):
        self.donazioni = []
        self.load_donazioni()
        listview_model = QStandardItemModel(self.list_view)  # definisce come è fatta una riga
        for donazione in self.donazioni:
            item = QStandardItem()
            nome = f"{donazione.day} / {donazione.month} / {donazione.year} ' ' {donazione.hour} : {donazione.minute} - {donazione.id_donazione}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(15)
            item.setFont(font)
            listview_model.appendRow(item)
        self.list_view.setModel(listview_model)

    def show_selected_info(self):
        amministratore = Amministratore(376, "AMMINISTRATORESTUPIDO", "Paniccia",
                                        2000 - 12 - 25, "osvaldopaniccia@boh.sium", "Osvaldo", "password")

        try:
            selected = self.list_view.selectedIndexes()[0].data()
            selected = selected.split("-")[1].strip()
            print(selected)
            donazione = amministratore.visualizzaDisponibilita(selected)
            self.vista_donazione = VistaVisualizzaDonazione(donazione, elimina_callback=self.update_donazioni)
            self.vista_donazione.show()
        except IndexError:
            print("INDEX ERROR")
            return
