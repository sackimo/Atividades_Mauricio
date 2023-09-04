from PySide6.QtWidgets import QApplication, QWidget, QMainWindow,QScrollArea,QTextBrowser,QPushButton, QLabel,QButtonGroup, QLineEdit, QMessageBox, QCheckBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QStackedWidget
from PySide6.QtCore import QSize, QObject, QRegularExpression,QDate,QTimer,QDateTime
from PySide6.QtGui import QPixmap, QRegularExpressionValidator
import sys
from functools import partial
import random
from paciente import Paciente

class Gerenciamento(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciamento de Fila")
        self.setGeometry(550, 250, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.button_atender = QPushButton("Atender", self)
        self.button_atender.clicked.connect(self.atender_primeiro_paciente)
        self.layout.addWidget(self.button_atender)

        self.button_cadastrar = QPushButton("Cadastrar Dados", self)
        self.button_cadastrar.setGeometry(15, 10, 145, 40)
        self.button_cadastrar.clicked.connect(self.caminho_cadastro)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_area.setWidget(self.scroll_widget)

        self.scroll_layout.addWidget(QLabel("Lista de Pacientes:"))

        self.layout.addWidget(self.button_cadastrar)
        self.layout.addWidget(self.scroll_area)
        self.central_widget.setLayout(self.layout)

        self.pacientes = []

        self.checkbox_masc = QCheckBox("Masculino")
        self.checkbox_fem = QCheckBox("Feminino")
        self.checkbox_outro = QCheckBox("Outro")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizar_tempo_na_fila)
        self.timer.start(1000)  

        

    def atender_primeiro_paciente(self):
        if self.pacientes:
            primeiro_paciente = self.pacientes[0]  
            self.mostrar_informacoes_paciente(primeiro_paciente)

            self.pacientes.pop(0)  

            mensagens_conclusao = [
            "Houve uma longa consulta apenas pro final você se der conta que o paciente estava ansioso e nenhum outro problema além tinha!",
            "Foi uma consulta rápida,o paciente mudou de ideia nos primeiros minutos por achar você 'suspeito'.",
            "Você diagnosticou com sucesso o problema do paciente e encaminhou ele para o próximo passo da consulta.",
            "O paciente não parecia bem suficiente para uma consulta, você encaminhou-o pra um setor mais adequado.",
            "Você passou uma receita para o paciente e o mesmo foi embora rapidamente.",
            "O atendimento ao paciente foi concluído.",
            "Excelente trabalho! Paciente atendido."
            ]

            mensagem_conclusao = random.choice(mensagens_conclusao)
            QMessageBox.information(self, "Atendimento Concluído", mensagem_conclusao)

            self.mostrar_pacientes()


    def caminho_cadastro(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Cadastro D' Cria")
        dialog.setGeometry(1000, 350, 400, 300)

        layout = QVBoxLayout(dialog)

        self.label_nome = QLabel("Nome Completo", dialog)
        layout.addWidget(self.label_nome)

        self.line_edit_nome = QLineEdit(dialog)
        layout.addWidget(self.line_edit_nome)

        self.label_fone = QLabel("Telefone de contato", dialog)
        layout.addWidget(self.label_fone)

        self.line_edit_fone = QLineEdit(dialog)
        layout.addWidget(self.line_edit_fone)

        self.label_email = QLabel("E-mail", dialog)
        layout.addWidget(self.label_email)

        self.line_edit_email = QLineEdit(dialog)
        layout.addWidget(self.line_edit_email)

        self.label_sexo = QLabel("Gênero")
        layout.addWidget(self.label_sexo)

        button_group = QButtonGroup()

        layout.addWidget(self.checkbox_masc)
        button_group.addButton(self.checkbox_masc)

        layout.addWidget(self.checkbox_fem)
        button_group.addButton(self.checkbox_fem)

        layout.addWidget(self.checkbox_outro)
        button_group.addButton(self.checkbox_outro)

        self.label_data = QLabel("Data de Nascimento", dialog)
        layout.addWidget(self.label_data)

        self.line_edit_data = QLineEdit(dialog)
        self.validador = QRegularExpressionValidator(QRegularExpression(r"\d{2}/\d{2}/\d{4}"), self.line_edit_data)
        self.line_edit_data.setValidator(self.validador)
        self.line_edit_data.setPlaceholderText("00/00/0000")
        layout.addWidget(self.line_edit_data)

        self.label_pcd = QLabel("PCD")
        layout.addWidget(self.label_pcd)

        self.checkbox_confirma_pcd = QCheckBox("Sim", dialog)
        layout.addWidget(self.checkbox_confirma_pcd)

        self.button_registro_paciente = QPushButton("Registrar Paciente")
        layout.addWidget(self.button_registro_paciente)

        self.button_registro_paciente.clicked.connect(self.registrar_paciente)

        dialog.exec()

    def registrar_paciente(self):
        nome = self.line_edit_nome.text()
        telefone = self.line_edit_fone.text()
        email = self.line_edit_email.text()

    
        if not nome:
            nome = "Fulano"
        if not telefone:
            telefone = "Sem Celular"
        if not email:
            email = "Não tem Gmail"

        genero = ""
        if self.checkbox_masc.isChecked():
            genero = "Masculino"
        elif self.checkbox_fem.isChecked():
            genero = "Feminino"
        elif self.checkbox_outro.isChecked():
            genero = "Outro"
        else:
            genero = "Alien" 

        data_nascimento = self.line_edit_data.text()
        if not data_nascimento:
            ano = random.randint(1950, 2000)
            mes = random.randint(1, 12)
            dia = random.randint(1, 28)  
            data_nascimento = f"{dia:02d}/{mes:02d}/{ano}"

        pcd = self.checkbox_confirma_pcd.isChecked()

        if not nome and not telefone and not email and not genero and not data_nascimento:
            nome = "Foragido"

        paciente = Paciente(nome, telefone, email, genero, data_nascimento, pcd)

        paciente.data_registro = QDateTime.currentDateTime()

        self.pacientes.append(paciente)

        self.line_edit_nome.clear()
        self.line_edit_fone.clear()
        self.line_edit_email.clear()
        self.checkbox_masc.setChecked(False)
        self.checkbox_fem.setChecked(False)
        self.checkbox_outro.setChecked(False)
        self.line_edit_data.clear()
        self.checkbox_confirma_pcd.setChecked(False)

        paciente.tempo_registro = 0

        self.mostrar_pacientes()


    def calcular_idade(self, data_nascimento):
        data_hoje = QDate.currentDate()
        partes_data = data_nascimento.split('/')
        
        if len(partes_data) == 3:
            ano_nascimento = int(partes_data[2])
            mes_nascimento = int(partes_data[1])
            dia_nascimento = int(partes_data[0])

            idade = data_hoje.year() - ano_nascimento - ((data_hoje.month(), data_hoje.day()) < (mes_nascimento, dia_nascimento))
            return idade
        else:
            return 0 

    def mostrar_pacientes(self):
        self.organizar_fila()
        
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        data_atual = QDateTime.currentDateTime() 
        for paciente in self.pacientes:
            idade = self.calcular_idade(paciente.data_nascimento)

            tempo_em_segundos = paciente.data_registro.secsTo(data_atual)
            tempo_em_minutos = tempo_em_segundos // 60
            
            paciente_info = f"Nome: {paciente.nome}, Idade: {idade}, PCD: {'Sim' if paciente.pcd else 'Não'}, Tempo na Fila: {tempo_em_segundos} segundos ({tempo_em_minutos} minutos)"

            button_paciente = QPushButton(paciente_info, self.scroll_widget)
            button_paciente.clicked.connect(partial(self.mostrar_informacoes_paciente, paciente))
            self.scroll_layout.addWidget(button_paciente)

    def organizar_fila(self):
        self.pacientes.sort(key=lambda paciente: (-int(paciente.pcd), -self.calcular_idade(paciente.data_nascimento)))

    def mostrar_informacoes_paciente(self, paciente):
        dialog = QDialog(self)
        dialog.setWindowTitle("Informações do Paciente")
        dialog.setGeometry(1000, 350, 400, 300)

        layout = QVBoxLayout(dialog)

        info_paciente = f"Nome: {paciente.nome}\nTelefone: {paciente.telefone}\nE-mail: {paciente.email}\nGênero: {paciente.genero}\nData de Nascimento: {paciente.data_nascimento}\nPCD: {'Sim' if paciente.pcd else 'Não'}"

        tempo_em_segundos = paciente.tempo_registro
        tempo_em_minutos = tempo_em_segundos // 60
        info_paciente += f"\nTempo na Fila: {tempo_em_segundos} segundos ({tempo_em_minutos} minutos)"

        text_browser = QTextBrowser()
        text_browser.setPlainText(info_paciente)
        layout.addWidget(text_browser)

        dialog.exec()

    def atualizar_tempo_na_fila(self):
        for paciente in self.pacientes:
            paciente.tempo_registro += 1

            if paciente.tempo_registro > 900:  # 15 minutos em segundos
                self.mostrar_notificacao_espera(paciente)
                self.pacientes.remove(paciente)
                self.pacientes.insert(0, paciente)

            if paciente.tempo_registro == 30:
                self.mostrar_notificacao_espera(paciente)

        self.mostrar_pacientes()

   

    def atender_paciente(self, paciente):
        self.pacientes.remove(paciente)
        self.mostrar_pacientes()

    def mostrar_notificacao_espera(self, paciente):
        mensagem = f"O paciente {paciente.nome} está pronto para ser atendido!"
        QMessageBox.information(self, "Paciente Pronto", mensagem)