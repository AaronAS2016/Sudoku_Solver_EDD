from solver import Solver
#TODO: Funcionalidades y requerimientos que hay que hacer
# [X] Armar la clase Solver
# [X] Pintar el tablero
# [X] Buscar casillero vacio 
# [X] Validar casillero 
# [X] Implementar solver usando backtracking
# [] Definir estructura de datos para los archivos .csv -- AARON
# [] Leer tableros de archivos .csv -- AARON 
# [] Armar clase lector .csv -- AARON 
# [] Escribir tableros de sudokus -- MICA
# [] Generar menues  -- MICA
# [] Registrar el tiempo de ejecución -- MICA / CHRISTIAN
# [X] Solver 9x9 
# [] Generar las soluciones en un archivo .csv
# [] Generar test unitarios
# [] Calcular complejidad computacional
# [] Manejo de Excepciones
# [] Medicion de tiempos
# [] Informe



board = [
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



sudoku = Solver()

sudoku.print_board(board)
print(" --------SOLUCION -------------")
sudoku.print_board(sudoku.solve(board))






