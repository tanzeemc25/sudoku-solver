# @author:  Tanzeem Chowdhury [997574726]
# @file:    SudokuIO.py
# @brief:   Contains methods to read/write to files, as well outputting to the screen


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


# Write clock time and generated node information to a file with name given by filename
def write_performance(total_time, search_time, nodes_expanded, filename):

	file = open(filename, "w")

	file.write("Total clock time: " + str(total_time*1000) + '\n')
	file.write("Search clock time: " + str(search_time*1000) + '\n')
	file.write("Number of nodes generated: " + str(nodes_expanded))

	file.close()

	return True


# Output puzzle to the screen
def output_puzzle(puzzle):
	
	output_str = ""
	
	row = 0
	while row < 9:
		
		cell = 0
		while cell < 9:

			# If it's not the last cell in a row, print a space after
			if not cell == 8:
				output_str += puzzle[row][cell] + " "
			# If last cell in row, but not last row, print newline after
			elif cell == 8 and not row == 8: 
				output_str += puzzle[row][cell] + "\n"
			# If last cell in last row, only print the cell value
			else:
				output_str += puzzle[row][cell]

			cell += 1

		row += 1

	print output_str


# Output clock time and generated node information to a file with name given by filename
def output_performance(total_time, search_time, nodes_expanded):
	
	print "Total clock time: " + str(total_time*1000)
	print "Search clock time: " + str(search_time*1000)
	print "Number of nodes generated: " + str(nodes_expanded)