import sys
from PySide6.QtWidgets import QApplication
from gerenciamento import Gerenciamento
from paciente import Paciente

#Opa professor! Igor Loureiro aqui, venho aqui admitir que usei GPT nesse codigo (não me sentiria bem não contando isso)
#O que vale pelo menos é o conhecimento que aprendemos no caminho, com esse codigo eu aprendi vários modulos novos e lógicas bizarras
#Entretanto eu só usei nas lógicas de programação do código já que era bem dificil
#De qualquer forma, fica seu critério contar esse exercicio como feito ou não por conta disso. Eu não ligo muito, eu gostei dele e aprendi muito 

#Usei GPT por desespero porque fiquei uns dias nesse codigo e não sabia qual logica aplicar. Até esquema no paint fiz mas nada

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Gerenciamento()
    window.show()
    sys.exit(app.exec())