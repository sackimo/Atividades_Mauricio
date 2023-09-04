from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox, QCheckBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QStackedWidget
from PySide6.QtCore import QSize, QObject
from PySide6.QtGui import QPixmap
import sys

from telaprincipal import TelaPrincipal

class Cadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Conta Bancária")
        self.setGeometry(550, 250, 400, 300)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        
        self.label_numero_conta = QLabel("Número da Conta :")
        self.layout.addWidget(self.label_numero_conta)
        
        self.line_edit_numero_conta = QLineEdit(self)
        self.layout.addWidget(self.line_edit_numero_conta)

        self.label_titular = QLabel("Nome do Titular :")
        self.layout.addWidget(self.label_titular)
        
        self.line_edit_titular = QLineEdit(self)
        self.layout.addWidget(self.line_edit_titular)

        self.label_deseja_inicial = QLabel("Você deseja informar seu Depósito inicial? (Caso não, será 0)")
        self.layout.addWidget(self.label_deseja_inicial)

        self.checkbox_sim_deposito = QCheckBox("Sim", self)
        self.layout.addWidget(self.checkbox_sim_deposito)
        self.checkbox_sim_deposito.stateChanged.connect(self.mostrar_ocultar_valor_inicial)

        self.checkbox_nao_deposito = QCheckBox("Não", self)
        self.layout.addWidget(self.checkbox_nao_deposito)
        self.checkbox_nao_deposito.stateChanged.connect(self.mostrar_ocultar_valor_inicial)

        self.label_valor_inicial = QLabel("Valor do Depósito Inicial :")
        self.layout.addWidget(self.label_valor_inicial)

        self.line_edit_valor_inicial = QLineEdit(self)
        self.layout.addWidget(self.line_edit_valor_inicial)

        self.button_cadastrar = QPushButton("Cadastrar", self)
        self.layout.addWidget(self.button_cadastrar)
        self.button_cadastrar.clicked.connect(self.caminho_janela)

        self.central_widget.setLayout(self.layout)
        


    def mostrar_ocultar_valor_inicial(self):
        if self.checkbox_sim_deposito.isChecked() and self.checkbox_nao_deposito.isChecked():
            if self.sender() == self.checkbox_sim_deposito:
                self.checkbox_nao_deposito.setChecked(False)
            else:
                self.checkbox_sim_deposito.setChecked(False)

            if self.checkbox_sim_deposito.isChecked():
                self.label_valor_inicial.show()
                self.line_edit_valor_inicial.show()
            else:
                self.label_valor_inicial.hide()
                self.line_edit_valor_inicial.hide()


    def caminho_janela(self):
        valor_inicial = float(self.line_edit_valor_inicial.text()) if self.line_edit_valor_inicial.text() else 0.0
        nome_titular = str(self.line_edit_titular.text()) if self.line_edit_titular.text() else "Não-Definido"
        numero_conta = int(self.line_edit_numero_conta.text()) if self.line_edit_numero_conta.text() else "123456789"

        self.secondary_window = TelaPrincipal(valor_inicial, nome_titular, numero_conta)
        self.secondary_window.show()
        
