from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        
        if left == right: return self.nums[left]
        
        for i in range(left, right + 1):
            sum += self.nums[i]
        
        return sum
        


# Example use cases

obj = NumArray([1, 3, 5])
print(obj.sumRange(0,2))
obj.update(1, 2)
print(obj.sumRange(0,2))