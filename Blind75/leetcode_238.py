from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        prefixArray = [1]
        for n in nums:
            prefix *= n
            prefixArray.append(prefix)
        
        postfix = 1
        postfixArray = [1] * (len(nums) + 1)
        for i in range(len(nums))[::-1]:
            postfix *= nums[i]
            postfixArray[i] = postfix
        
        print(prefixArray)
        print(postfixArray)

        res = []
        for i in range(len(nums)):
            res.append(prefixArray[i] * postfixArray[i + 1])
        
        return res
    
obj = Solution()

def test__001():
    nums = [1,2,3,4]
    assert(obj.productExceptSelf(nums)) == [24, 12, 8, 6]

def test__002():
    nums = [-1,1,0,-3,3]
    assert(obj.productExceptSelf(nums)) == [0,0,9,0,0]