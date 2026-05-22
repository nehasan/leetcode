from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def __init__(self):
    self.maxDiameter = 0
    
  '''
  Approach: DFS search to find depth of each node and diameter of a particular node is
  diameter(node1) = leftDepth + rightDepth, counter a global variable to calculate current max diameter
  of each node
  '''
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
    def dfsToFindMaxHeight(root: Optional[TreeNode]) -> int:
      
      if root:
        leftHeight = dfsToFindMaxHeight(root.left)[0]
        rightHeight = dfsToFindMaxHeight(root.right)[0]
      
        print(f"at node {root.val } before maxDiameter: {self.maxDiameter}")
        self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)
        print(f"at node: {root.val}, lH: {leftHeight}, rH: {rightHeight}, currMaxDiameter: {self.maxDiameter}")
        return [max(leftHeight, rightHeight) + 1, self.maxDiameter]
      
      return [0, 0]
    
    return dfsToFindMaxHeight(root)[1]


obj = Solution()
root = TreeNode(
  1,
  TreeNode(2),
  TreeNode(
    3,
    TreeNode(
      4,
      TreeNode(
        6,
        TreeNode(10),
      ),
      TreeNode(7)
    ),
    TreeNode(
      5,
      TreeNode(8),
      TreeNode(
        9,
        None,
        TreeNode(11)
      )
    )
  )
)
print(obj.diameterOfBinaryTree(root))

def test__001():
  root = TreeNode(
    1,
    TreeNode(
      2,
      TreeNode(4),
      TreeNode(5)
    ),
    TreeNode(3)
  )
  assert(obj.diameterOfBinaryTree(root)) == 3

def test__002():
  root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(
      3,
      TreeNode(
        4,
        TreeNode(
          6,
          TreeNode(10),
        ),
        TreeNode(7)
      ),
      TreeNode(
        5,
        TreeNode(8),
        TreeNode(
          9,
          None,
          TreeNode(11)
        )
      )
    )
  )
  assert(obj.diameterOfBinaryTree(root)) == 6