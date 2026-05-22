// leetcode 236

import java.util.*;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode() {}
	TreeNode(int val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}

class Solution {

	/*
	* Approach dfs to traverse the nodes and map the path (including its own node).
	* 
	*/
	public void dfs(TreeNode root, Map<Integer, TreeNode> nodeDict, Map<Integer, List<TreeNode>> path, Stack<TreeNode> nodes) {
		if (root != null) {
			nodeDict.put(root.val, root);
			nodes.add(root);
			List<TreeNode> nodesCopy = new ArrayList<>(nodes);
			path.put(root.val, nodesCopy);
			// System.out.println("node is: " + root.val);
			// for (TreeNode node : nodes) {
			// 	System.out.println("copy node is: " + node.val);
			// }
			dfs(root.left, nodeDict, path, nodes);
			dfs(root.right, nodeDict, path, nodes);
			// removes the node from the path for the upper level nodes or another nodes on the right
			nodes.pop();
		}
	}

	public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
		Map<Integer, TreeNode> nodeDict = new HashMap<>();
		Map<Integer, List<TreeNode>> path = new HashMap<>();
		Stack<TreeNode> nodes = new Stack<>();

		dfs(root, nodeDict, path, nodes);

		List<TreeNode> pAncestors = path.get(p.val);
		List<TreeNode> qAncestors = path.get(q.val);

		for (int i = pAncestors.size() - 1; i >= 0; i--) {
			// System.out.println("checking p.val : " + pAncestors.get(i).val);
			for (int j = qAncestors.size() - 1; j >= 0; j--) {
				// System.out.println("with q.val : " + qAncestors.get(j).val);
				if (pAncestors.get(i).val == qAncestors.get(j).val) {
					return pAncestors.get(i);
				}
			}
		}

		return root;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		// TreeNode p = new TreeNode(5, new TreeNode(6), new TreeNode(2, new TreeNode(7), new TreeNode(4)));
		// TreeNode q = new TreeNode(1, new TreeNode(0), new TreeNode(8));
		// TreeNode root = new TreeNode(3, p, q);
		// System.out.println(obj.lowestCommonAncestor(root, p, q).val);

		// TreeNode q = new TreeNode(4);
		// TreeNode p = new TreeNode(5, new TreeNode(6), new TreeNode(2, new TreeNode(7), q));
		// TreeNode branches = new TreeNode(1, new TreeNode(0), new TreeNode(8));
		// TreeNode root = new TreeNode(3, p, branches);
		// System.out.println(obj.lowestCommonAncestor(root, p, q).val);
	}
}