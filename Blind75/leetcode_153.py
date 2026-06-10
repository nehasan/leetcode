from typing import List

class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        while len(nums1) > 0 or len(nums2) > 0:
            if len(nums1) > 0 and len(nums2) > 0:
                if nums1[0] < nums2[0]:
                    res.append(nums1.pop(0))
                elif nums2[0] < nums1[0]:
                    res.append(nums2.pop(0))
                elif nums1[0] == nums2[0]:
                    res.append(nums1.pop(0))
                    res.append(nums2.pop(0))
            
            elif len(nums1) > 0: 
                res.append(nums1.pop(0))
            elif len(nums2) > 0:
                res.append(nums2.pop(0))
            
        return res
    
    def mergeSort(self, nums: List[int]) -> List[int]:
        containerSize = len(nums)
        if containerSize == 1:
            return nums
        mid = round(containerSize / 2)
        return self.merge(self.mergeSort(nums[0:mid]), self.mergeSort(nums[mid:containerSize]))

    def findMin(self, nums: List[int]) -> int:
        sortedNums = self.mergeSort(nums)

        return sortedNums[0]



obj = Solution()
nums = [4,5,6,7,0,1,2]
nums = [6,5,4,3,2,1,0]
nums = [0,1]
nums = [1,0]
print(obj.findMin(nums))