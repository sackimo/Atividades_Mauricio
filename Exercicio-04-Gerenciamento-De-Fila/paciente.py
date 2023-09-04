from PySide6.QtCore import QDateTime

class Paciente:
    def __init__(self, nome, telefone, email, genero, data_nascimento, pcd):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.genero = genero
        self.data_nascimento = data_nascimento
        self.pcd = pcd
        self.data_registro = QDateTime.currentDateTime()
        self.tempo_registro = 0