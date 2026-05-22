import java.util.*;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode() {}
	TreeNode(int val) {this.val = val;}
	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}

class Solution {
	public Map<Integer, List<Integer>> levelToNodes;

	Solution() {
		this.levelToNodes = new HashMap<>();
	}

	public void insertToLevel(int level, int val) {
		List<Integer> values;

		if (this.levelToNodes.containsKey(level)) {
			values = this.levelToNodes.get(level);
		} else {
			values = new ArrayList<>();
		}

		values.add(val);
		this.levelToNodes.put(level, values);
	}

	public void traverseNodes(TreeNode root, int level) {
		if (root != null) {
			insertToLevel(level, root.val);

			traverseNodes(root.left, level + 1);
			traverseNodes(root.right, level + 1);
		}
	}

	public List<List<Integer>> levelOrder (TreeNode root) {
		traverseNodes(root, 0);

		List<List<Integer>> res = new ArrayList<>();
		int len = levelToNodes.size();

		for(int i = 0; i < len; i++) {
			res.add(this.levelToNodes.get(i));
		}

		return res;
	}
}

class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		TreeNode root = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
		System.out.println(obj.levelOrder(root));
	}
}