# leetcode 64

from typing import List

class Solution:

	'''
	Approach, dynamic programming and bottom up approach, same as leetcode 62, unique paths
	So basically we build up the minSum of a cell from the base cell which is 0,0
	Technically the base cell 0,0 we start summing up the path sum. Initially dp[0][0] would be grid[0][0]
	Now, a move can be made either to a right cell or down cell, so technically minSum of a cell x,y can be calculated
	by choosing the min of upper cell + current grid and left cell + current grid.
	Please see the example below:
	 inf inf inf << the out boundary cells are +ve inf by default
	|1|3|1|
	|1|5|1|
	|4|2|1|

	It is always dp[x][y] = min((dp[i - 1][j] + grid[i][j]), (dp[i][j - 1] + grid[i][j]))

	the final dp would be as follows:
	|1|4|5|
	|2|7|6|
	|6|8|7|
	Time complexity O(m * n) number of total cells
	Space complexity O(m * n)
	'''
	def minPathSum(self, grid: List[List[int]]) -> int:
		
		rowSize = len(grid)
		colSize = len(grid[0])

		dp = [[0 for _ in range(colSize)] for _ in range(rowSize)]
		# dp[0][0] = grid[0][0]

		for i in range(rowSize):
			for j in range(colSize):
				if i == 0 and j == 0:
					continue

				upperCellVal = float('inf') if i - 1 < 0 else dp[i - 1][j]
				leftCellVal = float('inf') if j - 1 < 0 else dp[i][j - 1]

				# print(f"upperCellVal {upperCellVal}, leftCellVal {leftCellVal}, dp[i][j] {dp[i][j]}")
				dp[i][j] = min((grid[i][j] + upperCellVal), (grid[i][j] + leftCellVal))
				# print(f"d[i][j] now {dp[i][j]}")

		# print(dp)
		return dp[rowSize - 1][colSize - 1]


obj = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(obj.minPathSum(grid))

grid = [[1,2,3],[4,5,6]]
print(obj.minPathSum(grid))