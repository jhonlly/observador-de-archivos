import time, threading, sys

from PyQt5 import uic,QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog,QMessageBox
import servicios

class UsuarioUI(QMainWindow):

    _file_name= ''
    
#TODO: Refactorizar.
    def __init__(self):
        super(UsuarioUI, self).__init__()
        uic.loadUi('front_usuario.ui', self)
        self.boton_selecionar_carpeta.clicked.connect(self.fn_selecionar_carpeta)
        self.boton_iniciar.clicked.connect(self.fn_iniciar)
        self.boton_parar.clicked.connect(self.fn_parar)
        self.boton_iniciar.setEnabled(False)
        self.boton_parar.setEnabled(False)
        self._supervisor_instancia = servicios.Watcher()
        self._t = None

        
    def fn_selecionar_carpeta(self):
        self.file_name = QFileDialog.getExistingDirectory(self,'Selecionar Carpeta', QtCore.QDir.rootPath())
        self.label_direccion_carpeta.setText(self.file_name)
        if(self.file_name != ''):
            self.boton_iniciar.setEnabled(True)
            

    def fn_inicio_supervision(self):
        self._supervisor_instancia.run(self.file_name)
 
    def fn_parar_supervision(self):
        self._t._delete()
        self._supervisor_instancia.stop()
    
    #TODO: Añadir funcionalidad para volver a iniciar la supervision.
    def fn_iniciar(self):
        self.boton_parar.setEnabled(True)
        self.boton_iniciar.setEnabled(False)
        self._t = threading.Thread(name="fn_inicio_supervision", target=self.fn_inicio_supervision)
        self._t.start()

    def fn_parar(self):
        self.fn_parar_supervision()
        self.boton_iniciar.setEnabled(True)
        self.boton_parar.setEnabled(False)
        #TODO: Poner Widget en una clase aparte.
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Información")
        msgBox.setText("Se ha detenido correctamente la supervicion de la carpeta")
        msgBox.exec()
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = UsuarioUI()
    GUI.show()
    sys.exit(app.exec())