import math

def find_square(board):
    for r in range(9): #0, 1, 2, ..., 8
        for c in range(9):
            if (board[r][c] == 0):
                return r, c
    return None, None

def isValid(board, guess, row, col):
    # We know the square exists now, and we have to check if there are any other numbers in the row and the column that are the same.
    row_values = board[row] # This gives a 1D list with all the values in the row.
    if (guess in row_values):
        return False

    col_values = []
    for i in range(9):
        col_values.append(board[i][col])
    if (guess in col_values):
        return False
    
    # Now we have to check if it is in the small 3x3 square.
    # For this we need to know the index of the top left and then we can iterate through it.
    starting_row_val = math.floor(row/3) * 3 # This gives a value of 0, 1, 2 
    # and then multiplies by 3 to get the starting value of the specific box
    # Do the same thing for column:
    starting_col_val = math.floor(col/3) * 3

    for r in range(starting_row_val, starting_row_val+3): # We add 3 because we only want to check 3 of the values.
    # This gives the values of starting_row_val, starting_row_val + 1, and starting_row_val + 2
    # We do the same thing for column because we are given a 2D Array
        for c in range(starting_col_val, starting_col_val + 3):
            if (guess == board[r][c]):
                return False
    
    # This means that it has passed all the tests, so we can return True as it is valid
    return True

def solve_sudoku(board):

    row, col = find_square(board) # This is step 1.

    if (row == None or col == None): # Checks if there are no empty spots
        return True # Returns true because there are no more empty spots to fill

    
    # Now we have to make a guess to fill in
    for guess in range(1, 10):
        if isValid(board, guess, row, col):
            # We know that our guess is valid, so now we can fill it into the board
            board[row][col] = guess

            # Now we can repeat the same process over and over and over again. This is simply recursion.
            if (solve_sudoku(board)):
                return True
        
    return False


example_board = [
    [3, 9, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 5],
    [0, 0, 0, 7, 1, 9, 0, 8, 0],

    [0, 5, 0, 0, 6, 8, 0, 0, 0],
    [2, 0, 6, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],

    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 7, 0, 0, 0, 5, 0, 4, 0],
    [1, 0, 9, 0, 0, 0, 2, 0, 0]
]
print(solve_sudoku(example_board))
print(example_board)