from typing import List
from collections import defaultdict

class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
    alphaDict = defaultdict(int)
    for char in magazine:
      alphaDict[char] += 1
    
    for char in ransomNote:
      if char not in alphaDict:
        return False
      
      if alphaDict[char] == 0:
        return False
      
      alphaDict[char] -= 1
    
    return True
    

obj = Solution()

def test_001():
  ransomNote = "a"
  magazine = "b"
  assert(obj.canConstruct(ransomNote, magazine)) == False

def test_002():
  ransomNote = "aa"
  magazine = "ab"
  assert(obj.canConstruct(ransomNote, magazine)) == False

def test_003():
  ransomNote = "aa"
  magazine = "aab"
  assert(obj.canConstruct(ransomNote, magazine)) == True