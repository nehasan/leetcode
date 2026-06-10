// leetcode 230

import java.util.*;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode (int val) {
		this.val = val;
	}
	TreeNode (int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}


class Solution {
	public void inorderTraverse (TreeNode root, List<Integer> inorder) {
		if (root != null) {
			inorderTraverse(root.left, inorder);
			inorder.add(root.val);
			inorderTraverse(root.right, inorder);
		}
	}

	public int kthSmallest(TreeNode root, int k) {
		List<Integer> inorder = new ArrayList<>();

		inorderTraverse(root, inorder);

		return inorder.get((k - 1));
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		TreeNode root = new TreeNode(3, new TreeNode(1, new TreeNode(1), null), new TreeNode(4));
		root = new TreeNode(5, new TreeNode(3, new TreeNode(2, new TreeNode(1), null), new TreeNode(4)), new TreeNode(6));

		System.out.println(obj.kthSmallest(root, 3));
	}
}