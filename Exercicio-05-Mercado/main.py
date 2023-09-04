from PySide6.QtWidgets import QApplication, QWidget, QMainWindow,QTableWidget,QTableWidgetItem,QScrollArea,QTextBrowser,QFormLayout,QPushButton, QLabel,QButtonGroup, QLineEdit, QMessageBox, QCheckBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QStackedWidget
from PySide6.QtCore import QSize, QObject, QRegularExpression,QDate,QTimer,QDateTime
from PySide6.QtGui import QPixmap, QRegularExpressionValidator, QPalette, QColor
from PySide6 import QtCore
import sys

from telacentral import TelaCentral

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaCentral()
    window.show()
    sys.exit(app.exec())