from qt_core import *
from controller.page_colaborador import PageControladorColaborador
from controller.page_projeto import PageControladorProjeto

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui',self)
        self.colabodor_page = PageControladorColaborador()
        self.projeto_page = PageControladorProjeto()

        #Widgets
        self.painel_principal.insertWidget(0,self.colabodor_page)
        self.painel_principal.insertWidget(1,self.projeto_page)
    
        #Botões
        self.novoprojeto_btn.clicked.connect(self.show_projeto)
        self.colaborador_btn.clicked.connect(self.show_colaborador)

    def show_projeto(self):
        self.painel_principal.setCurrentIndex(1)

    def show_colaborador(self):
        self.painel_principal.setCurrentIndex(0)