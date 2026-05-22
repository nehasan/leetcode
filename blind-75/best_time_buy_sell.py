from typing import List

'''
Approach: Iterate over the prices array and find the min price comapring with the curr price
Now find the max profit by maxProfit = max(maxProfit, (currPrice - minPrice))
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
         
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, (price - minPrice))
        
        return maxProfit


obj = Solution()

def test_0001():
    prices = [7,1,5,3,6,4]
    assert(obj.maxProfit(prices)) == 5

def test_0002():
    prices = [7,6,4,3,2,1]
    assert(obj.maxProfit(prices)) == 0

def test_0003():
    prices = [1,4,2]
    assert(obj.maxProfit(prices)) == 3

def test_0004():
    prices = [2,1,4]
    assert(obj.maxProfit(prices)) == 3

def test_0005():
    prices = [2,1,2,0,1]
    assert(obj.maxProfit(prices)) == 1

