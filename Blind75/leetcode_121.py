from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 10001
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                maxProfit = max(maxProfit, (price - minPrice))
        
        return maxProfit


soln = Solution()
prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,2,1]
print(soln.maxProfit(prices))