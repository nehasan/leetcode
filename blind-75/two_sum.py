from collections import defaultdict
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # read the input and map them to a hash
        numDict = defaultdict(list)
        
        for i, n in enumerate(nums):
            numDict[n] += [i]
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numDict:
                indices = numDict[diff]
                # make sure not including same index twice for same number
                if len(indices) > 1 or (len(indices) == 1 and diff != n):
                    a = [x for x in indices if x != i][0]
                    b = [x for x in numDict[n] if x != a][0]
                    return [a, b]
        


obj = Solution()

def test_0001():
    nums = [2,7,11,15]
    target = 9 # passed
    assert(obj.twoSum(nums, target)) == [1, 0]

def test_0002():
    nums = [3,2,4]
    target = 6 # passed
    assert(obj.twoSum(nums, target)) == [2, 1]

def test_0003():
    nums = [3,3]
    target = 6 # passed
    assert(obj.twoSum(nums, target)) == [1, 0]