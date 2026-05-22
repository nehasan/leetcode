from collections import defaultdict
from typing import List


class Solution:
    """
    Approach prefix sum
    - First calculate all two distinct numbers sums and add them to the dictionary in the following fasion
    [num1, num2, [i, j]] // so the value in third index is the position of those two numbers respectively
    for example the following dict is created
    sumDict = {-1: [[-1, 0, [0, 1]]], 0: [[-1, 1, [0, 2]], [1, -1, [1, 4]]], ....}
    - Now iterate over the nums again and calculate the diff, which is diff = 0 - n, where n is x suppose
    - Now find the diff in the sumDict and iterate over the list of sums and add them to the res list if 
    sorted [n, y z] is not already added to the list
    
    Gets TLE at test case 312/316
    """
    '''
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        sumDict = defaultdict(list)
        # hash the two nums sum
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                
                # print(f"i: {i}, j: {j}")
                sumDict[nums[i] + nums[j]] += [[nums[i], nums[j], [i, j]]]
        
        res = []
        print(sumDict)
        for i, n in enumerate(nums):
            diff = 0 - n # let's say n is x
            if diff in sumDict:
                sums = sumDict[diff]
                # print(f"n is {n}, diff is: {diff}, analyzing sums: {sums}, pos is : {i}")
                for y, z, pos in sums:
                    if i not in pos:
                        sortedList = [n, y, z]
                        sortedList.sort()
                        if sortedList not in res:
                            res.append(sortedList)
        
        
        return res
    '''
    
    '''
    Approach two pointers
    - Sort the input array that gives us the intuition for applying two pointers and solve it
    - Keep the first pointer i fixed which is x = nums[i], and set low to i + 1 and high to nums_len - 1
    - Move i forward if we find the same number that was processed just now
    - Now calculate the total sum of nums[i] + nums[low] + nums[high]
    - If total is 0 that means it is a solution and we put the numbers to the result set
    And move low pointer to the right and high pointer left keeping in mind that we don't wanna process the same
    numbers again. When low == high we stop the loop and go for another i increment
    - Else if the number is lower than 0 then move low pointer right
    - Else squeeze the high pointer to the left
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(0, len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            low = i + 1
            high = len(nums) - 1
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                
                if total == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    
                    low, high = low + 1, high - 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                
                elif total < 0:
                    low += 1
                else:
                    high -= 1
        
        
        return res
                
        


obj = Solution()

nums = [0,0,0]
print(obj.threeSum(nums))

def test_0001():
    nums = [-1,0,1,2,-1,-4]
    assert(obj.threeSum(nums)) == [[-1,-1,2], [-1,0,1]]

def test_0002():
    nums = [0,1,1]
    assert(obj.threeSum(nums)) == []

def test_0003():
    nums = [0,0,0]
    assert(obj.threeSum(nums)) == [[0,0,0]]            
            