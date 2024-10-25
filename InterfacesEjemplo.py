#el QMAinWIndow sería el frame donde se ponen los elementos
'''
aQplication nos permite comunicarnos con el sisema operativo
'''
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication)
from setuptools.extern import names


class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana ejemplo') #este metodo le da un titulo a la ventana
        self.setFixedSize(800, 600) #este metodo fija el tamaño de la ventana
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("purple"))
        self.setPalette(paleta)
        self.show() ##mostramos la ventana


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = PrimeraVentana()
    aplicacion.exec() #ejecutamos la aplicacion