// leetcode 417

import java.util.*;

class Solution {

	public void findMaxPoint(int[][] heights, Set<String> visitSet, int i, int j, int rowSize, int colSize, Set<String> cellSet) {
		cellSet.add(i + "," + j);
		visitSet.add(i + "," + j);

		int[][] moves = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
		for (int[] move : moves) {
			int dx = i + move[0];
			int dy = j + move[1];

			if ((dx >= 0 && dx < rowSize) && (dy >= 0 && dy < colSize) && !visitSet.contains(dx + "," + dy)) {
				if ((heights[dx][dy] >= heights[i][j])) {
					findMaxPoint(heights, visitSet, dx, dy, rowSize, colSize, cellSet);
				}
			}
		}
	}

	public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int rowSize = heights.length;
        int colSize = heights[0].length;
        Set<String> visitSet = new HashSet<>();
        Set<String> pacificSet = new HashSet<>();
        Set<String> atlanticSet = new HashSet<>();

        // processing left side pacific ocean
        for(int i = 0, j = 0; i < rowSize; i++) {
        	visitSet.clear();
        	findMaxPoint(heights, visitSet, i, j, rowSize, colSize, pacificSet);
        }

        // processing top side pacific ocean
        for(int i = 0, j = 1; j < colSize; j++) {
        	visitSet.clear();
        	findMaxPoint(heights, visitSet, i, j, rowSize, colSize, pacificSet);
        }

        // processing right side atlantic ocean
        for(int i = 0, j = colSize - 1; i < rowSize; i++) {
        	visitSet.clear();
        	findMaxPoint(heights, visitSet, i, j, rowSize, colSize, atlanticSet);
        }

        // processing bottom side atlantic ocean
        for(int i = rowSize - 1, j = 0; j < colSize - 1; j++) {
        	visitSet.clear();
        	findMaxPoint(heights, visitSet, i, j, rowSize, colSize, atlanticSet);
        }

        pacificSet.retainAll(atlanticSet);
        // System.out.println(pacificSet);

        List<List<Integer>> res = new ArrayList<>();
        for (String coord : pacificSet) {
        	String[] token = coord.split(",");
        	List<Integer> list = new ArrayList<>();
        	list.add(Integer.parseInt(token[0]));
        	list.add(Integer.parseInt(token[1]));
        	res.add(list);
        }

        return res;
    }
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		int[][] heights = {{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}};
		System.out.println(obj.pacificAtlantic(heights));
	}
}