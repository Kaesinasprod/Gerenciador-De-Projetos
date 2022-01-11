from PyQt5.uic.uiparser import QtWidgets
from qt_core import *
#Arquivo que controla page_projetos.ui

FILE_UI = "view/page_projetos.ui"

class PageControladorProjeto(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)