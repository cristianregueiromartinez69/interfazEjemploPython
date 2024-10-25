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
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel)
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
        boton_ventana_ejemplo_saludo = QPushButton('ola bebe') #esto sería un boton
        self.label_mensaje_boton_venana_saludo = QLabel('hola')
        boton_ventana_ejemplo_saludo.clicked.connect(self.on_boton_saudar)# con este metodo, podemos hacer que al hacer un click,  pase algo
        caixa.addWidget(boton_ventana_ejemplo_saludo) #añadimos el boton al layout
        caixa.addWidget(self.label_mensaje_boton_venana_saludo)
        container = QWidget() #necesitamos hacer un casteo, ya que el metodo setCentralWidget solo admite un QWidget
        container.setLayout(caixa) #establecemos el layout con la caja
        self.setCentralWidget(container) #metemos el container convertido en la ventana

    def on_boton_saudar(self):
        lista_mensajes = ["hola bebe", "adios bebe", "jajajaja", "vinicus balon de oro"]
        self.label_mensaje_boton_venana_saludo.setText(lista_mensajes[random.randint(0,len(lista_mensajes)-1)])

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = PrimeraVentana()
    aplicacion.exec() #ejecutamos la aplicacion


'''
Tareas: 
1. crear ub objeto QLabel
2. incluirlo en la ventana (layout)
3. que salga un mensaje en la etiqueta
4. buscar un método para escribir en la etiqueta y cambiarle el texto
5. cuando el usuario pulse el boton, cambiar el texto
'''