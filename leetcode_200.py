'''
Leetcode 200. Number of Islands
Author: Nahid Hasan Khan
Language: Python
'''
from typing import List


class Solution:
    '''
    Algorithm: This function uses the recursive dfs to search the lands around a land ('1')
    - It iterates over each value on the grid and recursively calls dfs function passing on the grid \
        position arguments
    - In each dfs it checks whether the value it's sitting on a land or water
    - If land it crosses out the lands by marking it '0' to avoid repeated visiting and \
        moves to the next land either up, right, left or down
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Returns int value of total islands present in the grid
        Arguments:
        grid - 2D m * n array contains '1' and '0', must be List[List[str]]
        '''
        
        row = len(grid)
        col = len(grid[0])
        totalIslands = 0
        
        def exploreIsland(i: int, j: int, row: int, col: int):
            '''
            Returns None
            Arguments:
            i    - ith position on the grid to start the search with, must be int
            j    - jth position on the grid to start the search with, must be int
            row  - rowsize of the grid to cap the next move, must be int
            col  - colsize of the grid to cap the next move, must be int
            This method explores the island and crosses out the visited lands to cap the repeated visit
            '''
            
            if 0 <= i and i < row and 0 <= j and j < col:
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    exploreIsland(i, j + 1, row, col) # moving to right
                    exploreIsland(i + 1, j, row, col) # moving to down
                    exploreIsland(i, j - 1, row, col) # moving to left
                    exploreIsland(i - 1, j, row, col) # moving to up
                    
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    exploreIsland(i, j, row, col)
                    totalIslands += 1
        
        return totalIslands
    
    

obj = Solution()
# grid = [['1','0'], ['0', '1']] # output: 2
'''
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]                                # output: 1
'''

'''
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]                                # output: 3
'''

grid = [["1","0","1","1","0","1","1"]]

print(obj.numIslands(grid))
    