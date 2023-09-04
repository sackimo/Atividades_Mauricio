from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox, QCheckBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QStackedWidget
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
import sys

        
class TelaPrincipal(QMainWindow):
    def __init__(self, saldo_inicial, nome_titular, numero_conta):
        super().__init__()
        self.setWindowTitle("Tela Principal")
        self.setGeometry(750, 350, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.layout_horizontal = QHBoxLayout()

        self.button_deposito = QPushButton("Depósito", self)
        self.button_deposito.setGeometry(10,10,100,50)
        self.button_deposito.clicked.connect(self.abrir_janela_deposito)

        self.button_saque = QPushButton("Saque", self)
        self.button_saque.setGeometry(130,10,100,50)
        self.button_saque.clicked.connect(self.abrir_janela_saque)

        self.button_alterar_dados = QPushButton("Alterar Dados", self)
        self.button_alterar_dados.setGeometry(250,10,100,50)
        self.button_alterar_dados.clicked.connect(self.abrir_janela_alterar_dados)

        self.label_nome = QLabel ("Bem-Vindo(a) :",self)
        self.label_nome.setGeometry(10,80,500,50)
        self.nome = nome_titular
        self.label_nome.setText(f"Bem-Vindo(a) {self.nome}")
        
        self.label_numero = QLabel ("Seu ID é :",self)
        self.label_numero.setGeometry(10,120,500,50)
        self.numero = numero_conta
        self.label_numero.setText(f"Seu ID É {numero_conta}")
        
        
        self.label_saldo = QLabel ("Seu saldo da conta atualmente é :", self)
        self.label_saldo.setGeometry(10,160,500,50)
        self.saldo = saldo_inicial
        self.label_saldo.setText(f"Seu saldo da conta atualmente é: {self.saldo}")

        self.layout.addLayout(self.layout_horizontal)

    
    def abrir_janela_saque(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Saque")
        dialog.setGeometry(1150, 350, 400, 300)

        self.sacar_quantia = QLabel("Qual é a quantia que você deseja sacar?", dialog)
        self.sacar_quantia.setGeometry(10, 20, 380, 30)

        self.line_edit_sacar = QLineEdit(dialog)
        self.line_edit_sacar.setGeometry(10, 60, 380, 30)

        button_sacar = QPushButton("Sacar", dialog)
        button_sacar.setGeometry(10, 100, 380, 30)
        button_sacar.clicked.connect(self.sacar_dinheiro)

        dialog.exec()

    def sacar_dinheiro(self):
        quantia_saque = float(self.line_edit_sacar.text())
        taxa_saque = 5.0

        novo_saldo = self.saldo - quantia_saque - taxa_saque

        if novo_saldo >= 0:
            self.saldo = novo_saldo
        else:
            self.saldo = novo_saldo
            print("Atento! Seu saldo está se tornando negativo")
        if novo_saldo <= -100:
            print ("Você está sendo procurado pela policia!!")

        self.label_saldo.setText(f"Seu saldo da conta atualmente é: {self.saldo}")

    def abrir_janela_deposito(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Deposito")
        dialog.setGeometry(355, 350, 400, 300)

        self.depositar_quantia = QLabel("Qual é a quantia que você deseja depositar?", dialog)
        self.depositar_quantia.setGeometry(10, 20, 380, 30)

        self.line_edit_depositar = QLineEdit(dialog)
        self.line_edit_depositar.setGeometry(10, 60, 380, 30)

        button_sacar = QPushButton("Depositar", dialog)
        button_sacar.setGeometry(10, 100, 380, 30)
        button_sacar.clicked.connect(self.depositar_dinheiro)

        dialog.exec()

    def depositar_dinheiro(self):
        quantia_deposito = float(self.line_edit_depositar.text())

        self.saldo += quantia_deposito
        self.label_saldo.setText(f"Seu saldo da conta atualmente é: {self.saldo}")

        print("Depósito realizado com sucesso!")


    def abrir_janela_alterar_dados(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Alterar Dados")
        dialog.setGeometry(750, 100, 400, 200)

        self.novo_nome = QLabel("Qual será seu novo Nome Titular?", dialog)
        self.novo_nome.setGeometry(10, 20, 380, 30)

        self.line_edit_novo_nome = QLineEdit(dialog)
        self.line_edit_novo_nome.setGeometry(10, 60, 380, 30)

        button_alterar_nome = QPushButton("Alterar Nome", dialog)
        button_alterar_nome.setGeometry(10, 100, 380, 30)
        button_alterar_nome.clicked.connect(self.alterar_nome_titular)

        dialog.exec()

    def alterar_nome_titular(self):
        novo_nome_titular = self.line_edit_novo_nome.text()

        self.nome = novo_nome_titular
        self.label_nome.setText(f"Bem-Vindo(a) {self.nome}")

        print("Nome titular alterado com sucesso!")