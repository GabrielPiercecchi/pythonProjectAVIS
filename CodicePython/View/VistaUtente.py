from CodicePython.Model.Utente import Utente
from CodicePython.View.PyQt5.QtWidgets import QVBoxLayout, QLabel, QSpacerItem, QSizePolicy


class VistaUtente:
    def __init__(self, utente, elimina_callback,):
        super(VistaUtente, self).__init__()
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        codice_fiscale = ""
        info = {}
        if isinstance(utente, Utente):
            nome = f"Utente {utente.codice_fiscale}"
            info = utente.getinfoUtente()
        label_codice_fiscale = QLabel(codice_fiscale)
        font_codice_fiscale = label_codice_fiscale.font()
        font_codice_fiscale.setPointSize(30)
        label_codice_fiscale.setFont(font_codice_fiscale)
        v_layout.addWidget(label_codice_fiscale)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(QLabel(f"Codice Fiscale : {info['codice_fiscale']}"))
        v_layout.addWidget((QLabel(f"Nome : {info['nome']}")))
        # etc...
