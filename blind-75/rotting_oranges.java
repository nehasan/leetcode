// leetcode 994

import java.util.*;

class Pair {
	int x;
	int y;
	Pair () {}
	Pair (int x, int y) {
		this.x = x;
		this.y = y;
	}

	public String toString() {
		return new String(x + " " + y);
	}
}

class Solution {

	public int minElapsedTime(int[][] grid) {
		int rowSize = grid.length;
		int colSize = grid[0].length;
		int minTime = 2;
		Queue<Pair> cellsQueue = new LinkedList<>();

		for (int i = 0; i < rowSize; i++) {
			for (int j = 0; j < colSize; j++) {
				if (grid[i][j] == 2) {
					cellsQueue.add(new Pair(i, j));
				}
			}
		}

		while(!cellsQueue.isEmpty()) {
			Pair currCell = cellsQueue.poll();

			System.out.println("cell to be processed: " + currCell);
			int[][] moves = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
			for (int[] move : moves) {
				int dx = currCell.x + move[0];
				int dy = currCell.y + move[1];

				if (((dx >=0 && dx < rowSize) && (dy >= 0 && dy < colSize)) && grid[dx][dy] == 1) {
					grid[dx][dy] = grid[currCell.x][currCell.y] + 1;
					minTime = Math.max(minTime, grid[dx][dy]);
					cellsQueue.add(new Pair(dx, dy));
				}
			}
			System.out.println("After this processing current grid" + Arrays.deepToString(grid));
		}

		for (int i = 0; i < rowSize; i++) {
			for (int j = 0; j < colSize; j++) {
				if (grid[i][j] == 1) {
					return -1;
				}
			}
		}

		return minTime - 2;
	}

	public int orangesRotting(int[][] grid) {
		return minElapsedTime(grid);
	}
}


class Main {
	public static void main (String[] args) {
		Solution obj = new Solution();

		int[][] grid = {
			{2,1,1},
			{1,1,0},
			{0,1,1}
		};
		System.out.println(obj.orangesRotting(grid)); // should print 4

		grid = new int[][] {
			{2,1,1},
			{0,1,1},
			{1,0,1}
		};
		System.out.println(obj.orangesRotting(grid)); //should print -1

		grid = new int[][] {
			{0,2},
		};
		System.out.println(obj.orangesRotting(grid)); //should print 0
	}
}