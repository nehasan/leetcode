# leetcode 704. Binary Search

from collections import defaultdict
from typing import List, Optional

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    
    def binarySearch(nums: List[int], target: int, low: int, high: int) -> int:
      # print(f"low: {low}, high: {high}")
      if low > high:
        return -1
      
      mid = int((low + high) / 2)
      # print(f"low: {low}, high: {high}, mid: {mid}")
      
      if low == high:
        if nums[low] == target:
          return low
        else:
          return -1
      if nums[mid] == target:
        return mid
      
      if target < nums[mid]:
        return binarySearch(nums, target, low, mid)
      else:
        return binarySearch(nums, target, mid + 1, high)
    
    if len(nums) == 0:
      return -1
    if len(nums) == 1:
      return 0 if nums[0] == target else -1 
    
    return binarySearch(nums, target, 0, len(nums) - 1)
    

obj = Solution()

# nums = [-1,0,3,5,9,12]
# target = 9
# nums = [1,2]
# target = 2
# print(obj.search(nums, target))

def test_001():
  nums = [-1,0,3,5,9,12]
  target = 9
  assert(obj.search(nums, target)) == 4

def test_002():
  nums = [-1,0,3,5,9,12]
  target = 2
  assert(obj.search(nums, target)) == -1
  
def test_003():
  nums = [1]
  target = 1
  assert(obj.search(nums, target)) == 0

def test_004():
  nums = [1,2]
  target = 1
  assert(obj.search(nums, target)) == 0

def test_005():
  nums = [1,2]
  target = 2
  assert(obj.search(nums, target)) == 1

def test_006():
  nums = []
  target = 1
  assert(obj.search(nums, target)) == -1