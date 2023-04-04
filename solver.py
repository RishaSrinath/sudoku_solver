def find_empty(grid):
    """
    Find an empty cell in the grid
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid(grid, row, col, value):
    """
    Check if a given value can be placed in a given cell
    """
    # Check row
    if value in grid[row]:
        return False
    
    # Check column
    if value in [grid[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 subgrid
    subgrid_row, subgrid_col = (row // 3) * 3, (col // 3) * 3
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if grid[i][j] == value:
                return False
    
    return True

def solve(grid):
    """
    Solve the Sudoku puzzle using backtracking
    """
    empty_cell = find_empty(grid)
    
    # If there are no more empty cells, the puzzle is solved
    if empty_cell is None:
        return True
    
    row, col = empty_cell
    
    # Try all possible values for this cell
    for value in range(1, 10):
        if is_valid(grid, row, col, value):
            grid[row][col] = value
            
            # Recursively solve the rest of the puzzle
            if solve(grid):
                return True
            
            # If the puzzle cannot be solved with this value, backtrack
            grid[row][col] = 0
    
    # If no value works for this cell, backtrack
    return False

  
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

solve(grid)

for row in grid:
    print(row)
