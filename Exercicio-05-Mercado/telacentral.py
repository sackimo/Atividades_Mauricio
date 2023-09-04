from PySide6.QtWidgets import QApplication, QWidget, QMainWindow,QTableWidget,QTableWidgetItem,QScrollArea,QTextBrowser,QFormLayout,QPushButton, QLabel,QButtonGroup, QLineEdit, QMessageBox, QCheckBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QStackedWidget
from PySide6.QtCore import QSize, QObject, QRegularExpression,QDate,QTimer,QDateTime
from PySide6.QtGui import QPixmap, QRegularExpressionValidator, QPalette, QColor
from PySide6 import QtCore
import sys

from telacadastro import TelaCadastro
from telaestoque import TelaEstoque
from telavendas import TelaVendas


class TelaCentral(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Central")
        self.setGeometry(550, 250, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_info = QLabel("Gestão de um Mercado", self)
        self.label_info.setGeometry(135, 5, 150, 10)

        self.button_cadastro = QPushButton("Cadastro", self)
        self.button_cadastro.setStyleSheet("background-color: green; color: white;")
        self.button_cadastro.clicked.connect(self.mostrar_janela_cadastro)
        self.layout.addWidget(self.button_cadastro)

        self.button_estoque = QPushButton("Estoque", self)
        self.button_estoque.setStyleSheet("background-color: green; color: white;")
        self.button_estoque.clicked.connect(self.mostrar_janela_estoque)
        self.layout.addWidget(self.button_estoque)

        self.button_vendas = QPushButton("Vendas", self)
        self.button_vendas.setStyleSheet("background-color: green; color: white;")
        self.button_vendas.clicked.connect(self.mostrar_janela_vendas)  
        self.layout.addWidget(self.button_vendas)

        self.central_widget.setLayout(self.layout)

        self.tela_cadastro = None

        self.produtos = {}

    def mostrar_janela_cadastro(self):
        self.tela_cadastro = TelaCadastro(self.produtos)
        if self.tela_cadastro.exec() == QDialog.Accepted:
            pass 
    def mostrar_janela_estoque(self):
        if not self.tela_cadastro:
            return

        self.atualizar_estoque()
        janela_estoque = TelaEstoque(self.produtos)  
        janela_estoque.exec()

    def mostrar_janela_vendas(self):
        if not self.tela_cadastro:
            return

        janela_vendas = TelaVendas(self.produtos)
        janela_vendas.exec()

    def atualizar_estoque(self):

        if self.tela_cadastro:
            self.produtos = self.tela_cadastro.dados_produtos
