# leetcode 105

from typing import List, Optional
from collections import deque


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def printTree(self, root: Optional[TreeNode]) -> None:
		pass
		if root:
			print(root.val)
			self.printTree(root.left)
			self.printTree(root.right)


	'''
	Approach recursive tree building using left inorder array and right inorder array
	Pop the preorder list to get the root value and find the index of that root value in inorder
	Now the root.left would be build using the left inorder array and root.right would be build using
	the right inorder array 
	'''
	def buildFromPreorderInorder(self, preorderQ: deque, inorder: List[int]) -> Optional[TreeNode]:
		root = None
		if len(preorderQ) > 0:
			if len(inorder) > 0:
				rootVal = preorderQ.popleft()
				root = TreeNode(rootVal)
				rootIndex = inorder.index(rootVal)
				root.left = self.buildFromPreorderInorder(preorderQ, inorder[0:rootIndex])
				root.right = self.buildFromPreorderInorder(preorderQ, inorder[rootIndex + 1: len(inorder)])

		return root


	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		preorderQ = deque(preorder)
		tree = self.buildFromPreorderInorder(preorderQ, inorder)
		# self.printTree(tree)
		return tree


obj = Solution()

preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]

obj.buildTree(preorder, inorder)