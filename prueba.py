from solver import Solver
from reader import Reader
import pickle
import csv
class Prueba:

    
    def __init__(self):
        self._sudoku = Solver()
        self._reader = Reader()
        self.iniciar()

    def iniciar(self):
        pathFile = 'boards.csv'
        self._reader.setFile(pathFile)
        board = self._reader.readFileAsCSV()
        self.solveBoards(board)

    def readFileAsCSV(self, delimiter=None):

        # Use the default delimiter
        if delimiter is None:
            delimiter = self._delimiter

        if(self.checkIfExistFile()):

            try:
                with open(self._filepath, 'r') as readerCsv:
                    reader = csv.reader(readerCsv, delimiter=delimiter)
                    data = []
                    for row in reader:
                        row = [int(i) for i in row]
                        data.append(row)

            except ValueError:
                print("Error trying to read the file: " + ValueError)
            return data
        else:
            raise ValueError("Ups!, The filepath looks wrong, try to change the filepath")

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
            for newboard in boards:
                sudoku_solved += self.solveBoards(newboard)
        else:
            sudoku_solved += self.solveBoard(board)
        return sudoku_solved
    
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
    
prueba = Prueba()
    








