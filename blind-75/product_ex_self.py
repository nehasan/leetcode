from typing import List

class Solution:
    '''
    Approach: Calculate prefix sum and postfix sum and then find the targeted product arr using those
    - Suppose nums ar [1,2,3,4], now calculate the prefix sum and store [1,1,2,6,24] // prefix[0] = 1 is a starter
    - Now with some similar operation find postfix sum from the behind, [24,24,12,4,1] // postfix[length - 1] = 1 is also a starter
    - Now the resutant array would be the calculation of prefix[i] and postfix[i+1], res[i] = prefix[i] * postfix[i + 1]
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        
        prefix = 1
        prefixArr = [1]
        for n in nums:
            prefix *= n
            prefixArr.append(prefix)
        
        postfix = 1
        postfixArr = [1] * (len(nums) + 1)
        for i in range(len(nums))[::-1]:
            postfix *= nums[i]
            postfixArr[i] = postfix
        
        # print(prefixArr)
        # print(postfixArr)
        res = []
        for i in range(len(nums)):
            res.append(prefixArr[i] * postfixArr[i + 1])
        
        return res

obj = Solution()

def test_001():
    nums = [1,2,3,4]
    assert(obj.productExceptSelf(nums)) == [24,12,8,6]

def test_002():
    nums = [-1,1,0,-3,3]
    assert(obj.productExceptSelf(nums)) == [0,0,9,0,0]
        