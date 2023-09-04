from cadastro import Cadastro
import telaprincipal
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox, QCheckBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QStackedWidget
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
import sys

from cadastro import Cadastro
from telaprincipal import TelaPrincipal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cadastro()
    window.show()
    sys.exit(app.exec())
