from qt_core import *
from controller.main_window import MainWindow
from controller.page_projeto import PageControladorProjeto
from controller.page_colaborador import PageControladorColaborador

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()