import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox,QTableWidgetItem
from PyQt5 import uic



class Generador_Numeros(QMainWindow):
    controlador=None
    numeros_aleatorios=[]

    def __init__(self):
        super() . __init__()

        uic.loadUi("ventanaGeneradorMontecarlo.ui",self)
        #self.controlador=controladorDistribuciones()


        self.btn_generar.clicked.connect(self.accion_generar_numeros)
        self.btn_mas_100.clicked.connect(self.accion_generar_numeros_de_a_100)
        self.btn_ultimo.clicked.connect(self.accion_generar_ultimo)



    def accion_generar_numeros(self):
        return 0

    def accion_generar_numeros_de_a_100(self):
        return 0

    def accion_generar_ultimo(self):
        return  0


    def mostrar_mensaje(self, titulo, mensaje):
        # Muestro mensaje
        box = QMessageBox()
        box.setWindowTitle(titulo)
        box.setText(mensaje)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()

    def preparar_interfaz(self):
        #Actividad A
        # Cargo combo box
        self.cmb_A.clear()
        self.cmb_A.addItem(" semana 5", 0)
        self.cmb_A.addItem("semana 6", 1)
        self.cmb_A.addItem("semana7", 2)
        self.cmb_A.addItem("semana8", 3)

        #Actividad B
        self.cmb_B.clear()
        self.cmb_B.addItem("semana 3", 0)
        self.cmb_B.addItem("semana 5", 1)
        self.cmb_B.addItem("semana 7", 2)

        #Actividad C
        self.cmb_C.clear()
        self.cmb_C.addItem("semana 10", 0)
        self.cmb_C.addItem("semana 12", 1)
        self.cmb_C.addItem("semana 14", 2)
        self.cmb_C.addItem("semana 16", 3)
        self.cmb_C.addItem("semana 18", 4)

        #Actividad D
        self.cmb_D.clear()
        self.cmb_D.addItem("semana 8", 0)
        self.cmb_D.addItem("semana 10", 1)

        # Preparo tabla de numeros generados
        self.dgv_vector.setColumnCount(11)
        self.dgv_vector.setHorizontalHeaderLabels(["N° de orden", "Tiempo A", "Tiempo B", "Tiempo C",
                                                   "Tiempo D", "P(A)", "P(B)", "P(C)", "P(D)", "P(Tot)","P(acum)"])
    def limpiar_interfaz_generar_numeros(self):


        # Selecciono opcion por defecto en combo boxs
        self.cmb_A.setCurrentIndex(0)
        self.cmb_B.setCurrentIndex(0)
        self.cmb_C.setCurrentIndex(0)
        self.cmb_D.setCurrentIndex(0)

        # Limpio grilla
        self.dgv_vector.clearSelection()
        self.dgv_vector.setCurrentCell(-1, -1)
        self.dgv_vector.setRowCount(0)


    def showEvent(self, QShowEvent):
        self.preparar_interfaz()




def main():
    app= QApplication(sys.argv)
    GUI= Generador_Numeros()
    GUI.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()