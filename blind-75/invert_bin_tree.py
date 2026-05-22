from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def printTree(self, root: Optional[TreeNode]) -> None:
    if root:
      print(root.val)
      self.printTree(root.left)
      self.printTree(root.right)
  
  
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    def invert(root: Optional[TreeNode]) -> Optional[TreeNode]:
      
      if root:
        left = invert(root.right)
        right = invert(root.left)
        
        root.left = left
        root.right = right
        
        return root
        
    
    if not root:
      return root
      
    return invert(root)


obj = Solution()

def extractTree(root: Optional[TreeNode], outList: List[int]) -> List[int]:
  if root:
    outList.append(root.val)
    if root.left:
      outList.append(extractTree(root.left, outList))
    if root.right:
      outList.append(extractTree(root.right, outList))
    
  
root = TreeNode(
  4,
  TreeNode(
    2, TreeNode(1), TreeNode(3)
  ),
  TreeNode(
    7, TreeNode(6), TreeNode(9)
  )
)

outList = []
extractTree(obj.invertTree(root), outList)
print(outList)

  
      

