from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = -(2**32)
        # print(maxProd)
        currProd = 1

        for n in nums:
            currProd = n if (currProd * n) == 0 else (currProd * n)
            maxProd = max(max(maxProd, currProd), n)
            print(f'currProd: {currProd}, maxProd: {maxProd}')
        
        return maxProd

soln = Solution()
# nums = [2,3,-2,4] # 6
# nums = [-2,0,-1]  # 0
# nums = [-2,3,-4]  # 24
# nums = [3,-1,4]   # 4
nums = [2,-5,-2,-4,3] # 24
print(soln.maxProduct(nums))