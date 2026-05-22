
class TreeNode:
    def __init__(self, left: None, right: None, val=0) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    leafsRootOne = []
    leafsRootTwo = []

    def preOrderTraverse(self, node: TreeNode, treeNo: int) -> None:
        if node != None:
            if (node.left == None) and (node.right == None):
                # its a leaf
                if treeNo == 0:
                    self.leafsRootOne.append(node.val)
                else:
                    self.leafsRootTwo.append(node.val)

            self.preOrderTraverse(node.left, treeNo)
            self.preOrderTraverse(node.right, treeNo)

    def leafSimilar(self, rootOne: TreeNode, rootTwo: TreeNode) -> bool:
        self.preOrderTraverse(rootOne, 0)
        self.preOrderTraverse(rootTwo, 1)

        # print(self.leafsRootOne)
        # print(self.leafsRootTwo)

        return ''.join(str(x) for x in self.leafsRootOne) == ''.join(str(x) for x in self.leafsRootTwo)


obj = Solution()
rootOne = TreeNode(
        TreeNode(TreeNode(None, None, 4), TreeNode(None, None, 5), 2),
        TreeNode(TreeNode(None, None, 6), TreeNode(None, None, 7), 3),
        1
    )

rootTwo = TreeNode(
        TreeNode(TreeNode(None, None, 4), TreeNode(None, None, 5), 2),
        TreeNode(TreeNode(None, None, 6), TreeNode(None, None, 8), 3),
        1
    )

res = obj.leafSimilar(rootOne, rootTwo)
print(res)
        
