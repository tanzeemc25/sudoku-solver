# @author:  Tanzeem Chowdhury [997574726]
# @file:    SudokuHelpers.py
# @brief:   Helper methods for SudokuSolver.py


# Opens puzzle from filename, and store puzzle content. 
# Returns a list, containing rows (nested lists), each of which contains cell values of a row.
def read_puzzle(filename):
    
    puzzle_rows = []
    
    # Open puzzle from filename
    with open(filename) as f:
        
        # Read each line of file, i.e. each sudoku row. Since cell values are separated by
        # whitespace, use split to get a list of cell values, and append this row to puzzle
        for line in f:
            puzzle_rows.append(line.split())

    return puzzle_rows


# Write given puzzle to a file with name given by filename
def write_puzzle(puzzle, filename):
    
    file = open(filename, "w")
    
    row = 0
    while row < 9:
        cell = 0
        while cell < 9:
            
            # If it's not the last cell in a row, write a space after
            if not cell == 8:
                file.write(puzzle[row][cell] + " ")
            # If last cell in row, but not last row, write newline after
            elif cell == 8 and not row == 8: 
                file.write(puzzle[row][cell] + "\n")
            # If last cell in last row, only write the cell value
            else:
                file.write(puzzle[row][cell])
            
            cell += 1
        
        row += 1
    
    file.close()
    
    return True


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


# Searches a puzzle for empty spaces, and returns a list containing their coordinates, as well as 
# all valid values for those spaces 
def get_empty_cells_mrv(puzzle):
    
    empty_cells = []
    
    # Iterate through each row and column index to search for 0's, which represent a blank space
    row = 0
    while row < 9:
        column = 0
        while column < 9:
            if puzzle[row][column] == "0":
                cell = (row, column)

                # Get all the legal values that can be placed in this cell 
                valid_nums = get_valid_nums(puzzle, cell)
                
                # Append a tuple containing the number of legal values, the cell coords, and the
                # list of legal values. The number of legal values are at the first index so we
                # can easily sort the tuples by number of legal values
                empty_cells.append((len(valid_nums), cell, valid_nums))

            column += 1
        row += 1
    
    # Return empty cells sorted by minimum restricted values
    return sorted(empty_cells)


# Given a cell, retrieve the row, column, and house lists it belongs to in the puzzle
def get_cell_groups(puzzle, cell):

    # Get the coordinates of empty cell
    row_coord = cell[0]
    col_coord = cell[1]

    # Get the row the empty cell belongs to
    puzzle_row = puzzle[row_coord]

    # Get the column the empty cell belongs to
    puzzle_column = []
    for i in range(0, 9):
        puzzle_column.append(puzzle[i][col_coord])

    # To get the house the empty cell belongs to, first determine the center cell of that house
    # based on it's row/column coordinates
    if row_coord < 3: house_center_r = 1
    elif row_coord > 5: house_center_r = 7
    else: house_center_r = 4
    if col_coord < 3: house_center_c = 1
    elif col_coord > 5: house_center_c = 7
    else: house_center_c = 4

    # Once we know the center cell of the house, we can get the entire house by retrieving all the
    # cells around it, which are at indexs from row-1 to row+1, and column-1 to column+1
    puzzle_house = []
    for r in range(-1, 2):
        for c in range(-1, 2):
            puzzle_house.append(puzzle[house_center_r+r][house_center_c+c])

    # return a dictionary containing the row, column and house
    return {'row': puzzle_row, 'column': puzzle_column, 'house': puzzle_house}


# Get a list of all the valid numbers possible for a cell, i.e. numbers that do not conflict with
# row, column or house of that cell
def get_valid_nums(puzzle, cell):
    
    valid_numbers = []

    # Get the row/column/house lists the cell belongs to
    groups = get_cell_groups(puzzle, cell)

    # For all possible cell values (1-9), if's not already in the same row/column/house, add it to
    # the list of valid numbers
    for i in range(1, 10):
        num = str(i)
        if num not in groups['row'] and num not in groups['column'] and num not in groups['house']:
            valid_numbers.append(i)

    return valid_numbers


# Check if placing a value in a cell in the puzzle causes a conflict, i.e. returns True if a value
# does not exist in the cell's row, column, or house
def check_cell(puzzle, cell, value):
    
    # Get the row/column/house lists the cell belongs to
    groups = get_cell_groups(puzzle, cell)

    if value not in groups['row'] and value not in groups['column'] and value not in groups['house']:
        return True

    return False

