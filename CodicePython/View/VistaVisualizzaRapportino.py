from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy


class VistaVisualizzaRapportino(QWidget):
    def __init__(self, rapportino, elimina_callback): #gestione visualizza ed elimina donatore
        super(VistaVisualizzaRapportino, self).__init__()
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        codice_fiscale = f"{rapportino.data_servizio}"
        label_codice_fiscale = QLabel(codice_fiscale)
        font_codice_fiscale = label_codice_fiscale.font()
        font_codice_fiscale.setPointSize(30)
        label_codice_fiscale.setFont(font_codice_fiscale)
        v_layout.addWidget(label_codice_fiscale)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(QLabel(f"Data: {rapportino.data_servizio}"))
        v_layout.addWidget(QLabel(f"KM Iniziali: {rapportino.KM_inizio}"))
        v_layout.addWidget(QLabel(f"KM Finali: {rapportino.KM_fine}"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(v_layout)
        self.setWindowTitle("Rapportino")