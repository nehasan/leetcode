// leetcode 572

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


class Solution {

	public boolean isExactSubTree(TreeNode p, TreeNode q) {
		if (p == null && q == null) {
			return true;
		} else if ((p != null && q == null) || (p == null && q != null)) {
			return false;
		} else if (p.val != q.val) {
			return false;
		} else {
			return isExactSubTree(p.left, q.left) && isExactSubTree(p.right, q.right);
		}
	}

	public boolean isSubTree(TreeNode root, TreeNode subRoot) {
		if (root != null) {
            // because tree can have duplicate values,
            // so if one root does not work, we check another root
			if (root.val == subRoot.val && isExactSubTree(root, subRoot)) {
				return true;
			} else {
				return (isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot));
			}
		}
		return false;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		TreeNode node4 = new TreeNode(4, new TreeNode(1), new TreeNode(2));
		TreeNode node3 = new TreeNode(3, node4, new TreeNode(5));
		System.out.println(obj.isSubTree(node3, node4));

		TreeNode node4Extra = new TreeNode(4, new TreeNode(1), new TreeNode(2, new TreeNode(0), null));
		node4 = new TreeNode(4, new TreeNode(1), new TreeNode(2));
		node3 = new TreeNode(3, node4, new TreeNode(5));
		System.out.println(obj.isSubTree(node3, node4Extra));
	}
}