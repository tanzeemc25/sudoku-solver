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


# Given a puzzle list containing lists of rows, returns a list containing list of columns
def get_puzzle_columns(puzzle_rows):
    
    puzzle_columns = [[],[],[],[],[],[],[],[],[]]
    
    # From each row, iterate through the cell values to append them separatly to each of the column 
    # lists
    for row in puzzle_rows:
        i = 0
        while i < 9:
            puzzle_columns[i].append(row[i])
            i += 1
        
    return puzzle_columns


# Given a puzzle list containing lists of rows, returns a list containing lists of houses, i.e.
# lists containing cell values that belong to same 3x3 sub-square
def get_puzzle_houses(puzzle_rows):
    
    # Use p to make the list map look cleaner
    p = puzzle_rows;

    # Map the cell values in lists organised by the 3x3 house they belong to.
    # Retrive cell value using row/column positon, and map acordingly
    puzzle_houses = [   [ p[0][0], p[0][1], p[0][2], p[1][0], p[1][1], p[1][2], p[2][0], p[2][1], p[2][2] ],
                        [ p[0][3], p[0][4], p[0][5], p[1][3], p[1][4], p[1][5], p[2][3], p[2][4], p[2][5] ],
                        [ p[0][6], p[0][7], p[0][8], p[1][6], p[1][7], p[1][8], p[2][6], p[2][7], p[2][8] ],

                        [ p[3][0], p[3][1], p[3][2], p[4][0], p[4][1], p[4][2], p[5][0], p[5][1], p[5][2] ],
                        [ p[3][3], p[3][4], p[3][5], p[4][3], p[4][4], p[4][5], p[5][3], p[5][4], p[5][5] ],
                        [ p[3][6], p[3][7], p[3][8], p[4][6], p[4][7], p[4][8], p[5][6], p[5][7], p[5][8] ],

                        [ p[6][0], p[6][1], p[6][2], p[7][0], p[7][1], p[7][2], p[8][0], p[8][1], p[8][2] ],
                        [ p[6][3], p[6][4], p[6][5], p[7][3], p[7][4], p[7][5], p[8][3], p[8][4], p[8][5] ],
                        [ p[6][6], p[6][7], p[6][8], p[7][6], p[7][7], p[7][8], p[8][6], p[8][7], p[8][8] ]
                    ]

    return puzzle_houses    
    

# Given the puzzle's rows, columns, and houses, returns whether the puzzle is in goal state / solved.
def is_goal_state(rows, columns, houses):

    # If any row contains 0, or it's set (row with duplicates removed) doesn't have length of 9 - 
    # meaning there were duplicates, return false
    for row in rows:
        row_set = set(row)
        if 0 in row_set or len(row_set) != 9:
            return False

    # If any column contains 0, or it's set (row with duplicates removed) doesn't have length of 9 - 
    # meaning there were duplicates, return false
    for column in columns:
        col_set = set(column)
        if 0 in col_set or len(col_set) != 9:
            return False

    # If any house contains 0, or it's set (row with duplicates removed) doesn't have length of 9 - 
    # meaning there were duplicates, return false
    for house in houses:
        house_set = set(row)
        if 0 in house_set or len(house_set) != 9:
            return False

    return True


# Main method
if __name__ == "__main__":
    
    rows = read_puzzle("examplePuzzle.txt")
    columns = get_puzzle_columns(rows)
    houses = get_puzzle_houses(rows)
    
    print is_goal_state(rows, columns, houses)