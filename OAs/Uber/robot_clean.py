'''

A vaccum cleaning robot is located at the charging station, which is at the top-left corner of the room 

the robot has a built-in map of the room, which is an mxn grid and a battery with limited capacity 

The floorPlan localizes obstacles and empty spaces, which are marked as 1 and 0 respectively in the grid. Initially, all the cells in the grid are dirty. Whenever the robot moves over a cell, it will clean the cell if it was dirty (It won't do anything if a cell is already cleaned) 

Every time the robot exectutes a move ( including leaving the charging station) the battery is redced by 1. Note that ther robot can move only in left, right, up and down. It cannot move diagonally 

The robot should return to the charging station before running out of battery.
Write a function that returns the maximum no of cells that can be cleaned by the robot 

Example 

floor Plan (grid) 

0 0 0 
0 1 0 
0 0 0 

Battery Capacity: 6 

Output: 3 
'''



def max_cells_cleaned(floor_plan, battery_capacity):
    rows = len(floor_plan)
    cols = len(floor_plan[0])

    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # To track visited cells and cleaned cells
    visited = [[False] * cols for _ in range(rows)]

    def dfs(x, y, battery, cleaned_cells):
        # If battery is insufficient to return, stop exploring
        if battery < 0:
            return 0
        
        # Mark the current cell as visited
        visited[x][y] = True
        max_cleaned = cleaned_cells

        # Try all possible moves
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the new position is within bounds, not an obstacle, and not visited
            if 0 <= nx < rows and 0 <= ny < cols and floor_plan[nx][ny] == 0 and not visited[nx][ny]:
                # Move to the new position, clean, and go back if battery allows
                cleaned = dfs(nx, ny, battery - 2, cleaned_cells + 1)  # -2 because it costs 1 move there and 1 move back
                max_cleaned = max(max_cleaned, cleaned)

        # Backtrack: unvisit the cell to explore other paths
        visited[x][y] = False
        return max_cleaned

    # Start from the charging station at (0, 0)
    return dfs(0, 0, battery_capacity, 0)

# Test the function with the example
floor_plan = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
battery_capacity = 6
print(max_cells_cleaned(floor_plan, battery_capacity))  # Output: 3
