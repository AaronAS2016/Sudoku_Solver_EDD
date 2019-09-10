

#TODO: Funcionalidades y requerimientos que hay que hacer
# [] Armar la clase Solver
# [X] Pintar el tablero
# [X] Buscar casillero vacio 
# [] Validar casillero 
# [] Implementar solver usando backtracking
# [] Definir estructura de datos para los archivos .csv
# [] Leer tableros de archivos .csv
# [] Escribir tableros de sudokus
# [] Generar menues 
# [] Registrar el tiempo de ejecución
# [] Solver 9x9
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

def valid(board, number, position):

    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
    #Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return board
    else:
        row, column = find
    
    for i in range(1,10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if solve(board):
                return solve(board)
            board[row][column] = 0
    
    return False

def print_board(board):
    """ Print a board 9x9  """
    for i in range(len(board)):
        #Every 3 rows print a separator
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(board[0])):

            #Every 3 column print a separator
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            #Check if is last column to make the jump line
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    """ In a board find the first element empty in a tuple """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

print_board(board)
print("------SOLUCION:-------")
print_board(solve(board))