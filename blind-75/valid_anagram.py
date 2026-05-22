from typing import List, Optional
from collections import defaultdict

class Solution:
  '''
  # Approach using dictionary and mapping/counting the characters
  def isAnagram(self, s: str, t: str) -> bool:
    
    if len(s) != len(t):
      return False
      
    dictS = defaultdict(int)
    for char in s:
      dictS[char] += 1
    
    
    for char in t:
      if char not in dictS or dictS[char] == 0:
        return False
      
      dictS[char] -= 1
    
    return True
  '''
  
  '''
  # Approach using bultin sort function
  # Slower than the previous one
  '''
  def isAnagram(self, s: str, t: str) -> bool:
    
    if len(s) != len(t):
      return False
      
    sortedS = sorted(s, key=lambda x: x)
    sortedT = sorted(t, key=lambda x: x)
    
    return True if sortedS == sortedT else False

obj = Solution()

def test__001():
  s = "anagram"
  t = "nagaram"
  assert(obj.isAnagram(s, t)) == True


def test__002():
  s = "rat"
  t = "car"
  assert(obj.isAnagram(s, t)) == False


def test__003():
  s = "carr"
  t = "car"
  assert(obj.isAnagram(s, t)) == False