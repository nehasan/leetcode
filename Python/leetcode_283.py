from typing import List
from collections import deque


class Solution:
    # def moveZeroes(self, nums: List) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     prev = nums[0]

    #     for i in range(1, len(nums)):
    #         # print(i)
    #         if prev == 0 and nums[i] != 0:
    #             nums[i - 1] = nums[i]
    #             nums[i] = 0
    #         elif prev == 0 and nums[i] == 0:
    #             j = i
    #             while j < len(nums):
    #                 if nums[j] != 0:
    #                     nums[i - 1] = nums[j]
    #                     nums[j] = 0
    #                     break
    #                 j += 1
    #         prev = nums[i]
    #         # print(nums)

        
    #     # print(nums)
    #     return nums

    def moveZeroes(self, nums: List) -> None:
        q = deque()
        for i in range(len(nums)):
            if nums[i] == 0:
                q.append(i)
            else:
                if len(q) > 0:
                    insertIndex = q.popleft()
                    nums[insertIndex] = nums[i]
                    nums[i] = 0
                    q.append(i)

        # print(nums)
        return nums


soln = Solution()
# nums = [0,1,0,3,12]
# nums = [0]
# nums = [0, 1]
nums = [0,0,1]
print(soln.moveZeroes(nums))
