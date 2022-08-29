import os
import pickle

from CodicePython.View.LoginNuovoVolontario import LoginNuovoVolontario
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton


class VistaVolontario(QWidget):
    def __init__(self, parent=None):
        self.windowTemp = QWidget
        super(VistaVolontario, self).__init__(parent)
        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_volontari()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()  # layout verticale
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
        self.setWindowTitle("Volontari")

    def load_volontari(self):
        if os.path.isfile('Model/Volontari.pickle'):
            with open('Model/Volontari.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.volontari.extend(current, values())

    def update_volontari(self):
        self.volontari = []

    def show_selected_info(self):
        pass

    def show_new(self):
        self.login = LoginNuovoVolontario(callback=LoginNuovoVolontario.log)  # controllare
        self.login.show()