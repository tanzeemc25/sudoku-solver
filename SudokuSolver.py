# @author:  Tanzeem Chowdhury [997574726]
# @brief:   Using different search algorthms to solve sudoku puzzles


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


# Given a puzzle, returns whether all rows are valid, that is, true if all rows do not contain
# empty spaces (represented by 0) and do not contain duplicates
def check_rows(puzzle):
    
    for row in puzzle:

        # Get set of list. If set contains 0 (empty space), or the set does not have length 9, 
        # meaning there were duplicates in the row, the row is invalid, so return false
        row_set = set(row)
        if 0 in row_set or len(row_set) != 9:
            return False

    # If code reaches here, all rows are valid, therefore return true
    return True


# Given a puzzle, returns whether all columns are valid, that is, true if all columns do not
# contain empty spaces (represented by 0) and do not contain duplicates
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
        if 0 in col_set or len(col_set) != 9:
            return False

        i += 1

    # If code reaches here, all columns are valid, therefore return true
    return True


# Given a puzzle, returns whether all houses (3x3 sub square) are valid, that is, true if all 
# houses do not contain empty spaces (represented by 0) and do not contain duplicates
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
        if 0 in house_set or len(house_set) != 9:
            return False

        i += 1

    # If code reaches here, all houses are valid, therefore return true
    return True


def is_goal_state(puzzle):

    # Puzzle is in goal state, i.e. solved, if all rows, columns and houses are valid
    return check_rows(puzzle) and check_columns(puzzle) and check_houses(puzzle)


# Main method
if __name__ == "__main__":

    puzzle = read_puzzle("examplePuzzle.txt")
    print is_goal_state(puzzle)
    
