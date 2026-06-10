# Definition for a binary tree node.
from os import pread
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    map = dict()
    preOrderIndex = 0

    def printTree(self, root: Optional[TreeNode]):
        if root is None:
            print('null')
        if root:
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = 0
        for n in inorder:
            self.map[n] = index
            index += 1
        
        root = self.build(preorder, inorder, 0, len(preorder) - 1)
        self.printTree(root)
        return root
    
    def build(self, preorder, inorder, leftIndex, rightIndex):
        if leftIndex > rightIndex:
            return None
        
        rootVal = preorder[self.preOrderIndex]
        self.preOrderIndex += 1
        rootIndex = self.map[rootVal]

        root = TreeNode(
            rootVal,
            self.build(preorder, inorder, leftIndex, rootIndex - 1),
            self.build(preorder, inorder, rootIndex + 1, rightIndex),
        )

        return root

            
soln = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
# preorder = [3,9,20]
# inorder = [9,3,20]
soln.buildTree(preorder, inorder)