from Model.Donatore import Donatore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton


class VistaVisualizzaDonatore(QWidget):
    def __init__(self, donatore, elimina_callback): #gestione visualizza ed elimina donatore
        super(VistaVisualizzaDonatore, self).__init__()
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        codice_fiscale = ""
        info = {}
        if isinstance(donatore, Donatore):
            codice_fiscale = f"Donatore {donatore.codice_fiscale}"
            info = donatore.__getInfoDonatore__()
        label_codice_fiscale = QLabel(codice_fiscale)
        font_codice_fiscale = label_codice_fiscale.font()
        font_codice_fiscale.setPointSize(30)
        label_codice_fiscale.setFont(font_codice_fiscale)
        v_layout.addWidget(label_codice_fiscale)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(QLabel(f"Nome: {info['nome']}"))
        v_layout.addWidget(QLabel(f"Cognome: {info['cognome']}"))
        v_layout.addWidget(QLabel(f"Codice fiscale: {info['codice_fiscale']}"))
        v_layout.addWidget(QLabel(f"Gruppo sanguigno: {info['Gruppo sanguigno']}"))
        v_layout.addWidget(QLabel(f"Data di nascita: {info['DataNascita']}"))
        v_layout.addWidget(QLabel(f"Email: {info['email']}"))
        v_layout.addWidget(QLabel(f"Cellulare: {info['cellulare']}"))
        v_layout.addWidget(QLabel(f"Idoneita: {info['idoneita']}"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton('Elimina')
        btn_elimina.clicked.connect(lambda: self.elimina_callback(donatore))
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle("Donatore")

    def elimina_donatore_click(self, donatore):
        if isinstance(donatore, Donatore):
            amministratore.__eliminaDonatore__() #AIUTO
        self.elimina_callback()
        self.close()







