class Solver():

    def valid(self, board, number, position):

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

    def solve(self, board, dimension = 9):
        find = self.find_empty(board)
        
        if not find:
            return board
        else:
            row, column = find
        
        for i in range(1, dimension + 1):
            if self.valid(board, i, (row, column)):
                board[row][column] = i

                if self.solve(board):
                    return self.solve(board)
                board[row][column] = 0
        
        return False

    def print_board(self, board):
        """ Print a board 9x9  """
        for i in range(len(board)):
            #Every 3 rows print a separator
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(len(board[0])):

                #Every 3 column print a separator
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                #Check if is last column to make the jump line
                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    def find_empty(self, board):
        """ In a board find the first element empty in a tuple """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)
        return None
