

from solver import Solver
from reader import Reader
import menu
import os
import time

reader = Reader('resources/boards.csv', ',')

board = reader.readFileAsCSV()

sudoku = Solver()

os.system('clear')
# Un fix rapido por que los elementos que trae el reader, estan en formato Strings, ver donde ponemos esta conversion

board_fixed = [[int(num) for num in sub] for sub in board]


def printMenu():
    print("1 - Ingresar el nombre de un archivo (path completo) con la entrada de datos")
    print("2 - Guardar la ejecución parcial, con un nombre arbitrario")
    print("3 - Recuperar una ejecución parcial y continuarla.")
    print("4 - Salir")


def solverMode():
    pass


answer = 0
while(answer != "4"):
    printMenu()
    answer = input("Ingrese la opcion que quiera ejecutar: ")
    if answer == "1":
        solverMode()


os.system('clear')
print("Gracias por jugar!")
print("Apagando la magia...")
time.sleep(3)
os.system('clear')
