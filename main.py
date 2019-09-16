

from solver import Solver
from reader import Reader
from writer import Writer

#import menu
import os
import time
import utils

reader = Reader('resources/boards.csv', ',')
writter = Writer()
board = reader.readFileAsCSV()

sudoku = Solver()

os.system('clear')

# Un fix rapido por que los elementos que trae el reader, estan en formato Strings, ver donde ponemos esta conversion
board_fixed = [[int(num) for num in sub] for sub in board]


def saveResultsInCsv(data, filepath="resources/solve.csv"):
    os.system('clear')
    print("Guardandooo...")
    time.sleep(2)
    writter.writeAsCSV(filepath, data)
    print("Guardado!")


def printMenu():
    print("1 - Ingresar el nombre de un archivo (path completo) con la entrada de datos")
    print("2 - Guardar la ejecución parcial, con un nombre arbitrario")
    print("3 - Recuperar una ejecución parcial y continuarla.")
    print("4 - Salir")


def solverMode():
    print("Bienvenido al modo solver")
    pathFile = input(
        "Ingrese el path del archivo o 0 para volver al menu principal: ")

    while pathFile != "0":

        reader.setFile(pathFile)
        board = reader.readFileAsCSV()

        os.system('clear')
        print("\n")

        print("El sudoku que ingreso es ...")
        print("\n")

        sudoku.print_board(board)
        print("\n")
        print("=========Solucion============")

        sudoku_solved = sudoku.solve(board)

        sudoku.print_board(sudoku_solved)
        print("\n")
        print("\n")

        saveResults = input(
            "¿Desea guardar los resultados en un archivo csv? (Y/N)")
        if saveResults == 'Y':
            filepathResult = input(
                "¿Donde desea guardar los resultados? Ingrese el path: ")
            saveResultsInCsv(sudoku_solved, filepathResult)

        pathFile = input(
            "Ingrese el path del archivo o 0 para volver al menu principal: ")


answer = 0
while(answer != "4"):
    os.system('clear')
    printMenu()
    answer = input("Ingrese la opcion que quiera ejecutar: ")
    if answer == "1":
        os.system('clear')
        solverMode()


os.system('clear')
print("Gracias por jugar!")
print("Apagando la magia...")
time.sleep(3)
os.system('clear')
