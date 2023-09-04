from PySide6.QtWidgets import QApplication, QWidget, QMainWindow,QTableWidget,QTableWidgetItem,QScrollArea,QTextBrowser,QFormLayout,QPushButton, QLabel,QButtonGroup, QLineEdit, QMessageBox, QCheckBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QStackedWidget
from PySide6.QtCore import QSize, QObject, QRegularExpression,QDate,QTimer,QDateTime
from PySide6.QtGui import QPixmap, QRegularExpressionValidator, QPalette, QColor
from PySide6 import QtCore
import sys

class TelaCadastro(QDialog):
    def __init__(self, produtos):
        super().__init__()
        self.setWindowTitle("Cadastro de Produtos")
        self.setGeometry(870, 250, 400, 300)

        layout = QVBoxLayout()

        self.label_info = QLabel("Cadastro de Produtos", self)
        layout.addWidget(self.label_info)

        form_layout = QFormLayout()

        self.input_nome = QLineEdit()
        form_layout.addRow("Nome:", self.input_nome)

        self.input_preco = QLineEdit()
        form_layout.addRow("Preço Unitário:", self.input_preco)

        self.input_quantidade = QLineEdit()
        form_layout.addRow("Quantidade em Estoque:", self.input_quantidade)

        self.button_cadastrar = QPushButton("Cadastrar")
        self.button_cadastrar.clicked.connect(self.cadastrar_produto)
        form_layout.addRow(self.button_cadastrar)

        layout.addLayout(form_layout)

        self.setLayout(layout)

        self.dados_produtos = produtos 

    def cadastrar_produto(self):
        nome = self.input_nome.text()
        preco = self.input_preco.text()
        quantidade = self.input_quantidade.text()

        if nome and preco and quantidade:
            self.dados_produtos[nome] = {
                "quantidade": int(quantidade),
                "preco_unitario": float(preco),
            }

            self.input_nome.clear()
            self.input_preco.clear()
            self.input_quantidade.clear()

            self.accept() 
