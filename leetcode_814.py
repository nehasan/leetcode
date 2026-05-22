'''
Leetcode 814. Binary Tree Pruning
Nahid Hasan Khan March 1st 2024
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def printTree(node: Optional[TreeNode]):
            if node != None:
                printTree(node.left)
                print(node.val)
                printTree(node.right)
        
        def pruneChild(node: Optional[TreeNode]) -> bool:
            if node == None:
                return True
                
            pruneLeft = True
            pruneRight = True
            
            pruneLeft = pruneChild(node.left)
            if pruneLeft == True:
                node.left = None
                
            pruneRight = pruneChild(node.right)
            if pruneRight == True:
                node.right = None
            
            return node.val == 0 and pruneLeft and pruneRight
        
        
        if root == None:
            return root
        if pruneChild(root) == True:
            return None
        else:
            return root
        # printTree(root)
        # return None root.val == 0 else root


obj = Solution()
# root = TreeNode(
#     1,
#     None,
#     TreeNode(
#         0,
#         TreeNode(0),
#         TreeNode(1)
#     )
# )

# root = TreeNode(
#     1,
#     TreeNode(
#         0,
#         TreeNode(0),
#         TreeNode(0)
#     ),
#     TreeNode(
#         1,
#         TreeNode(0),
#         TreeNode(1)
#     )
# )

root = TreeNode(
    1,
    TreeNode(
        1,
        TreeNode(
            1,
            TreeNode(0),
            None
        ),
        TreeNode(1)
    ),
    TreeNode(
        0,
        TreeNode(0),
        TreeNode(1)
    )
)

obj.pruneTree(root)