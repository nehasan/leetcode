from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        containerLen = len(height)
        
        i, j = 0, containerLen - 1
        maxArea = 0
        
        while i < j:
            currArea = (j - i) * min(height[i], height[j])
            maxArea = max(maxArea, currArea)
            
            if height[i] < height[j]: i += 1
            elif height[i] > height[j]: j -= 1
            else: 
                i += 1
                j -= 1
        
        return maxArea


sol = Solution()
height = [1,8,6,2,5,4,8,3,7] # output 49
height = [1, 1] # output 1
print(sol.maxArea(height))
        