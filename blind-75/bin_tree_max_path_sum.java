// leetcode 124

import java.util.*;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode () {}
	TreeNode (int val) { this.val = val; }
	TreeNode (int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}

class Solution {
	int maxSum;

	Solution () {
		this.maxSum = Integer.MIN_VALUE;
	}

	/*
	* Approach, DFS traversal and find the max path sum.
	* So apprantly we start from deeper end nodes where we try to find the
	* max sum of the left tree and then max sum of the right tree of a particular root node
	* Value of the nodes can be negative, so we always find the max sum of each tree by max(0, leftMaxSum) and max(0, rightMaxSum)
	* Now we store the maxSum of this path (leftTree -> root -> rightTree) by max(maxSum, (leftMaxSum + root + rightMaxSum))
	* But when we return to the previous node we choose the max sum of root + leftMaxSum or root + rightMaxSum, to be able to find
	* the max path sum for this previous node
	* Time complexity O(n), where n is the number of nodes we traverse
    * Space complexity O(n + 1), where n times we store left and right max sum and one single global maxSum
	*/
	public int findMaxPathSum(TreeNode root) {
		if (root == null) {
			return 0;
		}

		int leftMaxSum = Math.max(0, findMaxPathSum(root.left));
		int rightMaxSum = Math.max(0, findMaxPathSum(root.right));

		this.maxSum = Math.max(this.maxSum, leftMaxSum + root.val + rightMaxSum);

		return Math.max((root.val + leftMaxSum), (root.val + rightMaxSum));
	}

	public int maxPathSum(TreeNode root) {
		if (root == null) {
			return 0;
		}

		findMaxPathSum(root);

		return this.maxSum;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
		System.out.println(obj.maxPathSum(root));

		root = new TreeNode(-10, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
		System.out.println(obj.maxPathSum(root));

		root = new TreeNode(-10, new TreeNode(9), new TreeNode(20, new TreeNode(15, new TreeNode(10), new TreeNode(9, null, new TreeNode(11))), new TreeNode(7)));
		System.out.println(obj.maxPathSum(root));
	}
}