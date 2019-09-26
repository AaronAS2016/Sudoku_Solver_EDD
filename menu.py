import csv
from os import system
from reader import Reader
from solver import Solver
from writer import Writer


class Menu():

    def pedir_numero(self):

        correcto = False

        while (not correcto):
            try:
                numero = int(
                    input("Introduzca el numero de la opcion que desee ejecutar"))
                correcto = True
            except ValueError:
                print(
                    'Error, numero no valido. Introduzca el numero de la opcion que desee ejecutar')

        return numero

    def guardarSolucion(self, filepath2):
        self.sudoku_solved = sudoku.solve(board)
        self.sudoku.print_board(sudoku_solved)
        self.writer.writeAsCSV(filePath2, sudoku_solved)
        system('cls')

    def opciones(self):
        salir = False
        sudoku = Solver()
        writer = Writer()

        while not salir:
            print(
                'Bienvenido a Sudoku Solver. Lea las opciones que tiene a continuacion:')
            print('1) Ingresar la ruta del archivo con el Sudoku que desee resolver')
            print('2) recuperar ejecucion parcial y continuarla')
            print('3) Salir')

            opcion = self.pedir_numero()

            if opcion == 1:
                filePath = input("Ingrese la ruta del archivo aqui:")
                reader = Reader(filePath, ',')
                board = reader.readFileAsCSV()
                board_fixed = [[int(num) for num in sub] for sub in board]
                sudoku.print_board(board)
                print("\n")
                print("-------SOLUCION---------")
                print("\n")
                sudoku.print_board(sudoku.solve(board_fixed))

                correcto = False
                while (not correcto):
                    try:
                        guardar = str(
                            input("¿Desea guardar los resultados en un archivo csv? (Y/N)"))
                        correcto = True
                    except ValueError:
                        system('cls')
                        print('Error, ingrese y o n:')

                if guardar == 'y':
                    filePath2 = input(
                        "ingrese la ruta donde quiera guardar el archivo:")
                    self.guardarSolucion(filePath2)
                    salir = True
                elif guardar == 'n':
                    salir = True
                else:
                    print('ingrese y o n:')

            elif opcion == 2:
                print("Opcion 2")

            elif opcion == 3:
                salir = True

            else:
                print("Introduce un numero entre 1 y 4")

        print("Gracias por usar Sudoku Solver.")
