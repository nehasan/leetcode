# leetcode 297

from typing import List
from collections import defaultdict

# Definition for a binary tree node.

class TreeNode(object):
	def __init__(self, x=0, left=None, right=None):
		self.val = x
		self.left = left
		self.right = right

class Codec:
	def __init__(self):
		self.serialized = ""
		self.deserialized = None
		self.rootIndex = 0


	def validateTree(self, root: TreeNode) -> None:
		if root:
			print(root.val)
			self.validateTree(root.left)
			self.validateTree(root.right)


	def serialize(self, root):
		"""Encodes a tree to a single string.

		:type root: TreeNode
		:rtype: str
		"""
		def preorderTraverse(root: TreeNode, preorder: List[str]) -> None:
			if root:
				preorder.append(str(root.val))
				# print(f"preorder now: {preorder}")
				preorderTraverse(root.left, preorder)
				preorderTraverse(root.right, preorder)

		def inorderTraverse(root: TreeNode, inorder: List[str]) -> None:
			if root:
				inorderTraverse(root.left, inorder)
				inorder.append(str(root.val))
				# print(f"inorder now: {inorder}")
				inorderTraverse(root.right, inorder)

		preorder = []
		inorder  = []

		# self.validateTree(root)
		if not root:
			return ""
		preorderTraverse(root, preorder)
		inorderTraverse(root, inorder)

		self.serialized = "|".join(preorder) + "+" + "|".join(inorder)
		print(f"self.serialized : {self.serialized}")
		return self.serialized


	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		
		:type data: str
		:rtype: TreeNode
		"""

		def buildTree(
				inorderMap:defaultdict, preorder: List[str], inorder: List[str], leftOffset: int, rightOffset: int) -> TreeNode:
			# print(f"leftOffset {leftOffset}, rightOffset {rightOffset}")
			if leftOffset <= rightOffset:
				root = TreeNode(int(preorder[self.rootIndex]))
				offset = inorderMap[preorder[self.rootIndex]]
				# print(f"self.rootIndex {self.rootIndex}")
				self.rootIndex += 1
				# print(f"self.rootIndex {self.rootIndex}")
				root.left = buildTree(inorderMap, preorder, inorder, leftOffset, offset - 1)
				root.right = buildTree(inorderMap, preorder, inorder, offset + 1, rightOffset)

				return root
			return None

		if data == "":
			return None
			
		token = data.split("+")
		# print(f"token {token}")
		preorder = token[0].split("|")
		inorder  = token[1].split("|")
		# print(f"preorder list {preorder}, inorder list {inorder}")

		inorderMap = defaultdict(int)
		for i, nodeVal in enumerate(inorder):
			inorderMap[nodeVal] = i

		# print(f"inorderMap {inorderMap}")
		self.deserialized = buildTree(inorderMap, preorder, inorder, 0, len(inorder) - 1)
		self.validateTree(self.deserialized)
		return self.deserialized


ser = Codec()
deser = Codec()

root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
# root = TreeNode(1, TreeNode(2), TreeNode(3))
deser.deserialize(ser.serialize(root))

