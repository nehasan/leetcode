'''
Leetcode 196. Binary Tree Right Side View
Author: Nahid Hasan Khan
'''

'''
Algorithm utilizes BFS approach to traverse all the nodes and takes only rightmost nodes
- Apply BFS to collect the nodes in a queue with node information and the current level
- Later while processing the nodes from queue if the level is not found in the set()\
    then enlist the node value into the final node values[], and add the level value to\
    level set () to mark that already one node from this level is collected
- If second nodes with same level comes we simply ignore that node
'''

from typing import Optional
from typing import List

# class definition of TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Returns list of numbers collected from each node of the right children
        Arguments:
        root - An optional TreeNode root (Optional[TreeNode]), can be None
        '''
        
        if not root:
            return []
            
        level = 0
        nodeQueue = list()
        nodeValues = list()
        levelSet = set()
        
        # Insert the root node and it's level 0 to queue
        nodeQueue.append((root, level))
        
        # Dequeue each node to process untill the queue is empty
        while len(nodeQueue) > 0:
            # Deqeue node info from the queue
            nodeInfo = nodeQueue.pop(0)
            print(f'--- DEBUG nodeInfo: {nodeInfo[0].val}, {nodeInfo[1]}')
            
            # If the level is not already added, add the node to the final list
            # Mark the level is processed by adding level value to the set
            if (nodeInfo[1] in levelSet) == False:
                nodeValues.append(nodeInfo[0].val)
                levelSet.add(nodeInfo[1])
            
            # Add the right node to the queue for further processing
            # Right nodes have the priority over the left ones
            if nodeInfo[0].right != None:
                nodeQueue.append((nodeInfo[0].right, nodeInfo[1] + 1))
                
            # Add the left node to the queue for further processing
            if nodeInfo[0].left != None:
                nodeQueue.append((nodeInfo[0].left, nodeInfo[1] + 1))
        
        return nodeValues


obj = Solution()
# sample input: root = [1,2,3,null,5,null,4]
# output: [1,3,4] // passed
# root = TreeNode(
#     1,
#     TreeNode(
#         2,
#         None,
#         TreeNode(5)
#     ),
#     TreeNode(
#         3,
#         None,
#         TreeNode(4)
#     )
# )

# sample input: root = [1, null, 3]
# output: [1,3] // passed
# root = TreeNode(
#     1,
#     None,
#     TreeNode(3)
# )

# sample input: root = []
# output: [] // passed
# root = None

# sample input: root [1, 2]
# output: [1, 2] // passed
# root = TreeNode(
#     1,
#     TreeNode(2),
#     None
# )

# sample input: root [1, 2, 3, null, 5, 6, null, 4]
# output: [1,3,6,4] //
# root = TreeNode(
#     1,
#     TreeNode(
#         2,
#         None,
#         TreeNode(
#             5,
#             TreeNode(4)
#         )
#     ),
#     TreeNode(
#         3,
#         TreeNode(6),
#         None
#     )
# )


print(obj.rightSideView(root))
        