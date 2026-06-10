# leetcode 33

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
        	mid = (low + high) // 2
 
        	if target == nums[mid]:
        		return mid
        	elif nums[low] <= nums[mid] <= nums[high]:
        		# [1,2,3,4,5]
        		if low == high:
        			if nums[low] == target:
        				return low
        			return -1
        		elif target < nums[mid]:
        			high = mid - 1
        		else:
        			low = mid + 1
        	elif nums[mid] <= nums[low] and nums[mid] < nums[high]:
        		# [4,5,1,2,3] or [5,1,2,3,4]
        		if target > nums[mid] and target <= nums[high]:
        			low = mid + 1
        		else:
        			high = mid - 1
        	elif nums[mid] >= nums[low] and nums[mid] > nums[high]:
        		# [2,3,4,5,1] or [3,4,5,1,2]
        		if target < nums[mid] and target >= nums[low]:
        			high = mid - 1
        		else:
        			low = mid + 1

        return -1


# obj = Solution()

# print(obj.search([4,5,6,7,0,1,2], 0))    #  4
# print(obj.search([4,5,6,7,0,1,2], 3))    # -1
# print(obj.search([1], 0))                # -1
# print(obj.search([5,1,3], 5))            #  0
# print(obj.search([5,1,3], 2))  		     # -1
# print(obj.search([5,1,3], 3))  		     #  2

"""
	Approach : Modified Binary Search
	This problem can be generalized based on the following input array
	[1,2,3,4,5]
	- We simply return mid if target == nums[mid]
	- If the array is not rotated at all or rotated n times then the array would be same 
	as before such as [1,2,3,4,5]. Now in this case if nums[low] <= nums[mid] <= nums[high]
	Now check if low == high then if nums[low] == nums[high] then return low
	Else we do the normal binary search procedure
	- Else if nums[mid] <= nums[low] && nums[mid] < nums[high], means [4,5,1,2,3] or [5,1,2,3,4],
	then we check if the num falls under second sequence means target > nums[mid] && target <= nums[high]
	then set low = mid + 1 else high = mid - 1
	- Else if nums[mid] >= nums[low] && nums[mid] > nums[high] means [2,3,4,5,1] or [3,4,5,1,2],
	then check if that falls under the first pure sequence target < nums[mid] && target >= nums[low]
	then set high = mid - 1 else low = mid + 1
"""
