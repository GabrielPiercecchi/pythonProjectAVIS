from datetime import datetime

from CodicePython.Model.Amministratore import Amministratore
from CodicePython.Model.Volontario import Volontario
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class VistaInserisciVolontario(QWidget):

    def __init__(self, callback):
        super(VistaInserisciVolontario, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("codice_fiscale", "CF")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("data di nascita", "Data Nascita")
        self.add_info_text("idoneita 118", "Idoneita 118")
        self.add_info_text("email", "Email")
        self.add_info_text("cellulare", "Cellulare")
        self.add_info_text("password", "Password")
        self.add_info_text("ore annuali", "Ore Annuali")
        self.add_info_text("ore settimanali", "Ore Settimanali")
        self.add_info_text("orariolavorativo", "Orario Lavorativo")
        self.add_info_text("stato", "Stato")
        self.add_info_text("turno", "Turno")

        btn_ok = QPushButton("Ok")
        btn_ok.clicked.connect(self.aggiungi_volontario)
        self.qLines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo volontario")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def aggiungi_volontario(self):  # problema Amministratore !!!!!
        # se serve, aggiungere un try catch. In questo caso no poiche il CF può essere una stringa
        for value in self.qLines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'Errore', 'Inserire tutte le informazioni richieste', QMessageBox.Ok,
                                         QMessageBox.Ok)
                    return
        amministratore = Amministratore(376, "AMMINISTRATORESTUPIDO", "Paniccia",
                                        2000 - 12 - 25, "osvaldopaniccia@boh.sium", "Osvaldo", "password")
        try:
            nome = self.qLines["nome"].text()
            cognome = self.qLines["cognome"].text()
            codice_fiscale = self.qLines["codice_fiscale"].text()
            idoneita118 = self.qLines["idoneita 118"].text()
            data_nascita = datetime.strptime(self.qLines["data di nascita"].text(), '%Y/%m/%d')
            email = self.qLines["email"].text()
            password = self.qLines["password"].text()
            cellulare = self.qLines["cellulare"].text()
            ore_annuali = self.qLines["ore annuali"].text()
            ore_settimanali = self.qLines["ore settimanali"].text()
            orariolavorativo = self.qLines["orario lavorativo"].text()  # aggiungere specifica per datetime
            stato = self.qLines["stato"].text()
            turno = self.qLines["turno"].text()  # aggiungere specifica per datetime

            amministratore.iscriviVolontario(nome, cognome, codice_fiscale, data_nascita, cellulare, email, password,
                                             idoneita118, orariolavorativo, stato, turno, ore_annuali, ore_settimanali)
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla i dati inseriti', QMessageBox.Ok, QMessageBox.Ok)
            return
        # self.callback()
        self.close()
