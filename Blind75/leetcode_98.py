# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    inOrderStack = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            print(f'processing root: {root.val} in order stack now: {self.inOrderStack}')
            # Go for left node and if it returns false then whole tree is false
            if self.isValidBST(root.left) == False:
                return False

            # Check the root value with the inorder traversal node list top
            # If the root value is less then the top node value then it is false
            if len(self.inOrderStack) > 0 and self.inOrderStack.pop() >= root.val:
                return False
            
            # Else push the current root value to inorder stack list
            print(f"inorder before: {self.inOrderStack}")
            self.inOrderStack.append(root.val)
            print(f"inorder after: {self.inOrderStack}")
            return self.isValidBST(root.right)
            
        return True
    

soln = Solution()
# root = TreeNode(2, TreeNode(1), TreeNode(3)) # true
# root = TreeNode(1, TreeNode(2), TreeNode(3)) # false
# root = TreeNode(1, TreeNode(4), TreeNode(3)) # true
# root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))) # false
# root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7))) # false
root = TreeNode(8, TreeNode(-70), TreeNode(81)) # true
print(soln.isValidBST(root))