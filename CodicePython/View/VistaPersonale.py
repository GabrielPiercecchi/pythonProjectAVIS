from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy


class VistaPersonale(QWidget):
    def __init__(self, parent=None):
        super(VistaPersonale, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Volontario", self.go_volontario), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Dipendente", self.go_dipendente), 1, 1)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Personale")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_volontario(self):
        pass

    def go_dipendente(self):
        pass
