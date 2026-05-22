from typing import List
from typing import Dict
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFreqSumRecursively(self, root: Optional[TreeNode], maxFreq: int, sumMap: Dict) -> List[int]:
        if root is None:
            return 0
        
        leftSum = self.findFreqSumRecursively(root.left, maxFreq, sumMap)
        rightSum = self.findFreqSumRecursively(root.right, maxFreq, sumMap)
        totalSum = root.val + leftSum + rightSum
        
        print(f"--- root: #{root.val}, leftSum: #{leftSum}, , rightSum: #{rightSum}, totalSum: #{totalSum}")
        
        if sumMap.get(totalSum) is None:
            sumMap[totalSum] = 1
        else:
            sumMap[totalSum] += 1
        
        return totalSum
	
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        maxFreq = 0
        sumMap = dict()
        
        self.findFreqSumRecursively(root, maxFreq, sumMap)
        print(sumMap)
        sortedMap = sorted(sumMap.items(), key=lambda item: item[1], reverse=True)
        
        res = list()
        for k,v in sortedMap:
            if v > maxFreq:
                res = [k]
                maxFreq = max(maxFreq, v)
            elif v == maxFreq:
                res.append(k)
        
        return res
        

# Example usage:
        
sol = Solution()
root = TreeNode(5, TreeNode(2), TreeNode(-3))
print(sol.findFrequentTreeSum(root))

root = TreeNode(5, TreeNode(2), TreeNode(-5))
print(sol.findFrequentTreeSum(root))
	