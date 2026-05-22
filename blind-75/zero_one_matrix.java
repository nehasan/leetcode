import java.util.*;

class Solution {
	/*
	* Approach, modified dfs with modified dynamic programming
	* Make mat[i][j] INF when there is a 1 and push mat[i][j] to a queue when there is a 0
	* Now pull and process the queue until its empty
	* For each 0 cell check adjecent 4 cells if mat[dx][dy] > mat[i][j] + 1
	* If yes then simply mat[dx][dy] = mat[i][j] + 1 and enqueue that mat[dx][dy] cell to process further
	* At the end return mat
	*/
	public int[][] updateMatrix(int[][] mat) {
		int rowSize = mat.length;
		int colSize = mat[0].length;
		int INF = Integer.MAX_VALUE;

		Queue<int[]> q = new LinkedList<>();

		for (int i = 0; i < rowSize; i++) {
			for (int j = 0; j < colSize; j++) {
				if (mat[i][j] == 1) {
					mat[i][j] = INF;
				} else {
					q.add(new int[] {i, j});
				}
			}
		}

		while(!q.isEmpty()) {
			int[] cell = q.poll();
			int i = cell[0], j = cell[1];
			int [][] moves = new int[][] {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};

			for (int[] move : moves) {
				int dx = i + move[0];
				int dy = j + move[1];

				if ((dx >= 0 && dx < rowSize) && (dy >= 0 && dy < colSize)) {
					if (mat[dx][dy] > (mat[i][j] + 1)) {
						mat[dx][dy] = mat[i][j] + 1;
						q.add(new int[] {dx, dy});
					}
				}
			}
		}
		
		return mat;
	}
}

class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();
		
		int[][] mat = new int[][] {
			{0,0,0},
			{0,1,0},
			{0,0,0},
		};
		int[][] res = obj.updateMatrix(mat);
		for (int i = 0; i < mat.length; i++) {
			for (int j = 0; j < mat[0].length; j++) {
				System.out.print(res[i][j]);
			}
			System.out.println("");
		}
		
		System.out.println("");
		mat = new int[][] {
			{0,0,0},
			{0,1,0},
			{1,1,1},
		};
		res = obj.updateMatrix(mat);
		for (int i = 0; i < mat.length; i++) {
			for (int j = 0; j < mat[0].length; j++) {
				System.out.print(res[i][j]);
			}
			System.out.println("");
		}

		System.out.println("");
		mat = new int[][] {
			{1,1,0},
			{1,1,0},
			{1,0,0},
		};
		res = obj.updateMatrix(mat);
		for (int i = 0; i < mat.length; i++) {
			for (int j = 0; j < mat[0].length; j++) {
				System.out.print(res[i][j]);
			}
			System.out.println("");
		}
	}
}