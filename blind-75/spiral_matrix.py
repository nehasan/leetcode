# leetcode 54

from typing import List

class Solution:
    '''
    Approach recursive DFS traversal through matrix cell
    - Initialize the traverse from cell (0,0) and check if next right cell is avaiable
    to traverse (not hitting the boundary and not yet visited)
    - If the current direction is right then try next right or move down
    - If the current direction is down then try next down or move left and so on
    '''
    def spiralTraverse(self, matrix, visited, res, i, j, rowSize, colSize, direction) -> None:
        if (i >= 0 and i < rowSize) and (j >= 0 and j < colSize):
            visited.add((i, j))
            res.append(matrix[i][j])

            if direction == "right":
                if (j + 1 < colSize) and (i, j + 1) not in visited:
                    self.spiralTraverse(matrix, visited, res, i, j + 1, rowSize, colSize, "right")
                elif(i + 1 < rowSize) and (i + 1, j) not in visited:
                    self.spiralTraverse(matrix, visited, res, i + 1, j, rowSize, colSize, "down")
            elif direction == "down":
                if (i + 1 < rowSize) and (i + 1, j) not in visited:
                    self.spiralTraverse(matrix, visited, res, i + 1, j, rowSize, colSize, "down")
                elif (j - 1 >= 0) and (i, j - 1) not in visited:
                    self.spiralTraverse(matrix, visited, res, i, j - 1, rowSize, colSize, "left")
            elif direction == "left":
                if (j - 1 >= 0) and (i, j - 1) not in visited:
                    self.spiralTraverse(matrix, visited, res, i, j - 1, rowSize, colSize, "left")
                elif (i - 1 >= 0) and (i - 1, j) not in visited:
                    self.spiralTraverse(matrix, visited, res, i - 1, j, rowSize, colSize, "up")
            elif direction == "up":
                if (i - 1 >= 0) and (i - 1, j) not in visited:
                    self.spiralTraverse(matrix, visited, res, i - 1, j, rowSize, colSize, "up")
                elif (j + 1 < colSize) and (i, j + 1) not in visited:
                    self.spiralTraverse(matrix, visited, res, i, j + 1, rowSize, colSize, "right")


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowSize = len(matrix)
        colSize = len(matrix[0])

        res = []
        visited = set()
        self. spiralTraverse(matrix, visited, res, 0, 0, rowSize, colSize, "right")

        return res


obj = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(obj.spiralOrder(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(obj.spiralOrder(matrix))