from PySide6.QtWidgets import QApplication, QWidget, QMainWindow,QTableWidget,QTableWidgetItem,QScrollArea,QTextBrowser,QFormLayout,QPushButton, QLabel,QButtonGroup, QLineEdit, QMessageBox, QCheckBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QStackedWidget
from PySide6.QtCore import QSize, QObject, QRegularExpression,QDate,QTimer,QDateTime
from PySide6.QtGui import QPixmap, QRegularExpressionValidator, QPalette, QColor
from PySide6 import QtCore
import sys


class TelaVendas(QDialog):
    def __init__(self, produtos):
        super().__init__()
        self.setWindowTitle("Vendas")
        self.setGeometry(550, 250, 400, 300)

        self.produtos = produtos
        self.produtos_vendidos = {} 

        layout = QVBoxLayout()

        self.label_info = QLabel("Selecione os produtos e quantidades vendidas:", self)
        layout.addWidget(self.label_info)

        self.tela_widget = QTableWidget(self)
        self.tela_widget.setColumnCount(4)
        self.tela_widget.setHorizontalHeaderLabels(["Nome", "Quantidade em Estoque", "Quantidade para vender", "Preço Unitário"])

        for produto, dados in self.produtos.items():
            row_position = self.tela_widget.rowCount()
            self.tela_widget.insertRow(row_position)
            self.tela_widget.setItem(row_position, 0, QTableWidgetItem(produto))
            self.tela_widget.setItem(row_position, 1, QTableWidgetItem(str(dados["quantidade"])))
            self.tela_widget.setItem(row_position, 3, QTableWidgetItem(str(dados["preco_unitario"])))

            quantidade_vendida_item = QTableWidgetItem("0")
            quantidade_vendida_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tela_widget.setItem(row_position, 2, quantidade_vendida_item)

        layout.addWidget(self.tela_widget)

        self.button_vender = QPushButton("Vender")
        self.button_vender.clicked.connect(self.realizar_venda)
        layout.addWidget(self.button_vender)

        self.setLayout(layout)

    def realizar_venda(self):
        produtos_para_remover = [] 

        for row in range(self.tela_widget.rowCount()):
            produto = self.tela_widget.item(row, 0).text()
            quantidade_vendida = int(self.tela_widget.item(row, 2).text())

            if quantidade_vendida > 0 and quantidade_vendida <= self.produtos[produto]["quantidade"]:
                self.produtos[produto]["quantidade"] -= quantidade_vendida

                if quantidade_vendida <= 0:
                    produtos_para_remover.append(produto)

                if produto in self.produtos_vendidos:
                    self.produtos_vendidos[produto] += quantidade_vendida
                else:
                    self.produtos_vendidos[produto] = quantidade_vendida

        for produto in produtos_para_remover:
            if self.produtos[produto]["quantidade"] <= 0:
                del self.produtos[produto]
                del self.produtos_vendidos[produto]

        self.atualizar_tabela_estoque()

        valor_total = 0
        for produto, quantidade in self.produtos_vendidos.items():
            valor_total += quantidade * self.produtos[produto]["preco_unitario"]

        QMessageBox.information(self, "Venda Concluída", f"Venda realizada com sucesso!\nValor Total: R${valor_total:.2f}")

    def atualizar_tabela_estoque(self):
        for row in range(self.tela_widget.rowCount()):
            produto = self.tela_widget.item(row, 0).text()
            quantidade_estoque = self.produtos[produto]["quantidade"]
            self.tela_widget.item(row, 1).setText(str(quantidade_estoque))
            self.tela_widget.item(row, 2).setText("0")


            if quantidade_estoque <= 0:
                self.tela_widget.removeRow(row)

