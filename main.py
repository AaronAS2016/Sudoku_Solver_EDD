

from time import sleep, time
from os import system
from solver import Solver
from reader import Reader
from writer import Writer

import pickle


class SudokuSolver:

    def __init__(self):
        self._sudoku = Solver()
        self._reader = Reader()
        self._writer = Writer()
        self.iniciarJuego()

    def iniciarJuego(self):
        answer = 0
        while(answer != "4"):
            system('clear')
            self.printMenu()
            answer = input("Ingrese la opcion que quiera ejecutar: ")
            system('clear')
            if answer == "1":
                self.solverMode()
            elif answer == "2":
                self.timerMode()
            elif answer == "3":
                self.resumeSolver()

        self.terminarJuego()

    def resumeSolver(self):
        board = []
        try:
            with open('partial/board', 'rb') as resumeReader:
                board = pickle.load(resumeReader)
                sudoku_solved = self.solveBoards(board)
                saveResults = input(
                "¿Desea guardar los resultados en un archivo csv? (Y/N)")
                while(saveResults != 'N'):
                    if saveResults == 'Y':
                        filepathResult = input(
                            "¿Donde desea guardar los resultados? Ingrese el path: ")
                        self.saveResultsInCsv(sudoku_solved, filepathResult)
                    else:
                        print("Por favor ingrese una opcion valida")
                        saveResults = input(
                        "¿Desea guardar los resultados en un archivo csv? (Y/N)")
        except EnvironmentError:
            print("No se encontro una ejecución parcial previa")
            input("Presiona enter para continuar...")



    def timerMode(self):
        print("Arrancando modo Timer, midiendo tiempos...")
        dimensiones_de_tableros = [9, 16, 25, 36, 49]
        for dimension in dimensiones_de_tableros:
            self.resolver_10_soluciones_mostrando_tiempos(dimension)

    def crear_filas(self, dimension):
        return [0] * dimension

    def crear_tablero_vacio(self, dimension):
        tablero = []
        for i in range(dimension):
            tablero.append(self.crear_filas(dimension))

        return tablero

    def insertar_valor_tablero(self, tablero, fila, columna, valor):
        tablero_nuevo = tablero
        tablero_nuevo[fila][columna] = valor
        return tablero_nuevo

    def resolver_10_soluciones_mostrando_tiempos(self, dimension):
        contador_soluciones = 0

        tiempo_total = 0
        for i in range(9):
            tablero_vacio = self.crear_tablero_vacio(dimension)
            tablero_vacio = self.insertar_valor_tablero(
                tablero_vacio, contador_soluciones, contador_soluciones, dimension)

            tiempo_inicial = time()

            self._sudoku.solve(tablero_vacio, dimension)

            tiempo_final = time()

            tiempo_vuelta = tiempo_final - tiempo_inicial

            tiempo_total += tiempo_vuelta

            contador_soluciones += 1

            print("Solucion Nº" + str(contador_soluciones) + " en: " +
                  str(tiempo_vuelta) + " ejecucucion total:" + str(tiempo_total) + " - Dimension:" + str(dimension))

        tiempo_promedio = tiempo_total / dimension
        print("Tiempo promedio de la solucion: " + str(tiempo_promedio))

    def terminarJuego(self):
        system('clear')
        print("Gracias por jugar!")
        print("Apagando la magia...")
        sleep(3)
        system('clear')

    def saveResultsInCsv(self, data, filepath="resources/solve.csv"):
        system('clear')
        print("Guardandooo...")
        sleep(2)
        self._writer.writeAsCSV(filepath, data)
        print("Guardado!")

    def printMenu(self):
        print(
            "1 - Ingresar el nombre de un archivo (path completo) con la entrada de datos")
        print("2 - Modo timer")
        print("3 - Recuperar una ejecución parcial y continuarla.")
        print("4 - Salir")

    def solveBoard(self, board):
        print("El sudoku a solucionar es ...")
        print("\n")
        self._sudoku.print_board(board)
        print("\n")
        print("=========Solucion============")
        print("\n")
        sudoku_solved = self._sudoku.solve(board)

        self._sudoku.print_board(sudoku_solved)
        print("\n")

        return sudoku_solved

    def splitBoards(self, boards):

        lista = []

        lista_a_agregar = []

        contador = 0

        for fila in boards:
            contador += 1
            lista_a_agregar.append(list(map(int, fila)))
            if contador == 9:
                lista.append(lista_a_agregar)
                lista_a_agregar = []
                contador = 0
        return lista

    def solveBoards (self, board) :
        sudoku_solved = []
        if len(board) > 9:
            boards = self.splitBoards(board)
            try:
                for newboard in boards:
                    sudoku_solved += self.solveBoard(newboard)
            except KeyboardInterrupt:
                saveBoards = input("¿Quieres guardar los tableros resueltos? (Y/N)")
                if saveBoards == "Y":
                    with open('partial/boards', 'wb') as saveBoardsWriter:
                        pickle.dump(sudoku_solved, saveBoardsWriter)
        else:
            sudoku_solved += self.solveBoard(board)
        return sudoku_solved

    def solverMode(self):
        print("Bienvenido al modo solver")
        pathFile = input(
            "Ingrese el path del archivo o 0 para volver al menu principal: ")

        while pathFile != "0":

            self._reader.setFile(pathFile)
            board = self._reader.readFileAsCSV()

            system('clear')
            print("\n")

            if type(board) is not list:
                print("Tablero invalido, Por favor ponga otra ruta")
            else:
                sudoku_solved = self.solveBoards(board)
                saveResults = input(
                    "¿Desea guardar los resultados en un archivo csv? (Y/N)")
                while(saveResults != 'N'):
                    if saveResults == 'Y':
                        filepathResult = input(
                            "¿Donde desea guardar los resultados? Ingrese el path: ")
                        self.saveResultsInCsv(sudoku_solved, filepathResult)
                    else:
                        print("Por favor ingrese una opcion valida")
                        saveResults = input(
                            "¿Desea guardar los resultados en un archivo csv? (Y/N)")

            pathFile = input(
                "Ingrese el path del archivo o 0 para volver al menu principal: ")


juego = SudokuSolver()
