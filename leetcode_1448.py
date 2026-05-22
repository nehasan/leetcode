'''
Leetcode 1448. Count Good Nodes in A Binary Tree
Author: Nahid Hasan Khan
'''

'''
Algorithm: class utilizes DFS approach to count good nodes from the top root node
- In each path to a targeted node we simply inject maximum value which has been\
    calculated so far to check whether the next node value is greater or less
- If the next node value (either left or right) is less then we simply ignore the\
    current node value by adding 0 with the rest
- If the next node value (...) is greater then we add 1 + rest
'''

from datetime import datetime

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        Returns int value of total good nodes
        Arguments:
        root - root of the tree, must be TreeNode
        '''
        
        def checkNextNode(node: TreeNode, maxValue) -> int:
            '''
            Returns 1 or 0 plus goodNodes based on left and right
            Arguments:
            node - node to be checked, must be TreeNode
            maxValue - maximum value so far to be compared with the current node value
            '''
            if node:
                if node.val < maxValue:
                    return 0 + checkNextNode(node.left, max(maxValue, node.val)) +\
                    checkNextNode(node.right, max(maxValue, node.val))
                else:
                    return 1 + checkNextNode(node.left, max(maxValue, node.val)) +\
                    checkNextNode(node.right, max(maxValue, node.val))
            
            return 0
        
        
        return 1 + checkNextNode(root.left, root.val) + checkNextNode(root.right, root.val)
        


obj = Solution()

'''
sample root = [3, 1, 4, 3, null, 1, 5]
output: 4 // passed
'''
# root = TreeNode(
#     3,
#     TreeNode(
#         1,
#         TreeNode(3, None),
#         None
#     ),
#     TreeNode(
#         4,
#         TreeNode(1, None),
#         TreeNode(5, None)
#     )
# )

'''
sample root = [3, 3, null, 4, 2]
output: 3 // passed
'''
# root = TreeNode(
#     3,
#     TreeNode(
#         3,
#         TreeNode(4),
#         TreeNode(2)
#     ),
#     None
# )

'''
sample root = [1]
output: 1
'''
root = TreeNode(1)
startTime = datetime.now()
print(obj.goodNodes(root))
endTime = datetime.now()
print((endTime - startTime).total_seconds() * 10**3)