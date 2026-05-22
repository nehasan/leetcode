from typing import List

class Solution:
  
  '''
  Approach, two iteration, first one just inserts the new interval into the right position
  The second iteration fix the overlaps
  '''
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    inserted = False
    insertedArr = [[0,0]]
    
    # loop to insert the new interval into its desired position
    for interval in intervals:
      prevStart = insertedArr[-1][0]
      prevEnd   = insertedArr[-1][1]
      
      start = interval[0]
      end = interval[1]
      
      # check if interval can be inserted
      if not inserted and newInterval[0] >= prevStart and newInterval[0] <= start:
        insertedArr.append(newInterval)
        inserted = True
      
      insertedArr.append(interval)
    
    if not inserted:
      insertedArr.append(newInterval)
    
    print(f"insertedArr {insertedArr}")
    
    #loop to fix the overlaps
    mergedArr = []
    mergedArr.append(insertedArr[1])
    
    for interval in insertedArr[2:]:
      start = interval[0]
      end = interval[1]
      
      prevStart = mergedArr[-1][0]
      prevEnd = mergedArr[-1][1]
      
      if start <= prevEnd:
        mergedArr[-1] = [min(prevStart, start), max(prevEnd, end)]
      else:
        mergedArr.append(interval)
        
    return mergedArr


obj = Solution()
intervals = [[2,3], [5,7]]
newInterval = [0,6]
print(obj.insert(intervals, newInterval))

def test_001():
  intervals = [[1,3], [6,9]]
  newInterval = [2,5]
  assert(obj.insert(intervals, newInterval)) == [[1,5], [6,9]]

def test_002():
  intervals = [[1,2], [3,5], [6,7], [8, 10], [12,16]]
  newInterval = [4,8]
  assert(obj.insert(intervals, newInterval)) == [[1,2], [3,10], [12,16]]

def test_003():
  intervals = []
  newInterval = [5,7]
  assert(obj.insert(intervals, newInterval)) == [[5,7]]

def test_004():
  intervals = [[1,5]]
  newInterval = [2,7]
  assert(obj.insert(intervals, newInterval)) == [[1,7]]

def test_004():
  intervals = [[2,3], [5,7]]
  newInterval = [0,6]
  assert(obj.insert(intervals, newInterval)) == [[1,7]]
