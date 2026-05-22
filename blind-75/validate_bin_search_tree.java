// leetcode 98

import java.util.*;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode () {}
	TreeNode (int val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
	TreeNode (int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}

class Solution {

	/*
	* Approach DFS traverse and check the min max limitation of a node value
	* Initialize the validation with a max value (+ve inf) and a min value (-ve inf)
	* Now, for a certain node check if the node value is bigger than the max value or 
	* smaller than the min value then return false immediately.
	* Otherwise pass down the root value as max to the left tree and as min value to the right tree
	*/
	public boolean validateTree(TreeNode root, long maxVal, long minVal) {
		if (root != null) {
			if (root.val >= maxVal || root.val <= minVal) {
				return false;
			}

			return validateTree(root.left, root.val, minVal) && validateTree(root.right, maxVal, root.val);
		}

		return true;
	}

	public boolean isValidBST (TreeNode root) {
		return validateTree(root, Long.MAX_VALUE, Long.MIN_VALUE);
	}
}


class Main {
	public static void main (String[] args) {
		Solution obj = new Solution();

		TreeNode root = new TreeNode(2, new TreeNode(1), new TreeNode(3));
		System.out.println(obj.isValidBST(root)); // should be true

		root = new TreeNode(5, new TreeNode(1), new TreeNode(4, new TreeNode(3), new TreeNode(6)));
		System.out.println(obj.isValidBST(root)); // should be false

		root = new TreeNode(5, new TreeNode(1, new TreeNode(0), new TreeNode(2)), new TreeNode(6, new TreeNode(3), new TreeNode(7)));
		System.out.println(obj.isValidBST(root)); // should be false
	}
}