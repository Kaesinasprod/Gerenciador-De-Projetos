from model.colaborador import Colaborador
from qt_core import *
import model.colaborador_dao as funções_colaborador
#Arquivo que controla page_colaboradores.ui

FILE_UI = "view/page_colaboradores.ui"

class PageControladorColaborador(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

    #Botões da página COLABORADORES
        self.excluir_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)

    #Fechar Janela
    def fechar_janela(self):
        self.close()

    #Salvar
    def salvar(self):
        nome = self.campo_nome.text()
        email = self.campo_email.text()

        #Cria o objeto
        novo_colaborador = Colaborador(None,nome,email)
        funções_colaborador.adicionar(novo_colaborador)
        funções_colaborador.imprime()

        #Atualiza a tabela
        self.carrega_dados()

        #Fecha a janela
        self.close()

    #Carrega os dados na tabela
    def carrega_dados(self):

        #Pega a lista de colaboradores
        lista_colaboradores = funções_colaborador.lista_colaboradores
        self.tabela.setRowCount(0)

        #Adiciona na tabela
        for colaborador in lista_colaboradores:
            self.add_linha(colaborador)
    
    def add_linha(self,colaborador):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)
    
        id = QTableWidgetItem(str(colaborador.id))
        nome = QTableWidgetItem(colaborador.nome)
        email = QTableWidgetItem(colaborador.email)

        #Imprime
        self.tabela.setItem(rowCount,0,id)
        self.tabela.setItem(rowCount,1,nome)
        self.tabela.setItem(rowCount,2,email)