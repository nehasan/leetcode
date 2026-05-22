import java.util.*;

class TreeNode {
	public int val;
	public TreeNode left;
	public TreeNode right;
	
	TreeNode(int val) { this.val = val; }
	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}

class Solution {
	int maxDiameter;
	
	Solution() {
		this.maxDiameter = 0;
	}
	
	public void setMaxDiameter(int diameter) {
		this.maxDiameter = diameter;
	}
	
	public int getMaxDiameter(){
		return this.maxDiameter;
	}
	
	public int[] dfsToFindMaxHeight(TreeNode root) {
		if (root != null) {
			int leftHeight = dfsToFindMaxHeight(root.left)[0];
			int rightHeight = dfsToFindMaxHeight(root.right)[0];
			
			setMaxDiameter(Math.max(getMaxDiameter(), leftHeight + rightHeight));
			return new int[] { Math.max(leftHeight, rightHeight) + 1, getMaxDiameter() };
		}
		
		return new int[] {0, 0};
	}
	
	public int diameterOfBinaryTree(TreeNode root) {
		dfsToFindMaxHeight(root);
		return getMaxDiameter();
	}
}

class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();
		// TreeNode root = new TreeNode(
// 			1,
// 			new TreeNode(2),
// 			new TreeNode(
// 				3,
// 				new TreeNode(4),
// 				new TreeNode(5)
// 			)
// 		);
// 		System.out.println(obj.diameterOfBinaryTree(root));
		TreeNode root = new TreeNode(
    	1,
    	new TreeNode(2),
    	new TreeNode(
      	3,
      	new TreeNode(
        	4,
        	new TreeNode(
          	6,
          	new TreeNode(10),
						null
        	),
        	new TreeNode(7)
      	),
      	new TreeNode(
        	5,
        	new TreeNode(8),
        	new TreeNode(
          	9,
          	null,
          	new TreeNode(11)
        	)
      	)
    	)
  	);
		Test test = new Test();
		test.assertEqual("Test name", obj.diameterOfBinaryTree(root), 6);
	}
}