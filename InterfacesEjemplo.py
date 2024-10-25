#el QMAinWIndow sería el frame donde se ponen los elementos
'''
aQplication nos permite comunicarnos con el sisema operativo
'''
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget)
from setuptools.extern import names


class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana ejemplo') #este metodo le da un titulo a la ventana
        self.setFixedSize(800, 600) #este metodo fija el tamaño de la ventana
        paleta = self.palette() #obtenemos el color de la paleta
        paleta.setColor(QPalette.ColorRole.Window, QColor("purple")) #cambiamos el color con la variabñe
        self.setPalette(paleta) #establecemos el nuevo color con la paleta
        self.show() ##mostramos la ventana
        caixa = QVBoxLayout() #esto es un layout
        boton_ventana_ejemplo_saludo = QPushButton('saludo') #esto sería un boton
        caixa.addWidget(boton_ventana_ejemplo_saludo) #añadimos el boton al layout

        container = QWidget() #necesitamos hacer un casteo, ya que el metodo setCentralWidget solo admite un QWidget
        container.setLayout(caixa) #establecemos el layout con la caja
        self.setCentralWidget(container) #metemos el container convertido en la ventana


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = PrimeraVentana()
    aplicacion.exec() #ejecutamos la aplicacion