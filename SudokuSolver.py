# @author: Tanzeem Chowdhury [997574726]
# @brief: Different algorthms to solve sudoku puzzles


# Open puzzle given a filename, and store puzzle contents as a list containing nested lists. That is, a list
# containing rows, which are lists 
def open_puzzle(filename):
    
    # Use list to store puzzle content
    puzzle = []
    
    # open puzzle file
    with open(filename) as f:
        
        # read each line of file, i.e. each sudoku row
        for line in f:
            
            # Cell values are separated by whitespace, use split to get a list of cell values, and add this row list
            # 
            puzzleList.append(line.split())
    
    return puzzleList

if __name__ == "__main__":
    print "Status: OK";
    
    puz = open_puzzle("puzzle1.txt")
    for e in puz:
        print e
    