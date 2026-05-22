from random import randrange

class Solution:
  def __init__(self):
    self.versions = []
  
  
  def populateVersions(self, n: int = 10, firstBad: int = 7):
    # rand = random.randrange(n)
    
    self.versions = [True] * n
    for i in range(firstBad):
      self.versions[i] = False
    
    print(self.versions)
  
  
  def firstBadVersion(self, n: int) -> int:
    
    def isBadVersion(n: int) -> bool:
      return self.versions[n]
    
    
    def findFirstBadVersion(low: int, high: int) -> int:
      mid = int((low + high) / 2)
      
      if low == high:
        return low
      
      isMidBad = isBadVersion(mid)
      
      if isMidBad:
        return findFirstBadVersion(low, mid)
      else:
        return findFirstBadVersion(mid + 1, high)
    
    return findFirstBadVersion(1, n)


obj = Solution()

def test_0001():
  obj.populateVersions(n=10, firstBad=3)
  assert(obj.firstBadVersion(10)) == 3

def test_0002():
  obj.populateVersions(10, 7)
  assert(obj.firstBadVersion(10)) == 7

def test_0003():
  obj.populateVersions(10, 1)
  assert(obj.firstBadVersion(10)) == 1