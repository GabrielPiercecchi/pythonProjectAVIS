from datetime import datetime

from CodicePython.Model.Donatore import Donatore
from CodicePython.View.PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class VistaInserisciDonatore(QWidget):

    def __init__(self, callback):
        super(VistaInserisciDonatore, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("codice_fiscale", "CF")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("data di nascita", "Data Nascita")
        self.add_info_text("gruppo sanguigno", "Gruppo Sanguigno")
        self.add_info_text("email", "Email")
        self.add_info_text("cellulare", "Cellulare")
        self.add_info_text("idoneita", "Idoneita")
        self.add_info_text("password", "Password")

        btn_ok = QPushButton("Ok")
        btn_ok.clicked.connect(self.aggiungi_donatore)
        self.qLines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo donatore")


    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def aggiungi_donatore(self, amministratore=None):  #problema Amministratore !!!!!
        # se serve, aggiungere un try catch. In questo caso no poiche il CF può essere una stringa
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Inserire tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
                    return
        donatore = Donatore()
        try:
            nome = self.qLines["nome"].text()
            cognome = self.qLines["cognome"].text()
            codice_fiscale = self.qLines["CF"].text()
            gruppo_sanguigno = self.qLines["Gruppo sanguigno"].text()
            data_nascita = datetime.strptime(self.qLines["DataNascita"].text(), '%d/%m/%Y')
            email = self.qLines["Email"].text()
            cellulare = self.qLines["Cellulare"].text()
            idoneita = self.qLines["Idoneita"].text()
            password = self.qLines["Password"].text()
            amministratore.__iscriviDonatore__([], nome, cognome, codice_fiscale, data_nascita, cellulare, email, password,
                            gruppo_sanguigno, idoneita)
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla i dati inseriti', QMessageBox.Ok, QMessageBox.Ok)
            return
        self.callback()
        self.close()


