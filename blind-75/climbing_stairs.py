from collections import defaultdict

class Solution:
  def climbStairs(self, n: int) -> int:
    
    dp = defaultdict(int)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    
    if n == 1 or n == 2:
      return n
    
    for i in range(3, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2]
    
    
    return dp[n]
    
    

obj = Solution()

def test_001():
  n = 2
  assert(obj.climbStairs(n)) == 2

def test_002():
  n = 3
  assert(obj.climbStairs(n)) == 3

def test_003():
  n = 4
  assert(obj.climbStairs(n)) == 5