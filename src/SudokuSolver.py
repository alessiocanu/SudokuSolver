"""
Sudoku Solver
This program takes a sudoku board and he resolves it using the backtracking algorithm
"""
board = [[0, 7, 2, 0, 0, 4, 9, 0, 0],
         [3, 0, 4, 0, 8, 9, 1, 0, 0],
         [8, 1, 9, 0, 0, 6, 2, 5, 4],
         [7, 0, 1, 0, 0, 0, 0, 9, 5],
         [9, 0, 0, 0, 0, 2, 0, 7, 0],
         [0, 0, 0, 8, 0, 7, 0, 1, 2],
         [4, 0, 5, 0, 0, 1, 6, 2, 0],
         [2, 3, 7, 0, 0, 0, 5, 0, 1],
         [0, 0, 0, 0, 2, 5, 7, 0, 0]]


def print_board():
    """
    Function that prints the board on the terminal
    """
    for i in range(0, 9):
        print(board[i])


def find_empty(coord):
    """
    Function that search the board for an empty box
    :param coord: array of two numbers
    :return: True if finds an empty box, False if not
    """
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                coord[0] = i
                coord[1] = j
                return True
    return False


def is_correct(coord, value):
    """
    Function to check if the number placed is correct or not, according to Sudoku's rules
    (No equal numbers on the same row, column or single boxes 3x3)
    :param coord: coord of the previosly found empty box
    :param value: number placed
    :return: True if the number is placed correctly, False if not
    """
    # Checks for equal numbers on same row or column
    for i in range(0, 9):
        if value == board[coord[0]][i] and coord[1] != i:
            return False
    for i in range(0, 9):
        if value == board[i][coord[1]] and coord[0] != i:
            return False

    # Finds the box 3x3 using the empty box's coord
    box_x = coord[0] // 3
    box_y = coord[1] // 3
    # Checks for equal numbers in the box
    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if board[i][j] == value and coord != (i, j):
                return False
    return True


def resolve():
    """
    Function that applies the backtracking algorithm to find the solution recursively
    1) Check for an empty box, if found proceed, if not the Sudoku is resolved
    2) Try, from 1 to 9, to place the number in the empty box
    3) If the number can be placed, repeat from Step 1
    4) If the number can't be placed, try the next number until 9
    5) If even the 9 can't be placed, erase any symbol from the current box, and go back to the previous one
    6) Try, in the previous one, the next value (i.g if it was 6, try 7) (this is basically Step 2)
    7) Repeat until done
    :return: True if the number could be placed and it can proceed on the next one, False if not and needs to go back
    to the previous one
    """
    coord = [0, 0]
    not_resolved = find_empty(coord)
    if not not_resolved:
        return True

    for i in range(1, 10):
        valid = is_correct(coord, i)
        if valid:
            board[coord[0]][coord[1]] = i
            if resolve():
                return True
            board[coord[0]][coord[1]] = 0
    return False


coord = [0, 0]
print_board()
resolve()
print("Soluzione:")
print_board()
