from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        output = 0
        
        if left == right: return self.nums[left]

        for i in range(left, right + 1):
            output += self.nums[i]
        
        return output

        


# Example use cases
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))
print(obj.sumRange(0,5))