# @author:  Tanzeem Chowdhury [997574726]
# @brief:   Using different search algorthms to solve sudoku puzzles


# Open puzzle from filename, and store and return puzzle contents in a list. The list will 
# contain 9 nested lists (sudoku rows), each of which contain the cell values of that row
def open_puzzle(filename):
    
    puzzle_rows = []
    
    # Open puzzle from filename
    with open(filename) as f:
        
        # Read each line of file, i.e. each sudoku row. Since cell values are separated by 
        # whitespace, use split to get a list of cell values, and append this row list to puzzle
        for line in f:
            puzzle_rows.append(line.split())
    
    return puzzle_rows


# Given a list containing the row lists of the puzzle, return a list containing the column lists
# of the puzzle
def get_puzzle_columns(puzzle_rows):
    
    puzzle_columns = [[],[],[],[],[],[],[],[],[]]
    
    # From each row, iterate through the cell values to append them to separate columns lists
    for row in puzzle_rows:
        i = 0
        while i < 9:
            puzzle_columns[i].append(row[i])
            i += 1
        
    return puzzle_columns


# Given a list containing the row lists of the puzzle, return a list containing nested lists,
# which store cell values from the same house, i.e. the same sub 3x3 square
def get_puzzle_houses(p):
    
    puzzle_houses = [[],[],[],[],[],[],[],[],[]]
    return puzzle_houses    
    


def is_goal_state(puzzle):
    return False
    

if __name__ == "__main__":
    
    rows = open_puzzle("puzzle1.txt")
    columns = get_puzzle_columns(rows)
    
    for r in rows:
        print r
    
    print "\n"    
    
    for c in columns:
        print c