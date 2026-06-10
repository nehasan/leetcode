// leetcode 212

import java.util.*;

class Solution {
	public void dfsTraverse(int i, int j, int rowSize, int colSize, char[][] board, Stack<String> pathString, Set<String> wordSet) {
		pathString.add(String.valueOf(board[i][j]));

		String word = "";
		for (String s: pathString) {
			word += s;
		}
		wordSet.add(word);
		// System.out.println("current pathString " + pathString);
		// System.out.println("current wordSet " + wordSet);

		char tempBoardValue = board[i][j];
		board[i][j] = '#';

		int[][] moves = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
		for (int[] move : moves) {
			int dx = i + move[0];
			int dy = j + move[1];

			if ((dx >= 0 && dx < rowSize) && (dy >= 0 && dy < colSize) && (board[dx][dy] != '#')) {
				dfsTraverse(dx, dy, rowSize, colSize, board, pathString, wordSet);
			}
		}

		pathString.pop();
		board[i][j] = tempBoardValue;
	}

	public List<String> findWords(char[][] board, String[] words) {
		int rowSize = board.length;
		int colSize = board[0].length;
		List<String> res = new ArrayList<>();

		Set<String> wordSet = new HashSet<>();
		Stack<String> pathString = new Stack<>();

		for (int i = 0; i < rowSize; i++) {
			for (int j = 0; j < colSize; j++) {
				pathString.clear();
				dfsTraverse(i, j, rowSize, colSize, board, pathString, wordSet);
			}
		}

		// System.out.println("final wordSet " + wordSet);
		for (String word: words) {
			if (wordSet.contains(word)) {
				res.add(word);
			}
		}

		Collections.sort(res);
		return res;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		char[][] board = {{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}};
		String[] words = {"oath","pea","eat","rain"};

		// char[][] board = {{'a', 'b'}, {'c', 'd'}};
		// String[] words = {"abcd"};
		System.out.println(obj.findWords(board, words));
	}
}