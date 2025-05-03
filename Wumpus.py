import random
import unittest

class Wumpus:
        def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        if initial_state:
             self.grid = [row[:] for row in initial_state]
        else:
            self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
            
        def get_neighbors(self, row, col):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                r, c = row + i, col + j
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    neighbors.append(self.grid[r][c])
        return neighbors
    
        def update_cell(self, row, col, next_grid):
        neighbors = self.get_neighbors(row, col)
        live_neighbors = sum(neighbors)

        with self.lock:
            if self.grid[row][col] == 1:  
                if live_neighbors < 2 or live_neighbors > 3:
                    next_grid[row][col] = 0
                else:
                    next_grid[row][col] = 1
            else:  
                if live_neighbors == 3:
                    next_grid[row][col] = 1
                else:
                    next_grid[row][col] = 0

        def display(self):
        with self.lock:
            for row in self.grid:
                print("".join(['#' if cell else '.' for cell in row]))
            print("-" * self.cols)
        

#if __name__ == "__main__":
#     initial_state = [
#         [0, 1, 0, 0, 0],
#         [0, 1, 0, 0, 0],
#         [0, 1, 0, 0, 0],
#         [0, 0, 0, 1, 0],
#         [0, 0, 0, 0, 0]
#     ]