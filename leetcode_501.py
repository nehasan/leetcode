# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import defaultdict

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def traverseBST(node: Optional[TreeNode], modeMap: defaultdict) -> None:
            if node:
                traverseBST(node.left, modeMap)
                modeMap[node.val] += 1
                traverseBST(node.right, modeMap)

        
        modeMap = defaultdict(int)
        traverseBST(root, modeMap)

        maxMode = 0
        res = []
        for k, v in modeMap.items():
            if maxMode < v:
                res = [k]
                maxMode = v
            elif maxMode == v:
                res.append(k)
        
        return res


# obj = Solution()
# root = TreeNode(
#     1,
#     None,
#     TreeNode(
#         2,
#         TreeNode(2),
#         None
#     )
# ) # [2]

# root = TreeNode(0) # [0]

# print(obj.findMode(root))
        