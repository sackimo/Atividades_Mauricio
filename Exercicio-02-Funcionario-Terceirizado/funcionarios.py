from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox, QCheckBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
import sys

from funcionario import Funcionario

class Funcionarios(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registrar Funcionários")
        self.setGeometry(550, 220, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self)

        self.label_nome = QLabel("Nome:")
        self.layout.addWidget(self.label_nome)

        self.line_edit_nome = QLineEdit(self)
        self.layout.addWidget(self.line_edit_nome)

        self.label_horas_total = QLabel("Horas Total:")
        self.layout.addWidget(self.label_horas_total)

        self.line_edit_horas_total = QLineEdit(self)
        self.layout.addWidget(self.line_edit_horas_total)

        self.label_valor_h = QLabel("Valor por Hora:")
        self.layout.addWidget(self.label_valor_h)

        self.line_edit_valor_h = QLineEdit(self)
        self.layout.addWidget(self.line_edit_valor_h)

        self.checkbox_terceirizado = QCheckBox("Terceirizado", self)
        self.layout.addWidget(self.checkbox_terceirizado)
        self.checkbox_terceirizado.stateChanged.connect(self.surgir_despesa_adicional_das_sombras)

        self.label_despesa_adicional = QLabel("Despesa Adicional:")
        self.layout.addWidget(self.label_despesa_adicional)

        self.line_edit_despesa_adicional = QLineEdit(self)
        self.layout.addWidget(self.line_edit_despesa_adicional)

        self.button_envio = QPushButton("Enviar", self)
        self.button_envio.clicked.connect(self.cadastrar_funcionario)
        self.layout.addWidget(self.button_envio)

        self.central_widget.setLayout(self.layout)

        self.lista_funcionarios = []

    def surgir_despesa_adicional_das_sombras(self):
        if self.checkbox_terceirizado.isChecked():
            self.label_despesa_adicional.show()
            self.line_edit_despesa_adicional.show()
        else:
            self.label_despesa_adicional.hide()
            self.line_edit_despesa_adicional.hide()

    def cadastrar_funcionario(self):
        nome = self.line_edit_nome.text()
        horas_total = self.line_edit_horas_total.text()
        valor_hora = self.line_edit_valor_h.text()
        terceirizado = self.checkbox_terceirizado.isChecked()

        funcionario = Funcionario(nome, horas_total, valor_hora, terceirizado)
        self.lista_funcionarios.append(funcionario)

        self.line_edit_nome.clear()
        self.line_edit_horas_total.clear()
        self.line_edit_valor_h.clear()
        self.checkbox_terceirizado.setChecked(False)

        QMessageBox.information(self, "Sucesso", "Funcionário cadastrado com sucesso!")

    def closeEvent(self, event):
        if self.lista_funcionarios:
            mensagem = "Lista de funcionários:\n"
            for funcionario in self.lista_funcionarios:
                pagamento_original = float(funcionario.horas_total) * float(funcionario.valor_hora)
                despesa_inicial = 0.0

                if funcionario.terceirizado:
                    despesas_adicionais = self.line_edit_despesa_adicional.text()
                    if despesas_adicionais:
                        despesa_inicial = float(despesas_adicionais) * 1.1
                        pagamento_final = pagamento_original + despesa_inicial
                        mensagem += (
                            f"Nome: {funcionario.nome}, "
                            f"Pagamento Original: {pagamento_original}, "
                            f"Despesa Inicial: {despesa_inicial}, "
                            f"Pagamento Final: {pagamento_final}\n"
                        )
                    else:
                        pagamento_final = pagamento_original
                        mensagem += (
                            f"Nome: {funcionario.nome}, "
                            f"Pagamento Original: {pagamento_original}, "
                            f"Pagamento Final: {pagamento_final}\n"
                        )
                else:
                    pagamento_final = pagamento_original
                    mensagem += (
                        f"Nome: {funcionario.nome}, "
                        f"Pagamento Original: {pagamento_original}, "
                        f"Pagamento Final: {pagamento_final}\n"
                    )

            QMessageBox.information(self, "Funcionários", mensagem) 