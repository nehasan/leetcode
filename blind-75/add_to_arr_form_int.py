from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
      
      def arrToNum(arr: List[int]) -> int:
        arr = arr[::-1]
        num = 0
        rank = 0
        for n in arr:
          num += (pow(10, rank) * n)
          rank += 1
          
        return num
      
      def numToArray(number: int) -> List[int]:
        res = []
        while number > 0:
          rem = number % 10
          res.append(rem)
          number = int(number / 10)
        
        return res[::-1]
      
      sum = list()
      carry = 0
      kArr = numToArray(k)
      
      while len(num) > 0 or len(kArr) > 0:
        x = num.pop() if len(num) > 0 else 0
        y = kArr.pop() if len(kArr) > 0 else 0
        currSum = x + y + carry 
        if currSum > 9:
          sum.append(currSum % 10)
          carry = int(currSum / 10)
        else:
          sum.append(currSum)
          carry = 0

      if carry > 0:
        sum.append(carry)
      
      return sum[::-1]
        

obj = Solution()

def test_000():
  num = [0]
  k = 23
  assert(obj.addToArrayForm(num, k)) == [2,3]

def test_001():
  num = [1,2,0,0]
  k = 34
  assert(obj.addToArrayForm(num, k)) == [1,2,3,4]

def test_002():
  num = [2,7,4]
  k = 181
  assert(obj.addToArrayForm(num, k)) == [4,5,5]
  
def test_003():
  num = [2,1,5]
  k = 806
  assert(obj.addToArrayForm(num, k)) == [1,0,2,1]

def test_004():
  num = [1,2,6,3,0,7,1,7,1,9,7,5,6,6,4,4,0,0,6,3]
  k = 516
  assert(obj.addToArrayForm(num, k)) == [1, 2, 6, 3, 0, 7, 1, 7, 1, 9, 7, 5, 6, 6, 4, 4, 0, 5, 7, 9]