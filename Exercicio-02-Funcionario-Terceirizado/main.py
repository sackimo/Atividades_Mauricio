from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox, QCheckBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
import sys

from funcionario import Funcionario
from funcionarios import Funcionarios

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Funcionarios()
    window.show()
    sys.exit(app.exec())
