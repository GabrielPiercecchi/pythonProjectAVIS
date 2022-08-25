from View.VistaDonatori import VistaDonatori
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Gestisci amministratore", self.go_amministratore), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Gestisci donatori", self.go_donatori), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Gestisci personale", self.go_personale), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Gestisci sistema", self.go_sistema), 1, 1)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("AVIS")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_amministratore(self):
        pass

    def go_donatori(self):
        self.vista_donatori = VistaDonatori()
        self.vista_donatori.show()

    def go_personale(self):
        pass

    def go_sistema(self):
        pass
