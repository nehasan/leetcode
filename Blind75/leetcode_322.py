import sys
from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.memo = defaultdict(int)
        self.memo[0] = 0
        self.coinsSorted: List[int] = []

    def coinChange(self, coins: List[int], amount: int) -> int:
        def dpTopDown(amount: int) -> int:
            if amount in self.memo: return self.memo[amount]

            minCoinCount = sys.maxsize
            for coin in self.coinsSorted:
                diff = amount - coin
                if diff < 0:
                    break

                minCoinCount = min(minCoinCount, 1 + dpTopDown(diff))
            
            self.memo[amount] = minCoinCount
            
            return self.memo[amount]
        
        def dpBottomUp(amount) -> int:
            minCoinCount = sys.maxsize
            currAmount = amount

            for i in range(1, amount):
                for coin in self.coinsSorted:
                    diff = amount - coin
                    currAmount = diff
                    if diff < 0 or currAmount < 0:
                        break
                    minCoinCount = min(minCoinCount, 1 + self.memo[diff])
                
                self.memo[currAmount] = minCoinCount

            return self.memo[amount]


        self.coinsSorted = coins.copy()
        self.coinsSorted.sort()

        res = dpTopDown(amount)
        print(self.memo)
        if res < sys.maxsize:
            return res
        return -1
    

obj = Solution()
# coins = [1, 2, 5]
# amount = 11
coins = [1, 2147483647]
amount = 2
print(obj.coinChange(coins, amount))