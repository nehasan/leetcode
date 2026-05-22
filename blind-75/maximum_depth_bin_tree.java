class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;
	
	TreeNode(int val) {
		this.val = val;
	}
	
	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}

class Solution {
	public int dfsToFindMaxDepth(TreeNode root) {
		if (root != null) {
			int leftDepth = dfsToFindMaxDepth(root.left);
			int rightDepth = dfsToFindMaxDepth(root.right);
			
			return 1 + Math.max(leftDepth, rightDepth);
		}
		
		return 0;
	}
	
	public int maxDepth(TreeNode root) {
		return dfsToFindMaxDepth(root);
	}
}

class Main {
	public static void main (String[] args) {
		Solution obj = new Solution();
		Test tester = new Test();
		
		// Test case 1
		TreeNode root = new TreeNode(
			1,
			new TreeNode(2),
			new TreeNode(3)
		);
		tester.assertEqual("Test case 1", obj.maxDepth(root), 2);
		
		// Test case 2
		root = new TreeNode(
			1,
			new TreeNode(2),
			new TreeNode(
				3,
				new TreeNode(4),
				new TreeNode(5)
			)
		);
		tester.assertEqual("Test case 1", obj.maxDepth(root), 3);
	}
}