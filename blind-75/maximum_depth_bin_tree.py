class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    
    def dfsToMaxDepth(root: TreeNode) -> int:
      if root:
        leftDepth = dfsToMaxDepth(root.left)
        rightDepth = dfsToMaxDepth(root.right)
        
        return 1 + max(leftDepth, rightDepth)
      
      return 0
    
    return dfsToMaxDepth(root)


obj = Solution()

def test__001():
  root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
  )
  assert(obj.maxDepth(root)) == 2

def test__002():
  root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(
      3,
      TreeNode(4),
      TreeNode(5)
    )
  )
  assert(obj.maxDepth(root)) == 2