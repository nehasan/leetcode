from typing import List

class Solution:
    def binarySearch(self, beg: int, end: int, nums, target) -> int:
        mid = int((beg + end) / 2)

        print(f"beg: {beg}, end: {end}, mid: {mid}")
        if target == nums[mid]:
            return mid
        if beg == end:
            return beg + 1 if target > nums[beg] else beg
        elif target < nums[mid]:
            end = mid - 1
            end = end if end > 0 else 0
            return self.binarySearch(beg, end, nums, target)
        elif target > nums[mid]:
            beg = mid + 1
            beg = beg if beg < end else end
            return self.binarySearch(beg, end, nums, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)


soln = Solution()
# nums = [1,3,5,6]
# target = 5
# target = 2
# target = 7
# nums = [1,3]
# target = 4
# nums = [1]
# target = 2
nums = [3,5,7,9,10]
target = 8
print(soln.searchInsert(nums, target))