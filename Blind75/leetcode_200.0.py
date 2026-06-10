'''
https://leetcode.com/problems/number-of-islands/
Algorithm approach:
Start with the 0,0 position, if that is "1" increase number of islands.
Start a recursive matrix exploration horizontally and vertically to mark the adjecent positions.
i, j-1 is left adjecent position of the current i, j
i-1, j is up
i, j+1 is right
i+1, j is down
mark the current i, j with any value except "1" and send instructions to visit adjecent positions and mark them done.
'''

from typing import List


class Solution:

    def markAdjecent(self, i, j, rowSize, colSize, grid):
        if i > -1 and j > -1 and i < rowSize and j < colSize:
            if grid[i][j] == '1':
                grid[i][j] = 'x'
                self.markAdjecent(i, j - 1, rowSize, colSize, grid)
                self.markAdjecent(i - 1, j, rowSize, colSize, grid)
                self.markAdjecent(i, j + 1, rowSize, colSize, grid)
                self.markAdjecent(i + 1, j, rowSize, colSize, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        rowSize = len(grid)
        colSize = len(grid[0])

        islandCount = 0
        for i in range(0, rowSize):
            for j in range(0, colSize):
                if grid[i][j] == '1':
                    islandCount += 1
                    self.markAdjecent(i, j, rowSize, colSize, grid)
                    
                
                print(grid)
        
        # print(grid)
        return islandCount


soln = Solution()
grid = [['1', '0'], ['0', '1']] # 2
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
] # 1
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
] # 3

grid = [['1', '0']] # 1
grid = [['1', '1']] # 1
grid = [['0', '1']] # 1
grid = [['0', '0']] # 0
grid = [["1","0","1","1","0","1","1"]] # 3
print(soln.numIslands(grid))