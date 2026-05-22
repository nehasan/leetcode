from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        numSet = set()
        
        for n in nums:
            if n in numSet:
                return True
            
            numSet.add(n)
        
        
        return False


obj = Solution()

def test_0001():
    nums = [1,2,3,1]
    assert(obj.containsDuplicate(nums)) == True
    

def test_0002():
    nums = [1,2,3,4]
    assert(obj.containsDuplicate(nums)) == False