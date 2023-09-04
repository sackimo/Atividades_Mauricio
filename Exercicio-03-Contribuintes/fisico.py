from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)
import sys


class Fisi(QWidget):
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titulo = QLabel(self.frame)
        self.titulo.setObjectName(u"titulo")
        font = QFont()
        font.setPointSize(26)
        self.titulo.setFont(font)

        self.verticalLayout.addWidget(self.titulo)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"NSimSun"])
        font1.setPointSize(26)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.nome = QLabel(self.frame_3)
        self.nome.setObjectName(u"nome")

        self.verticalLayout_2.addWidget(self.nome)

        self.digita_nome = QLineEdit(self.frame_3)
        self.digita_nome.setObjectName(u"digita_nome")

        self.verticalLayout_2.addWidget(self.digita_nome)

        self.renda_anual = QLabel(self.frame_3)
        self.renda_anual.setObjectName(u"renda_anual")

        self.verticalLayout_2.addWidget(self.renda_anual)

        self.digita_renda = QLineEdit(self.frame_3)
        self.digita_renda.setObjectName(u"digita_renda")

        self.verticalLayout_2.addWidget(self.digita_renda)

        self.gasto_saude = QLabel(self.frame_3)
        self.gasto_saude.setObjectName(u"gasto_saude")

        self.verticalLayout_2.addWidget(self.gasto_saude)

        self.digita_gasto = QLineEdit(self.frame_3)
        self.digita_gasto.setObjectName(u"digita_gasto")

        self.verticalLayout_2.addWidget(self.digita_gasto)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.envia_relatorio = QPushButton(self.centralwidget)
        self.envia_relatorio.setObjectName(u"envia_relatorio")
        self.envia_relatorio.clicked.connect(self.calculate_tax)

        self.verticalLayout_3.addWidget(self.envia_relatorio)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.mostra_resultado = QTextBrowser(self.centralwidget)
        self.mostra_resultado.setObjectName(u"mostra_resultado")

        self.verticalLayout_3.addWidget(self.mostra_resultado)
        
        self.setLayout(self.verticalLayout_3)

     

    
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"contribuintes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"fisico", None))
        self.nome.setText(QCoreApplication.translate("MainWindow", u"nome", None))
        self.digita_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite seu nome", None))
        self.renda_anual.setText(QCoreApplication.translate("MainWindow", u"renda anual", None))
        self.digita_renda.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite sua renda", None))
        self.gasto_saude.setText(QCoreApplication.translate("MainWindow", u"gasto com saude", None))
        self.digita_gasto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite seu gasto", None))
        self.envia_relatorio.setText(QCoreApplication.translate("MainWindow", u"enviar", None))

    def calculate_tax(self):
        income = float(self.digita_renda.text())
        health_expenses = float(self.digita_gasto.text())

        if income < 20000.00:
            tax_rate = 0.15
        else:
            tax_rate = 0.25

        tax_amount = income * tax_rate

        tax_amount -= 0.5 * health_expenses
        self.mostra_resultado.clear()
        self.mostra_resultado.append(f"Nome: {self.digita_nome.text()}")
        self.mostra_resultado.append(f"Renda Anual: {income:.2f}")
        self.mostra_resultado.append(f"Gastos com Saúde: {health_expenses:.2f}")
        self.mostra_resultado.append(f"Imposto a Pagar: {tax_amount:.2f}")

if __name__ == '__main__':
    aplicativo = QApplication(sys.argv)
    w = Fisi()
    w.show()
    sys.exit(aplicativo.exec_())
