# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     def printTree(root: Optional[TreeNode]):
    #         if root:
    #             print(root.val)
    #             printTree(root.left)
    #             printTree(root.right)
        
    #     def invert(node: Optional[TreeNode]):
    #         if node:
    #             node.left = invert(node.right)
    #             node.right = invert(node.left)
 
    #         return node
        
    #     printTree(root)
    #     return invert(root)

    def printTree(self, root: Optional[TreeNode]):
        if root:
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # Not sure why this did not work
            # root.left = self.invertTree(root.right)
            # root.right = self.invertTree(root.left)

            left = self.invertTree(root.left)
            right = self.invertTree(root.right)

            root.left = right
            root.right = left

        return root

soln = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(5), TreeNode(6)))
soln.invertTree(root)
soln.printTree(root)