from collections import defaultdict

class Solution:
  '''
  Approach: hashing and counting alphabets. The idea is a proper palindrome can be formulated
  using the following sets of characters
  - Multiple even numbered alpha
  - Present of 1 or more single alpha, for example s = "aa bb c" -> "abcba"
  - Now if the string is suppose "abcccccdd", the count will be 7 because we will take a total 4 out of 5 c(s)
  - In case of only one alphabet available then we return that count directly
  
  - Count the characters
  - Ff the count is odd then we take even of them and
  - If there are multiple single chars the we just add 1 to the total longest length
  Complexity: O(n)
  '''
  def longestPalindrome(self, s: str) -> int:
    
    alphaDict = defaultdict(int)
    
    for char in s:
      alphaDict[char] += 1
    
    
    # print(alphaDict)
    lenAlphaDict = len(alphaDict)
    singleAlpha = False
    longestToBe = 0
      
    for k, v in alphaDict.items():
      if v % 2 == 1:
        singleAlpha = True
        longestToBe += (v - 1)
      else:
        longestToBe += v
    
    
    longestToBe += 1 if singleAlpha else 0
    
    return longestToBe


obj = Solution()
s = "abccccdd"
print(obj.longestPalindrome(s))

def test_000():
  s = "abcccccdd"
  assert(obj.longestPalindrome(s)) == 7

def test_001():
  s = "abccccdd"
  assert(obj.longestPalindrome(s)) == 7

def test_002():
  s = "a"
  assert(obj.longestPalindrome(s)) == 1

def test_003():
  s = "abbccccdd"
  assert(obj.longestPalindrome(s)) == 9

def test_004():
  s = "abc"
  assert(obj.longestPalindrome(s)) == 1

def test_005():
  s = ""
  assert(obj.longestPalindrome(s)) == 0

def test_005():
  s = "aaaaa"
  assert(obj.longestPalindrome(s)) == 5
  
def test_005():
  s = "ababababa"
  assert(obj.longestPalindrome(s)) == 9