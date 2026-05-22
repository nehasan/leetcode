from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    
class Solution:
    currMax = 0
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def findLongest(node, nextDir):
            if node == None:
                return 0
        
            leftMax = 0
            rightMax = 0
        
            if nextDir == 'l':
                leftMax = 1 + findLongest(node.left, 'r')
                leftMax = max(self.currMax, leftMax)
                rightMax = findLongest(node.right, 'l')
                
            elif nextDir == 'r':
                leftMax = findLongest(node.left, 'r')
                rightMax = 1 + findLongest(node.right, 'l')
                rightMax = max(self.currMax, rightMax)
        
            return max(leftMax, rightMax)
        
        
        return (max(findLongest(root.left, 'r'), findLongest(root.right, 'l')))



obj = Solution()
root = TreeNode(
    1,
    None,
    TreeNode(
        1,
        TreeNode(1),
        TreeNode(
            1,
            TreeNode(
                1,
                None,
                TreeNode(
                    1,
                    None,
                    TreeNode(1)
                )
            ),
            TreeNode(1)
        )
    )
)
'''

# sample root [1]
# expected output: 0
root = TreeNode(
    1
)

# sample root [1, 1, 1, null, null, null, null]
# sample output: 1
root = TreeNode(
    1,
    TreeNode(1),
    TreeNode(1)
)

# sample root [1, null, 1, 1, null, null, 1]
# sample output: 3
root = TreeNode(
    1,
    None,
    TreeNode(
        1,
        TreeNode(
            1,
            None,
            TreeNode(1),
        ),
        None
    )
)

# sample root [1, 1, 1, null, null, null, null]
# sample output: 3
root = TreeNode(
    1,
    None,
    TreeNode(
        1,
        None,
        TreeNode(
            1,
            TreeNode(1),
            None
        )
    )
)
'''
print(obj.longestZigZag(root))