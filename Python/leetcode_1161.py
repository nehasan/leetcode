
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque


class Solution:
    def sumLevel(self, map, rootNode, currLevel):
        if rootNode is not None:
            if map.get(currLevel) is None:
                map[currLevel] = rootNode.val
            else:
                map[currLevel] += rootNode.val
            
            self.sumLevel(map, rootNode.left, currLevel + 1)
            self.sumLevel(map, rootNode.right, currLevel + 1)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        Maintained a global map to track the total sum
        map[1] = 23 // means level one total sum is 23
        map[2] = 45 // level 2 total sum
        '''
        map = dict()
        self.sumLevel(map, root, 1)

        maxLevel = 0
        maxSum = 0
        for k, v in map.items():
            if v > maxSum:
                maxSum = v
                maxLevel = k
        
        return maxLevel

            

soln = Solution()
# root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
root = TreeNode(989, None, TreeNode(10250, TreeNode(98693), TreeNode(-89388, None, TreeNode(-32127))))
print(soln.maxLevelSum(root))