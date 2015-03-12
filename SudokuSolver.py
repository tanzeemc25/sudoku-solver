# @author:  Tanzeem Chowdhury [997574726]
# @brief:   Using different search algorithms to solve sudoku puzzles


from itertools import *


# Opens puzzle from filename, and store puzzle content. 
# Returns a list, containing nested lists, each of which contains cell values of a row.
def read_puzzle(filename):
    puzzle_rows = []   
    # Open puzzle from filename
    with open(filename) as f:
        # Read each line of file, i.e. each sudoku row. Since cell values are separated by
        # whitespace, use split to get a list of cell values, and append this row to puzzle
        for line in f:
            puzzle_rows.append(line.split())
    return puzzle_rows


def write_puzzle(filename):
    return


# Given a puzzle, returns whether all rows are valid, that is, true if all rows do not contain
# empty spaces (represented by 0) and do not contain duplicates.
# Returns false as soon as an invalid row is found.
def check_rows(puzzle):
    for row in puzzle:
        # Get set of list. If set contains 0 (empty space), or the set does not have length 9, 
        # meaning there were duplicates in the row, the row is invalid, so return false
        row_set = set(row)
        if str(0) in row_set or len(row_set) != 9:
            return False
    # If code reaches here, all rows are valid, therefore return true
    return True


# Given a puzzle, returns whether all columns are valid, that is, true if all columns do not
# contain empty spaces (represented by 0) and do not contain duplicates.
# Returns false as soon as an invalid column is found.
def check_columns(puzzle):
    # Iterate to check each column
    i = 0
    while i < 9:
        # Puzzle is stored as list of rows. So get columns by pulling values from all rows at the same
        # index
        column = [  puzzle[0][i], puzzle[1][i], puzzle[2][i], puzzle[3][i], puzzle[4][i], 
                    puzzle[5][i], puzzle[6][i], puzzle[7][i], puzzle[8][i] ]
        # Get set of list. If set contains 0 (empty space), or the set does not have length 9, 
        # meaning there were duplicates in the column, the column is invalid, so return false
        col_set = set(column)
        if str(0) in col_set or len(col_set) != 9:
            return False
        i += 1
    # If code reaches here, all columns are valid, therefore return true
    return True


# Given a puzzle, returns whether all houses (3x3 sub square) are valid, that is, true if all 
# houses do not contain empty spaces (represented by 0) and do not contain duplicates.
# Returns false as soon as an invalid house is found.
def check_houses(puzzle):
    # Puzzle is stored as list of rows. Get the coordinates of the center cells of each 3x3 house
    centers = [ (1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7) ]
    # Iterate to check each house
    i = 0
    while i < len(centers):      
        r = centers[i][0] # row coordinate
        c = centers[i][1] # column coordinate   
        # If we have the coordinates for the center of the house, we can get the coordinates of all
        # cell values surrounding it. Get house by using these coordinates.
        house = [   puzzle[r-1][c-1], puzzle[r-1][c], puzzle[r-1][c+1], puzzle[r][c-1], puzzle[r][c], 
                    puzzle[r][c+1], puzzle[r+1][c-1], puzzle[r+1][c], puzzle[r+1][c+1] ]
        # Get set of list. If set contains 0 (empty space), or the set does not have length 9,
        # meaning there were duplicates in the house, the house is invalid, so return false
        house_set = set(house)
        if str(0) in house_set or len(house_set) != 9:
            return False
        i += 1
    # If code reaches here, all houses are valid, therefore return true
    return True


# Returns whether a puzzle's current state is in goal state, i.e. solved
def is_goal_state(puzzle):
    # In goal state if all rows, columns and houses are valid
    return check_rows(puzzle) and check_columns(puzzle) and check_houses(puzzle)


# Searches a puzzle for empty spaces, and returns a list containing all the coordinates of empty 
# spaces
def get_empty_cells(puzzle):
    empty_cells = []
    # Iterate through each row and column index to search for 0's, which represent a blank space
    row = 0
    while row < 9:
        column = 0
        while column < 9:
            if puzzle[row][column] == "0":
                empty_cells.append((row, column))
            column += 1
        row += 1
    return empty_cells


# Attempts to solve sudoku puzzle using the brute force (exhaustive search) method
def brute_force(puzzle):
    # Get a list of coordinates of all the empty cells
    blanks = get_empty_cells(puzzle)
    
    # Since we are brute forcing, we need every single permutation of possible values we can insert
    # into empty cell values. We can get all possible blanks using the product method from the
    # module itertools, providing it the range of numbers we want (1 - 9), and repeat value, which
    # is the number of blanks we have
    possible_blanks = product(range(1, 10), repeat=len(blanks))
    
    # Starting with the first permutation (e.g. (1, 1, 1, ...) ), iter through all possibilities
    # until a permuation is found that solves the puzzle
    for p in possible_blanks:
        i = 0
        while i < len(blanks):
            # Use the coordinates from empty cells list, and place the value from the permutation
            # in there
            row = blanks[i][0]
            column = blanks[i][1]
            puzzle[row][column] = str(p[i])
            i += 1  
        # Once a single permuation's values are inserted into the puzzle, check if the puzzle is
        # solved. If so, return immediatley to stop looping through the rest of the permuations
        if is_goal_state(puzzle):
            return
    return

# Get a list of all the valid numbers possible for a cell, i.e. numbers that do not conflict with
# row, column or house of that cell
def get_valid_nums(puzzle, cell):
    
    valid_numbers = []

    row_coord = cell[0]
    col_coord = cell[1]

    puzzle_row = puzzle[row_coord]

    puzzle_column = []
    for i in range(0, 9):
        puzzle_column.append(puzzle[i][col_coord])

    if row_coord < 3: house_center_r = 1
    elif row_coord > 5: house_center_r = 7
    else: house_center_r = 4

    if col_coord < 3: house_center_c = 1
    elif col_coord > 5: house_center_c = 7
    else: house_center_c = 4

    puzzle_house = []
    for r in range(-1, 2):
        for c in range(-1, 2):
            puzzle_house.append(puzzle[house_center_r+r][house_center_c+c])
  
    for i in range(1, 10):
        num = str(i)
        if num not in puzzle_row and num not in puzzle_column and num not in puzzle_house:
            valid_numbers.append(i)

    return valid_numbers


def back_tracking(puzzle, empty_cells):
    
    if is_goal_state(puzzle):

        for e in puzzle:
            print e
        print "\n"


        return True



    else:

        current_cell = empty_cells[0]
        valid_nums = get_valid_nums(puzzle, current_cell)
        for valid_num in valid_nums:
            puzzle[current_cell[0]][current_cell[1]] = str(valid_num)


            if back_tracking(puzzle, empty_cells[1:]):
                return True
            puzzle[current_cell[0]][current_cell[1]] = str(0)
    return False






def forward_checking(puzzle):
    return


# Main method
if __name__ == "__main__":

    # Read puzzle
    puzzle = read_puzzle("examplePuzzle.txt")
    #puzzle = read_puzzle("exampleEasy.txt")

    empty_cells = get_empty_cells(puzzle)

    back_tracking(puzzle, empty_cells)

    # Use brute force algorithm
    #brute_force(puzzle)



    
