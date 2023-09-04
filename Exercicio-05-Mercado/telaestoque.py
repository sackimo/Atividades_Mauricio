from PySide6.QtWidgets import QApplication, QWidget, QMainWindow,QTableWidget,QTableWidgetItem,QScrollArea,QTextBrowser,QFormLayout,QPushButton, QLabel,QButtonGroup, QLineEdit, QMessageBox, QCheckBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QStackedWidget
from PySide6.QtCore import QSize, QObject, QRegularExpression,QDate,QTimer,QDateTime
from PySide6.QtGui import QPixmap, QRegularExpressionValidator, QPalette, QColor
from PySide6 import QtCore
import sys

class TelaEstoque(QDialog):
    def __init__(self, produtos):
        super().__init__()
        self.setWindowTitle("Estoque")
        self.setGeometry(550, 250, 400, 300)

        layout = QVBoxLayout()

        self.label_info = QLabel("Produtos em estoque atualmente: ", self)
        layout.addWidget(self.label_info)

        self.tela_widget = QTableWidget(self)
        self.tela_widget.setColumnCount(3) 
        self.tela_widget.setHorizontalHeaderLabels(["Nome", "Quantidade", "Preço Unitário"])

        for produto, dados in produtos.items():
            row_position = self.tela_widget.rowCount()
            self.tela_widget.insertRow(row_position)
            self.tela_widget.setItem(row_position, 0, QTableWidgetItem(produto))
            self.tela_widget.setItem(row_position, 1, QTableWidgetItem(str(dados["quantidade"])))
            self.tela_widget.setItem(row_position, 2, QTableWidgetItem(str(dados["preco_unitario"])))

        layout.addWidget(self.tela_widget)

        self.setLayout(layout)
