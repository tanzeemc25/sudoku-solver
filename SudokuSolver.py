# @author:  Tanzeem Chowdhury [997574726]
# @file:    SudokuSolver.py
# @brief:   Using different search algorithms to solve sudoku puzzles


from itertools import *
from SudokuHelpers import *
from SudokuIO import *
import timeit
import sys


# Set global variables
global total_time_start
global total_time_stop
global search_time_start
global search_time_stop
global nodes_expanded
global SOLUTION_FILENAME


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

            global nodes_expanded
            nodes_expanded += 1            
            
            i += 1  
        
        # Once a single permuation's values are inserted into the puzzle, check if the puzzle is
        # solved. If so, output to the screen and write solution to file
        if is_goal_state(puzzle):         
            output_puzzle(puzzle)
            write_puzzle(puzzle, SOLUTION_FILENAME)

            # return (True for success) immediatley to stop looping through the rest of 
            # the permuations
            return True
    
    return False


# Attempts to solve sudoku puzzle using the back-tracking (Constraint Satisfaction Problem) method,
# using recursion to back-track if path leads to incorrect values
def back_tracking(puzzle, empty_cells):
    
    # If the puzzle is solved, output to the screen and write solution to file
    if is_goal_state(puzzle):
        output_puzzle(puzzle)
        write_puzzle(puzzle, SOLUTION_FILENAME)
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
            
            global nodes_expanded
            nodes_expanded += 1

            # Check constraints before assigning the value (or else it'll accidentally find
            # itself as duplicate)
            check = check_cell(puzzle, current_cell, str(i))

            puzzle[current_cell[0]][current_cell[1]] = str(i)
            if (check):
                if back_tracking(puzzle, empty_cells[1:]):
                    return True

            # Reset the cell to empty cell as we have tried all values
            puzzle[current_cell[0]][current_cell[1]] = str(0)
    
    return False


# Attempts to solve sudoku puzzle using the forward-checking with Mininum Remaining Values (MRV) 
# heuristics method, using recursion to back-track if path leads to incorrect values
def forward_checking_mrv(puzzle):
    
    # If the puzzle is solved, output to the screen write solution to file
    if is_goal_state(puzzle):
        output_puzzle(puzzle)
        write_puzzle(puzzle, SOLUTION_FILENAME)
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

            global nodes_expanded
            nodes_expanded += 1

            puzzle[coords[0]][coords[1]] = str(legal_value)
            if forward_checking_mrv(puzzle):
                return True

            # Reset to cell to empty cell as we have tried all values
            puzzle[coords[0]][coords[1]] = str(0)
    
    return False


# Main method
if __name__ == "__main__":

    # Start timing total time
    total_time_start = timeit.default_timer()

    nodes_expanded = 0

    # If user doesn't provide the correct amount of arguments, send msg
    if len(sys.argv) != 3:
        print "Please use correct synopsis. Usage: SudokuSolver.py puzzlefilename algorithm"

    else:
        PUZZLE_FILENAME = sys.argv[1]
        METHOD = sys.argv[2]

        # Solution and Performance output file names are dependant on input filename
        SOLUTION_FILENAME = 'solution' + PUZZLE_FILENAME[-5:]
        PERFORMANCE_FILENAME = 'performance' + PUZZLE_FILENAME[-5:]

        # Read puzzle
        puzzle = read_puzzle(PUZZLE_FILENAME)

        # Use brute force to solve
        if METHOD == 'BF':
            search_time_start = timeit.default_timer()
            brute_force(puzzle)
            search_time_stop = timeit.default_timer()

        # Use back tracking to solve
        elif METHOD == 'BT':
            search_time_start = timeit.default_timer()
            empty_cells = get_empty_cells(puzzle)
            back_tracking(puzzle, empty_cells)
            search_time_stop = timeit.default_timer()

        # Use forward checking with MRV to solve
        elif METHOD == 'FC-MRV':
            search_time_start = timeit.default_timer()
            forward_checking_mrv(puzzle)
            search_time_stop = timeit.default_timer()
        
        # Stop and calculate times
        total_time_stop = timeit.default_timer()
        search_time = search_time_stop - search_time_start
        total_time = total_time_stop - total_time_start

        # Output to screen and write to file performance information
        output_performance(total_time, search_time, nodes_expanded)
        write_performance(total_time, search_time, nodes_expanded, PERFORMANCE_FILENAME)
    
