from typing import List, Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    """
    Approach: Recursive inorder tree traversal and store the values in an array.
    The stored array will be already sorted as we traverse the BST (Binary search Tree)
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        def dfsSearch(node: Optional[TreeNode], sortedNums: List[int]) -> None:
            if node:
                if node.left:
                    dfsSearch(node.left, sortedNums)
                
                sortedNums.append(node.val)
                
                if node.right:
                    dfsSearch(node.right, sortedNums)
        
        sortedNums = []
        dfsSearch(root, sortedNums)
        
        return sortedNums[k-1]


obj = Solution()
root = TreeNode(
    3,
    TreeNode(
        1,
        None,
        TreeNode(2)
    ),
    TreeNode(4)
)

root = TreeNode(
    5,
    TreeNode(
        3,
        TreeNode(
            2,
            TreeNode(1)
        ),
        TreeNode(4)
    ),
    TreeNode(6)
)

# print(obj.kthSmallest(root, 1))
# print(obj.kthSmallest(root, 3))