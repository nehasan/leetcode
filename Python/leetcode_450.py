# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Algorithm:
Recursively search for required node, if key is less than root value then search through left subtree, else right subtree
Following cases need to be considered when we find the node
Case 1: return and assign left subtree when there is no right node
Case 2: return and assign right subtree when there is no left node
Case 3: dig deeper of the right child to find the min most node value, assign it as value of the root and again recursively search with curr.val to remove the node from the right subtree
'''

from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            
            curr = root.right
            while curr.left:
                curr = curr.left

            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)

        return root