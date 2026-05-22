from typing import List

class Solution:

	'''
	Approach, dynamic programming and bottom up approach
	So basically we build up the number of ways the robot can go to another cell from base cell which is 0,0
	Technically the base cell 0,0 a robot can go just 1 way. So in this case dp[0][0] would be 1
	Now, a robot can move either a right cell or down cell, so technically number of ways of a cell x,y can be calculated
	by summing up the upper cell and left cell.
	Please see the example below:
	 0 0 0 << the out boundary cells are 0 by default
	|1|1|1|
	|1|2|3|
	|1|3|6|

	It is always dp[x][y] = dp[i - 1][j] + dp[i][j - 1]
	Time complexity O(m * n) number of total cells
	Space complexity O(m * n)
	'''
	def uniquePaths(self, m: int, n: int) -> int:
		
		dp = [[0 for _ in range(n)] for _ in range(m)]

		dp[0][0] = 1
		for i in range(0,m):
			for j in range(0,n):
				if i == 0 and j == 0:
					continue

				valueUpCell = 0 if (i - 1) < 0 else dp[i - 1][j]
				valueLeftCell = 0 if (j - 1) < 0 else dp[i][j - 1]

				dp[i][j] = valueUpCell + valueLeftCell

		# print(dp)

		return dp[m - 1][n - 1]


obj = Solution()
print(obj.uniquePaths(3,7))
