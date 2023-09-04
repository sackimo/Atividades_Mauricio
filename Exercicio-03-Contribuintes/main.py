from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from telaprincipal import Ui_MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w =  QMainWindow()
    ui = Ui_MainWindow()   
    ui.setupUi(w)
    w.show()
    app.exec()