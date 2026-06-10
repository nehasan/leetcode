// leetcode 671

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
	public void inorderTraverse (TreeNode root, PriorityQueue<Integer> heap) {
		if (root != null) {
			inorderTraverse(root.left, heap);
			heap.add(root.val);
			inorderTraverse(root.right, heap);
		}
	}

	public int findSecondMinimumValue(TreeNode root) {
		// List<Integer> inorder = new ArrayList<>();
		PriorityQueue<Integer> heap = new PriorityQueue<>();

		inorderTraverse(root, heap);

		int firstMinVal = heap.poll();

		while(!heap.isEmpty()){
			int secMinVal = heap.poll();
			if (secMinVal > firstMinVal) {
				return secMinVal;
			}
		}

		return -1;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		TreeNode root = new TreeNode(2, new TreeNode(2), new TreeNode(5, new TreeNode(5), new TreeNode(7)));
		System.out.println(obj.findSecondMinimumValue(root)); //5

		root = new TreeNode(2, new TreeNode(2), new TreeNode(2));
		System.out.println(obj.findSecondMinimumValue(root)); // -1

		root = new TreeNode(5, new TreeNode(8), new TreeNode(5));
		System.out.println(obj.findSecondMinimumValue(root)); // 8
	}
}