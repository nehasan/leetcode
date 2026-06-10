from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        map = dict()
        for n in nums:
            if map.get(n) is None:
                map[n] = 1
            else:
                map[n] += 1

        colors = [k for k in map.keys()]
        colors.sort()

        index = 0
        for c in colors:
            for i in range(map[c]):
                nums[index] = c
                index += 1
        
        print(nums)
        

soln = Solution()
# nums = [2,0,2,1,1,0]
# nums = [2,0,1]
nums = [1, 0, 0, 0]
soln.sortColors(nums)
