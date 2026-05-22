# leetcode 994

from typing import List
from collections import deque

class Solution:

	'''
	Approach, modified BFS, queueing the cell coordinates and processing 4 adjecent cells around a cell
	EnQueue all the cells that indicates rotten oranges which is 2
	Now we popout the cell from the queue and increase the value of the adjecent cells. Suppose
	the current cell is a rotten orange cell and value is 2 then adjecent 4 cells will be 2 + 1 = 3
	We enqueue this 4 adjecent cells and increase the value for the adjecents of the adjecent, however they must be good oranges means grid[dx][dx] == 1.
	Maximum value of a particular cell is the total minimum number of time it takes to rot all the oranges in the grid
	'''
	def minElapsedTime(self, grid: List[int]) -> int:
		rowSize, colSize = len(grid), len(grid[0])
		cellQ = deque()
		minTime = 2

		for i in range(rowSize):
			for j in range(colSize):
				if grid[i][j] == 2:
					cellQ.append((i, j))


		while len(cellQ) > 0:
			x, y = cellQ.popleft()

			# print(f"cell to be processed {(x, y)}")
			for move in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
				dx = x + move[0]
				dy = y + move[1]

				if (dx >= 0 and dx < rowSize) and (dy >= 0 and dy < colSize) and grid[dx][dy] == 1:
					grid[dx][dy] = grid[x][y] + 1
					minTime = max(minTime, grid[dx][dy])
					cellQ.append((dx, dy))

			# print(f"after this processing current grid {grid}")

		for i in range(rowSize):
			for j in range(colSize):
				if grid[i][j] == 1:
					return -1

		return minTime - 2


	def orangesRotting(self, grid: List[int]) -> int:
		
		return self.minElapsedTime(grid)


obj = Solution()

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(obj.orangesRotting(grid))

def test__001():
	grid = [[2,1,1],[1,1,0],[0,1,1]]
	assert(obj.orangesRotting(grid)) == 4

def test__002():
	grid = [[2,1,1],[0,1,1],[1,0,1]]
	assert(obj.orangesRotting(grid)) == -1

def test__003():
	grid = [[0,2]]
	assert(obj.orangesRotting(grid)) == 0