from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)


from juiz import Juiz
from fisico import Fisi

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(441, 528)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.juridico = QPushButton(self.centralwidget)
        self.juridico.setObjectName(u"juridico")
        self.juridico.setGeometry(QRect(40, 400, 141, 51))
        self.fisico = QPushButton(self.centralwidget)
        self.fisico.setObjectName(u"fisico")
        self.fisico.setGeometry(QRect(260, 400, 141, 51))
        self.escolha_fisic_juridico = QLabel(self.centralwidget)
        self.escolha_fisic_juridico.setObjectName(u"escolha_fisic_juridico")
        self.escolha_fisic_juridico.setGeometry(QRect(20, 160, 431, 101))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(20)
        self.escolha_fisic_juridico.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    
        self.juridico.clicked.connect(self.juri)
        self.fisico.clicked.connect(self.pessoafisica)
        
        
        
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.juridico.setText(QCoreApplication.translate("MainWindow", u"juridico", None))
        self.fisico.setText(QCoreApplication.translate("MainWindow", u"fisico", None))
        self.escolha_fisic_juridico.setText(QCoreApplication.translate("MainWindow", u"escolha se voce e juridico ou fisico", None))
    
    def juri(self,):
        self.janelajuridica = Juiz()
        self.janelajuridica.show()
        
    def pessoafisica(self):
        self.janelafisica = Fisi()
        self.janelafisica.show()

if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    app.exec()