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

class Juiz(QWidget):
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titulo = QLabel(self.frame)
        self.titulo.setObjectName(u"titulo")
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold"])
        font.setPointSize(28)
        font.setBold(True)
        self.titulo.setFont(font)

        self.verticalLayout_2.addWidget(self.titulo)

        self.espaco1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.espaco1)

        self.titulo_juridico = QLabel(self.frame)
        self.titulo_juridico.setObjectName(u"titulo_juridico")
        font1 = QFont()
        font1.setPointSize(24)
        self.titulo_juridico.setFont(font1)

        self.verticalLayout_2.addWidget(self.titulo_juridico)

        self.espaco2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.espaco2)

        self.nome = QLabel(self.frame)
        self.nome.setObjectName(u"nome")
        font2 = QFont()
        font2.setPointSize(11)
        self.nome.setFont(font2)

        self.verticalLayout_2.addWidget(self.nome)

        self.digita_nome = QLineEdit(self.frame)
        self.digita_nome.setObjectName(u"digita_nome")

        self.verticalLayout_2.addWidget(self.digita_nome)

        self.renda_anual = QLabel(self.frame)
        self.renda_anual.setObjectName(u"renda_anual")
        self.renda_anual.setFont(font2)

        self.verticalLayout_2.addWidget(self.renda_anual)

        self.digita_renda = QLineEdit(self.frame)
        self.digita_renda.setObjectName(u"digita_renda")

        self.verticalLayout_2.addWidget(self.digita_renda)

        self.funcionarios = QLabel(self.frame)
        self.funcionarios.setObjectName(u"funcionarios")
        self.funcionarios.setFont(font2)

        self.verticalLayout_2.addWidget(self.funcionarios)

        self.digita_funcionarios = QLineEdit(self.frame)
        self.digita_funcionarios.setObjectName(u"digita_funcionarios")

        self.verticalLayout_2.addWidget(self.digita_funcionarios)

        self.espaco3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.espaco3)

        self.envia_relatorio = QPushButton(self.frame)
        self.envia_relatorio.setObjectName(u"envia_relatorio")

        self.verticalLayout_2.addWidget(self.envia_relatorio)

        self.espaco4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.espaco4)


        self.verticalLayout.addWidget(self.frame)

        self.resultados = QTextBrowser(self.centralwidget)
        self.resultados.setObjectName(u"resultados")

        self.verticalLayout_2.addWidget(self.resultados)
        
        self.setLayout(self.verticalLayout_2)
        
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"contribuintes", None))
        self.titulo_juridico.setText(QCoreApplication.translate("MainWindow", u"juridico", None))
        self.nome.setText(QCoreApplication.translate("MainWindow", u"nome", None))
        self.digita_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite seu nome", None))
        self.renda_anual.setText(QCoreApplication.translate("MainWindow", u"renda anual", None))
        self.digita_renda.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite a renda anual", None))
        self.funcionarios.setText(QCoreApplication.translate("MainWindow", u"numeros de funcionarios", None))
        self.digita_funcionarios.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite o numero de funcionarios", None))
        self.envia_relatorio.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        
        
       
        self.envia_relatorio.clicked.connect(self.conta_pessoaJuridica)
        
        self.return_pJuridica = QLabel(self)
        self.return_pJuridica.setGeometry(30, 250, 200, 30)
        

    def conta_pessoaJuridica(self):
        try:

            renda_anual_str = self.digita_renda.text()
            numDeFunc_str = self.digita_funcionarios.text()
            

            renda_anual = float(renda_anual_str)
            numDeFunc = float(numDeFunc_str)
            
            if numDeFunc <= 10:
                imposto = 0.16 * renda_anual
                self.return_pJuridica.setText("Seu imposto ficou %.2f" % imposto)
                self.verticalLayout_2.addWidget(self.return_pJuridica)
            elif numDeFunc > 10:
                imposto = 0.14 * renda_anual
                self.return_pJuridica.setText("Seu imposto ficou %.2f" % imposto)
                self.verticalLayout_2.addWidget(self.return_pJuridica)
        except ValueError:

            self.return_pJuridica.setText("Entrada inválida")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Juiz()
    window.show()
    sys.exit(app.exec())