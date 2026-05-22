# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], inOrderStack: List[int]) -> bool:
            if node:
                # Go for depth and left child tree validation
                if validate(node.left, inOrderStack) is False:
                    return False
                
                # Check if it violates left < root < right
                if len(inOrderStack) > 0 and node.val <= inOrderStack.pop():
                    return False
                
                # If everything is ok then push node value to in order traversal stack
                inOrderStack.append(node.val)
                # If ev. is ok check for right child tree
                return validate(node.right, inOrderStack)
            
            return True
        
        return validate(root, [])
        

obj = Solution()
root = TreeNode(
    5,
    TreeNode(1),
    TreeNode(
        4,
        TreeNode(3),
        TreeNode(6)
    )
) # False

root = TreeNode(
    5,
    TreeNode(4),
    TreeNode(
        6,
        TreeNode(3),
        TreeNode(7)
    )
) # False

# root = TreeNode(
#     2,
#     TreeNode(1),
#     TreeNode(3)
# ) # True

print(obj.isValidBST(root))
                    
                