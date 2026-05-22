from typing import List

class Solution:
  def islandPerimeter(self, grid: List[int]) -> int:
    
    def findPerimeter(grid: List[List[int]], i: int, j: int, rowSize: int, colSize: int):
      if i < 0 or i >= rowSize or j < 0 or j >= colSize or grid[i][j] == 0:
        return 1
      elif grid[i][j] == -1:
        return 0
      elif (i >= 0 and i < rowSize) and (j >= 0 and j < colSize) and (grid[i][j] == 1):
        grid[i][j] = -1 # -1 means done processing
        
        return 0 + findPerimeter(grid, i, j - 1, rowSize, colSize) + \
                findPerimeter(grid, i - 1, j, rowSize, colSize) + \
                findPerimeter(grid, i, j + 1, rowSize, colSize) + \
                findPerimeter(grid, i + 1, j, rowSize, colSize)
      
    
    rowSize = len(grid)
    colSize = len(grid[0])
    perimeterSize = 0
    
    for i in range(rowSize):
      for j in range(colSize):
        if grid[i][j] == 1:
          perimeterSize += findPerimeter(grid, i, j, rowSize, colSize)
    
    # print(grid)
    return perimeterSize
    


obj = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(obj.islandPerimeter(grid))

def test_001():
  grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
  assert(obj.islandPerimeter(grid)) == 16

def test_002():
  grid = [[1]]
  assert(obj.islandPerimeter(grid)) == 4

def test_003():
  grid = [[0,1]]
  assert(obj.islandPerimeter(grid)) == 4

def test_004():
  grid = [[1,0]]
  assert(obj.islandPerimeter(grid)) == 4

def test_005():
  grid = [[1,0],[0,1]]
  assert(obj.islandPerimeter(grid)) == 8

def test_006():
  grid = [[0,1],[1,0]]
  assert(obj.islandPerimeter(grid)) == 8

def test_006():
  grid = [[0,1],[0,1]]
  assert(obj.islandPerimeter(grid)) == 6