from typing import List

class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    
    def fill(image: List[List[int]], i: int, j:int, rowSize: int, colSize: int, sharedColor: int, color: int):
      
      print(f"i: {i}, j: {j}, row: {rowSize}, col: {colSize}, sharedColor: {sharedColor}, color: {color}")
      if (i >= 0 and i < rowSize) and (j >= 0 and j < colSize) and (image[i][j] == sharedColor):
        print(f"entered for i {i}, j {j}, row {rowSize}, col {colSize}")
        image[i][j] = color
        
        fill(image, i, j - 1, rowSize, colSize, sharedColor, color) # left box
        fill(image, i - 1, j, rowSize, colSize, sharedColor, color) # up box
        fill(image, i, j + 1, rowSize, colSize, sharedColor, color) # right box
        fill(image, i + 1, j, rowSize, colSize, sharedColor, color) # bottom box
    
    
    rowSize = len(image)
    colSize = len(image[0])
    
    if image[sr][sc] != color:
      fill(image, sr, sc, rowSize, colSize, image[sr][sc], color)
    
    return image


obj = Solution()

def test_0001():
  image = [[1,1,1],[1,1,0],[1,0,1]]
  sr, sc, color = 1, 1, 2
  assert(obj.floodFill(image, sr, sc, color)) == [[2,2,2],[2,2,0],[2,0,1]]


def test_0002():
  image = [[0,0,0],[0,0,0]]
  sr, sc, color = 0, 0, 0
  assert(obj.floodFill(image, sr, sc, color)) == [[0,0,0],[0,0,0]]