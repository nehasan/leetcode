from typing import List, Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    

class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    
    if root:
      if p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
      elif p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
      else:
        return root


obj = Solution()

root = TreeNode(
  6,
  TreeNode(
    2,
    TreeNode(0),
    TreeNode(
      4,
      TreeNode(3),
      TreeNode(5)
    )
  ),
  TreeNode(
    8,
    TreeNode(7),
    TreeNode(9)
  )
)

print(obj.lowestCommonAncestor(root, root.left, root.right).val)