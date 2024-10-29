#el QMAinWIndow sería el frame donde se ponen los elementos
'''
aQplication nos permite comunicarnos con el sisema operativo
'''
import random
import sys
import math
from cProfile import label

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit)
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

        self.boton_ventana_ejemplo_saludo = QPushButton('Pulsame despues de introducir el nombre') #esto sería un boton


        self.label_mensaje_boton_venana_saludo = QLabel('hola a todos')
        self.boton_ventana_ejemplo_saludo.clicked.connect(self.on_boton_saudar)# con este metodo, podemos hacer que al hacer un click,  pase algo
        caixa.addWidget(self.label_mensaje_boton_venana_saludo)

        label_indica_escribe_nombre = QLabel('Introduce tu nombre')
        caixa.addWidget(label_indica_escribe_nombre)

        self.QLine_escribe_saludo = QLineEdit() #con esto introducimos un texto
        self.QLine_escribe_saludo.returnPressed.connect(self.on_boton_saudar)
        self.QLine_escribe_saludo.setPlaceholderText('Nombre aquí...')

        caixa.addWidget(self.QLine_escribe_saludo) #añadimos el texto a la caja
        caixa.addWidget(self.boton_ventana_ejemplo_saludo) #añadimos el boton al layout
        container = QWidget() #necesitamos hacer un casteo, ya que el metodo setCentralWidget solo admite un QWidget

        container.setLayout(caixa) #establecemos el layout con la caja

        self.setCentralWidget(container) #metemos el container convertido en la ventana

    '''
    Recordar que para acceder al objeto QlineEdit, tenemos 
    que meterlo en self ya que si no sería inaccesible
    '''
    def on_boton_saudar(self):
        self.boton_ventana_ejemplo_saludo.hide() #este metodo hace que el boton se oculte una vez introduciste el nombre
        self.label_mensaje_boton_venana_saludo.setText("Hola " + self.QLine_escribe_saludo.text())
        self.QLine_escribe_saludo.setText("")
        self.QLine_escribe_saludo.setEnabled(False) ##este metodo hace que el texto no sea editable

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = PrimeraVentana()
    aplicacion.exec() #ejecutamos la aplicacion


