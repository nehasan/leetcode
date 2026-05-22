from typing import List


'''
Approach: Two pointer algorithm, where expand right pointer till we find that the frefix sum is greater than
the target. Once the prefix sum is greater then we shrink left pointer closer to right to reduce the prefix sum
until it gets to less than the target. While shrinking we calculate the possible min length ((j - i) + 1)
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] >= target: return 1
        if len(nums) == 1 and nums[0] < target: return 0
        
        minLength = 10e9
        
        i, j = 0, 0
        currSum = nums[i]
        
        while True:
            if currSum < target:
                j += 1
                currSum += nums[j]
            else:
                while currSum >= target and i <= j:
                    minLength = min(minLength, (j - i) + 1)
                    currSum -= nums[i]
                    i += 1
            if j == (len(nums) - 1) and currSum < target: break
        
        return minLength if minLength < 10e9 else 0
    
    
sol = Solution()
target = 7
nums = [2,3,1,2,4,3] # output 2
target = 4
nums = [1, 4, 4] # output 1
target = 11
nums = [1,1,1,1,1,1,1,1]
target = 7
nums = [5]
print(sol.minSubArrayLen(target, nums))