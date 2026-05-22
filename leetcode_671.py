from typing import List, Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfsSearch(node: Optional[TreeNode], sortedNums: List[int]) -> None:
            if node:
                if node.left:
                    if node.left.val < node.right.val:
                        dfsSearch(node.left, sortedNums)
                        sortedNums.append(node.val)
                        dfsSearch(node.right, sortedNums)
                    else:
                        dfsSearch(node.right, sortedNums)
                        sortedNums.append(node.val)
                        dfsSearch(node.left, sortedNums)
                else:
                    sortedNums.append(node.val)
                
                
        sortedNums = list()
        dfsSearch(root, sortedNums)
        
        if len(sortedNums) < 2:
            return -1
        
        print(sortedNums)
        minVal = sortedNums[0]
        
        for e in sortedNums[1:]:
            if e > minVal:
                return e
        
        return -1


obj = Solution()
root = TreeNode(
    2,
    TreeNode(
        2
    ),
    TreeNode(
        5,
        TreeNode(5),
        TreeNode(7)
    )
)
# output 5

root = TreeNode(
    2,
    TreeNode(2),
    TreeNode(2)
)

root = TreeNode(
    5,
    TreeNode(8),
    TreeNode(5)
)

root = TreeNode(
    2,
    TreeNode(2),
    TreeNode(2147483647)
)
print(obj.findSecondMinimumValue(root))