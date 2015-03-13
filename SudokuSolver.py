# @author:  Tanzeem Chowdhury [997574726]
# @file:    SudokuSolver.py
# @brief:   Using different search algorithms to solve sudoku puzzles


from itertools import *
from SudokuHelpers import *


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
        # solved. If so, write solution to file
        if is_goal_state(puzzle):
            write_puzzle(puzzle, "output.txt")

            # return (True for success) immediatley to stop looping through the rest of 
            # the permuations
            return True
    
    return False


# Attempts to solve sudoku puzzle using the back-tracking (Constraint Satisfaction Problem) method,
# using recursion to back-track if path leads to incorrect values
def back_tracking(puzzle, empty_cells):
    
    # If the puzzle is solved, write solution to file
    if is_goal_state(puzzle):
        write_puzzle(puzzle, "output.txt")
        return True
    
    else:
        # Get the next empty cell
        current_cell = empty_cells[0]
        
        # For each value that can be put in the empty cell (1-9), assign the value to the empty 
        # cell. Check if this creates conflicts, and choose next value if it does and so on. If 
        # constraints are ok, modify puzzle with value and then recurse this function with the 
        # rest of the empty cells. If this value doesn't lead to the solution, the recursive call 
        # will eventually return false, then try the next value if one exists
        for i in range(1, 10):
            if (check_cell(puzzle, current_cell, str(i))):
                puzzle[current_cell[0]][current_cell[1]] = str(i)
                if back_tracking(puzzle, empty_cells[1:]):
                    return True

            # Reset to cell to empty cell as we have tried all values
            puzzle[current_cell[0]][current_cell[1]] = str(0)
    
    return False


# Attempts to solve sudoku puzzle using the forward-checking with Mininum Remaining Values (MRV) 
# heuristics method, using recursion to back-track if path leads to incorrect values
def forward_checking_mrv(puzzle):
    
    # If the puzzle is solved, write solution to file
    if is_goal_state(puzzle):
        write_puzzle(puzzle, "output.txt")
        return True
    
    else:

        # Get list of all empty cells, and the legal values they can currently take, sorted by
        # minimum restricted values, i.e. the cells which have the fewest legal options
        empty_cells = get_empty_cells_mrv(puzzle)

        # Get first mrv empty cell
        current_cell = empty_cells[0]
        coords = current_cell[1]
        legal_values = current_cell[2]
            
        # For each value that can legally be put in the chosen empty cell, modify the puzzle by 
        # placing value in empty cell. Then recurse this function with the rest of the empty cells, 
        # re-evaluating the mrv cells. If this value doesn't lead to the solution, the recursive 
        # call with eventually return false, then try the next legal value if one exists
        for legal_value in legal_values:
            puzzle[coords[0]][coords[1]] = str(legal_value)
            if forward_checking_mrv(puzzle):
                return True

            # Reset to cell to empty cell as we have tried all values
            puzzle[coords[0]][coords[1]] = str(0)
    
    return False


# Main method
if __name__ == "__main__":

    #FILE_NAME = "exampleEasy.txt"
    FILE_NAME = "examplePuzzle.txt"
    method = 'FC-MRV'

    # Read puzzle
    puzzle = read_puzzle(FILE_NAME)

    # Use brute force to solve
    if method == 'BF':
        brute_force(puzzle)
    # Use back tracking to solve
    elif method == 'BT':
        empty_cells = get_empty_cells(puzzle)
        back_tracking(puzzle, empty_cells)
    elif method == 'FC-MRV':
        forward_checking_mrv(puzzle)



    
