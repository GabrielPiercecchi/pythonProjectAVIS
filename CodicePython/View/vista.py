from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy


class vista(QWidget):

    def __init__(self, parent=None):
        super(vista, self).__init__(parent)
        grid_layout = QGridLayout()

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)

    def go_amministratore(self):
        pass