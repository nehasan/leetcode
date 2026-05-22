from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  '''
  Approach using recursive DFS solution. So we go depth and we check that whether the base node is balanced or not
  If any of the nodes in depth is not balanced that means the entire sub tree from the root is not balanced.
  We return two values from each node/root [isBalanced, depth]
  On each root node we check if left balanced and right balanaced and abs (left depth - right depth) <= 1 which indicates
  balanced
  So then one node is imbalanced, that info will be back propagated to the original root node to determeine the balance
  '''
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
    def checkBalanced(node: Optional[TreeNode]):
      if node:
        leftTreeInfo = checkBalanced(node.left)
        rightTreeInfo = checkBalanced(node.right)
        
        lBalanced = leftTreeInfo[0]
        rBalanced = rightTreeInfo[0]
        lHeight = leftTreeInfo[1]
        rHeight = rightTreeInfo[1]
        
        # print(f"node : {node.val} info: {[(lBalanced and rBalanced and (abs(lHeight - rHeight) <= 1)), max(lHeight, rHeight) + 1]}")
        return [(lBalanced and rBalanced and (abs(lHeight - rHeight) <= 1)), max(lHeight, rHeight) + 1]
        
      return [True, 0]
    
    return checkBalanced(root)[0]

    


obj = Solution()
root1 = TreeNode(
  3,
  TreeNode(9),
  TreeNode(
    3,
    TreeNode(15),
    TreeNode(7)
  )
)

root2 = TreeNode(
  1,
  TreeNode(
    2,
    TreeNode(
      3,
      TreeNode(4),
      TreeNode(4)
    ),
    TreeNode(3)
  ),
  TreeNode(2)
)

root3 = TreeNode(
  1,
  TreeNode(
    2,
    TreeNode(
      3,
      TreeNode(4),
      None
    ),
    None
  ),
  TreeNode(
    2,
    None,
    TreeNode(
      3,
      None,
      TreeNode(4)
    )
  )
)

# print(obj.isBalanced(root))

def test_001():
  assert(obj.isBalanced(root1)) == True

def test_002():
  assert(obj.isBalanced(root2)) == False

def test_003():
  assert(obj.isBalanced(root3)) == False
  
        
        
    
    
    