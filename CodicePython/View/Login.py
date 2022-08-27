from CodicePython.View.VistaInserisciDonatore import VistaInserisciDonatore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QWidget


class Login:

    def __init__(self, callback):
        super(Login, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qLines = {}
        self.add_info_text("username", "Username")
        self.add_info_text("password", "Password")

        btn_ok = QPushButton("Ok")
        btn_ok.clicked.connect(self.login)
        self.qLines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

    def add_info_text(self, param, label): #problema
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qLines[param] = current_text
        self.v_layout.addWidget(current_text)

    def loginNuovoDonatore(self, admin):
        username = self.qLines["Username"].text()
        password = self.qLines["Password"].text()
        if admin == True:
            if username == "username" and password == "password":
                self.iscrivi_donatore = VistaInserisciDonatore(callback=VistaInserisciDonatore.aggiungi_donatore)
                self.iscrivi_donatore.show()
            else:
                QMessageBox.critical(self, 'Errore', 'Controlla i dati inseriti', QMessageBox.Ok, QMessageBox.Ok)
                return


#    def loginNuovoVolontario(self, admin):
#        username = self.qLines["Username"].text()
#        password = self.qLines["Password"].text()
#        if admin == True:
#            if username == "username" and password == "password":
#                self.iscrivi_volontario = VistaInserisciVolontario(callback=VistaVolontario.update_volontario)
#                self.iscrivi_volontario.show()
#            else:
#                QMessageBox.critical(self, 'Errore', 'Controlla i dati inseriti', QMessageBox.Ok, QMessageBox.Ok)
#                return

