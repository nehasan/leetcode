# leetcode 236

from typing import List
from collections import deque, defaultdict

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:

	def dfs(self, root: TreeNode, path: defaultdict, nodes: deque) -> None:
		if root:
			nodes.append(root)
			path[root.val] = nodes.copy()

			self.dfs(root.left, path, nodes)
			self.dfs(root.right, path, nodes)
			nodes.pop()

	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

		path = defaultdict(deque)
		nodes = deque()

		self.dfs(root, path, nodes)

		pAncestors = path[p.val]
		qAncestors = path[q.val]

		pAncestors.reverse()
		qAncestors.reverse()

		for pA in pAncestors:
			for qA in qAncestors:
				if pA.val == qA.val:
					return pA

		return root


obj = Solution()

p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
q = TreeNode(1, TreeNode(0), TreeNode(8))
root = TreeNode(3, p, q)
print(obj.lowestCommonAncestor(root, p, q).val)

q = TreeNode(4)
p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), q))
branches = TreeNode(1, TreeNode(0), TreeNode(8))
root = TreeNode(3, p, branches)
print(obj.lowestCommonAncestor(root, p, q).val)