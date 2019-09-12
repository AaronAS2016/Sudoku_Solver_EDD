from solver import Solver
from reader import Reader
#TODO: Funcionalidades y requerimientos que hay que hacer
# [X] Armar la clase Solver
# [X] Pintar el tablero
# [X] Buscar casillero vacio 
# [X] Validar casillero 
# [X] Implementar solver usando backtracking
# [X] Definir estructura de datos para los archivos .csv -- AARON
# [X] Leer tableros de archivos .csv -- AARON 
# [X] Armar clase lector .csv -- AARON 
# [] Separar en varios tableros --- MICA
# [] Generar excepciones en el reader ----- Mica / Chris
# [] Escribir tableros de sudokus -- MICA
# [] Generar menues  -- MICA
# [] Registrar el tiempo de ejecución -- MICA / CHRISTIAN
# [X] Solver 9x9 
# [] Persistencia ---- A debatir
# [] Generar las soluciones en un archivo .csv---- MICA
# [] Escribir clase Writter ---- A debatir
# [] Generar test unitarios ---- Chris
# [] Calcular complejidad computacional ---- Mica / CHRIS
# [] Manejo de Excepciones ---- Chris
# [] Medicion de tiempos ---- Mica Chris #
# [] Informe ---- ya veremo

""" 
board2 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

 """
reader = Reader('resources/boards.csv', ',')

board = reader.readFileAsCSV()

sudoku = Solver()

#Un fix rapido por que los elementos que trae el reader, estan en formato Strings, ver donde ponemos esta conversion
board_fixed = [[int(num) for num in sub] for sub in board]


sudoku.print_board(board)
print("\n")
print("-------SOLUCION---------")
print("\n")
sudoku.print_board(sudoku.solve(board_fixed))
