from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = -(2**32)

        containerSize = len(height)
        indexI = 0
        indexJ = containerSize - 1

        while indexI < indexJ:
            area = min(height[indexI], height[indexJ]) * (indexJ - indexI)
            maxArea = max(maxArea, area)
            print(f"area {area} maxArea {maxArea}")
            if height[indexI] < height[indexJ]:
                indexI += 1
            else:
                indexJ -= 1

        return maxArea


soln = Solution()
# height = [1,8,6,2,5,4,8,3,7]
# height = [1,10,10,2,2]
# height = [1,1]
height = [0, 1]
print(soln.maxArea(height))