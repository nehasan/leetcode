from typing import List

class Solution:
    '''
    Window sliding approach does not solve with negative numbers:
    For example: [3, 4, 7, -2, 2, 1, 4, 2] k = 7, output should be 6
    [3, 4], [7], [7, -2, 2], [-2, 2, 1, 4], [2, 1, 4], [1,4, 2]
    '''
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     if len(nums) == 1 and k == nums[0]: return 1
    #     if len(nums) == 1 and k != nums[0]: return 0

    #     totalSubArray = 0
    #     i, j, l = 0, 0, 0
        
    #     currSum = 0
    #     for j in range(0, len(nums)):
    #         currSum += nums[j]
    #         if currSum == k:
    #             totalSubArray += 1
    #         if currSum > k:
    #             for i in range(l, j):
    #                 currSum -= nums[i]
    #                 l = i + 1
    #                 if currSum == k: totalSubArray += 1
    #                 if currSum < k: break
        
        
    #     return totalSubArray
    
    '''
    Approach: Prefix sum, where currSum should be in the hash and update the count of the diff (currSum - k) in the hash to
    calculate numbers of ways (subarray) can be formed to equal target k
    '''
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        currSum = 0
        prefixSums = {}
        prefixSums[currSum] = 1
        
        for n in nums:
            currSum += n
            diff = currSum - k
            
            output += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
            print(f"currSum: {currSum}, diff: {diff}")
            print(f"output: {output} prefixSums: {prefixSums}")
        
        return output
            


sol = Solution()
# nums = [1, 1, 1]
# k = 2
# nums = [1, 2, 3]
# k = 3
# nums = [3, 4, 7, -2, 2, 1, 4, 2]
# k = 7
# print(sol.subarraySum(nums, k))

def test_case_0001():
    nums = [1, 1, 1]
    k = 2
    assert sol.subarraySum(nums, k) == 2

def test_case_0002():
    nums = [1, 2, 3]
    k = 3
    assert sol.subarraySum(nums, k) == 2
    
def test_case_0003():
    nums = [3, 4, 7, -2, 2, 1, 4, 2]
    k = 7
    assert sol.subarraySum(nums, k) == 6