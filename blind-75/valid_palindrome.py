import re
from typing import List

class Solution:
  def isPalindrome(self, s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    s = s.lower()
    
    if s == "":
      return True
    
    sLen = len(s)
    i, j = 0, sLen - 1
    
    while i < j:
      if s[i] != s[j]:
        return False
      
      i += 1
      j -=1
    
    return True


obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))

def test__001():
  s = "A man, a plan, a canal: Panama"
  assert(obj.isPalindrome(s)) == True

def test__002():
  s = "race a car"
  assert(obj.isPalindrome(s)) == False

def test__003():
  s = ". /"
  assert(obj.isPalindrome(s)) == True