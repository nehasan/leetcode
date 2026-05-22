from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lastLeft = 0
        left = 0
        right = sum(nums)

        foundPos = -1
        for i, x in enumerate(nums):
            left += lastLeft
            right -= x

            if left == right:
                foundPos = i
                break
            
            lastLeft = x
        
        return foundPos

sol = Solution()

def test_case_001():
    nums = [1,7,3,6,5,6] # output 3
    assert sol.pivotIndex(nums) == 3

def test_case_002():
    nums = [1,2,3] # output -1
    assert sol.pivotIndex(nums) == -1
    
def test_case_003():
    nums = [2,1,-1] # output 0
    assert sol.pivotIndex(nums) == 0