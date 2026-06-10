# leetcode 153

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

    	low, high = 0, len(nums) - 1

    	while low <= high:
    		mid = (low + high) // 2
    		if nums[low] <= nums[mid] <= nums[high]:
    			if low == high:
    				return nums[low]
    			# [1,2,3,4,5]
    			high = mid
    		elif nums[mid] >= nums[low]  and nums[mid] > nums[high]:
    			# [2,3,4,5,1] or [3,4,5,1,2]
    			low = mid + 1
    		elif nums[mid] <= nums[low] and nums[mid] < nums[high]:
    			# [4,5,1,2,3] or [5,1,2,3,4]
    			high = mid

    	return nums[low]


obj = Solution()

print(obj.findMin([3,4,5,1,2]))
print(obj.findMin([4,5,6,7,0,1,2]))
print(obj.findMin([11,13,15,17]))
print(obj.findMin([1]))
print(obj.findMin([2,1]))
print(obj.findMin([1,2]))

'''
	Approach divide and conquer
	Either we can implement merge sort
	Or we can simply search with binary search
	
	Pseudo algorithm
	```
	low = high = 0
	while low <= high:
		if nums[low] <= nums[mid] <= nums[high]:
			if low == high:
				return nums[low]
			high = mid
		else if nums[mid] >= nums[low] && nums[mid] < nums[high]:
			low = mid + 1
		else if nums[mid] <= nums[low] && nums[mid] < nums[high]:
			high = mid

	return nums[low]

	However, special test case needs to be checked such as [2,1]
	```

'''