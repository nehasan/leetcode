from collections import defaultdict

class Solution:
    def __init__(self):
        self.memo = defaultdict(int)
    
    def dpTopDown(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        if n in [1, 2]: return n

        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.memo[n]
    
    def dpBottomUp(self, n: int) -> int:
        if n in [1, 2]: return n

        for i in range(3, n + 1):
            self.memo[i] = self.memo[i-2] + self.memo[i-1]
        
        return self.memo[n]

    def climbStairs(self, n: int) -> int:
        self.memo[1] = 1
        self.memo[2] = 2
        # self.dpTopDown(n)
        self.dpBottomUp(n)

        # print(self.memo)
        return self.memo[n]