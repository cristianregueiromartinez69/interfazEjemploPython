#el QMAinWIndow sería el frame donde se ponen los elementos
'''
aQplication nos permite comunicarnos con el sisema operativo
'''
import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication)
from setuptools.extern import names


class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = PrimeraVentana()
    aplicacion.exec()