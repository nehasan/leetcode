from collections import defaultdict
from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    
    numsDict = defaultdict(int)
    majorElmInfo = [-1, -10e9 + 1]
    
    for n in nums:
      numsDict[n] += 1
      if numsDict[n] > majorElmInfo[1]:
        majorElmInfo[0] = n
        majorElmInfo[1] = numsDict[n]
    
    return majorElmInfo[0]
    

obj = Solution()

def test_001():
  nums = [3,2,3]
  assert(obj.majorityElement(nums)) == 3

def test_001():
  nums = [2,2,1,1,1,2,2]
  assert(obj.majorityElement(nums)) == 2