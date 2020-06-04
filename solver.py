# sudoku solver


def solve(puzzle):
    space = locate_empty_space(puzzle)
    # checks if puzzle has any empty space
    if space:
        row, column = space
    else:
        return True, puzzle

    for i in range(1, len(puzzle) + 1):
        if check_if_valid(puzzle, space, i):
            puzzle[row][column] = i
            # recursion step
            if solve(puzzle)[0]:
                return True, puzzle
            # reset puzzle
            # for when the number does not violate any rules but putting it there causes sudoku to be unsolvable
            puzzle[row][column] = 0
    return False, puzzle


# Scans the sudoku puzzle and returns the earliest empty space
def locate_empty_space(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return i, j

    return None


# checks if the number at the position in the puzzle is valid
def check_if_valid(puzzle, position, number):
    # Check row
    # check if there is already that number in the row of the position
    # if so, it must be in the position given
    # else, return False
    for i in range(0, len(puzzle[0])):
        if puzzle[position[0]][i] == number and position[1] != i:
            return False

    # Check column
    # checks if given number already exists in the column of the position
    # if so, number must be in the row of position given
    # else, return False
    for i in range(0, len(puzzle)):
        if puzzle[i][position[1]] == number and position[0] != i:
            return False

    # Check Box

    box_x = int(position[1] // 3)
    box_y = int(position[0] // 3)

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == number and (i, j) != position:
                return False

    return True


# def print_puzzle(puzzle):
#     for i in range(len(puzzle)):
#         if i % 3 == 0 and i != 0:
#             print("____________________________")
#         for j in range(len(puzzle[0])):
#             if j % 3 == 0:
#                 print(" | ", end="")
#
#             if j == 8:
#                 print(puzzle[i][j], end="\n")
#             else:
#                 print(str(puzzle[i][j]) + " ", end="")
