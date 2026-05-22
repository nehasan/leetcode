// leetcode 200

class Solution {
	public void floodFillTheGrid (int i, int j, int rowSize, int colSize, char[][] grid) {
		if ((i >= 0 && i < rowSize) && (j >= 0 && j < colSize) && grid[i][j] == '1') {
			grid[i][j] = '0';

			floodFillTheGrid(i, j - 1, rowSize, colSize, grid);
			floodFillTheGrid(i - 1, j, rowSize, colSize, grid);
			floodFillTheGrid(i, j + 1, rowSize, colSize, grid);
			floodFillTheGrid(i + 1, j, rowSize, colSize, grid);
		}
	}

	public int numIslands (char[][] grid) {
		int rowSize = grid.length;
		int colSize = grid[0].length;
		int totalIslands = 0;

		for (int i = 0; i < rowSize; i++) {
			for (int j = 0; j < colSize; j++) {
				if (grid[i][j] == '1') {
					floodFillTheGrid(i, j, rowSize, colSize, grid);
					totalIslands++;
				}
			}
		}

		return totalIslands;
	}
}


class Main {
	public static void main (String[] args) {
		Solution obj = new Solution();

		char[][] grid = new char[][] {
			{'1','1','1','1','0'},
  		{'1','1','0','1','0'},
  		{'1','1','0','0','0'},
  		{'0','0','0','0','0'}
		};
		System.out.println(obj.numIslands(grid)); // should print 1

		grid = new char[][] {
			{'1','1','0','0','0'},
  		{'1','1','0','0','0'},
  		{'0','0','1','0','0'},
  		{'0','0','0','1','1'}
		};
		System.out.println(obj.numIslands(grid)); // should print 3
	}
}