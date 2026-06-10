from typing import List

class Solution:
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = []
        res.append(intervals[0])
        for interval in intervals[1:]:
            prevStart = res[-1][0]
            prevEnd = res[-1][1]

            currStart = interval[0]
            currEnd = interval[1]

            if currStart < prevEnd:
                res[-1][0] = min(prevStart, currStart)
                res[-1][1] = max(prevEnd, currEnd)
            else:
                res.append(interval)
        
        return res
    '''

    '''
    Approach: Sorting plus greedy algorithm
    Just sort the intervals and when we see an overlap currStart < prevEnd
    Then we choose min of both starts
    And min of both ends
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = []
        minRemoved = 0
        res.append(intervals[0])
        for interval in intervals[1:]:
            prevStart = res[-1][0]
            prevEnd = res[-1][1]

            currStart = interval[0]
            currEnd = interval[1]

            if currStart < prevEnd:
                res[-1][0] = min(prevStart, currStart)
                res[-1][1] = min(prevEnd, currEnd)
                minRemoved += 1
            else:
                res.append(interval)
        
        return minRemoved
    

obj = Solution()

def test_case_0001():
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    assert(obj.eraseOverlapIntervals(intervals)) == 1

def test_case_0002():
    intervals = [[1,2],[1,2],[1,2]]
    assert(obj.eraseOverlapIntervals(intervals)) == 2

def test_case_0003():
    intervals = [[1,2],[2,4]]
    assert(obj.eraseOverlapIntervals(intervals)) == 0

def test_case_0004():
    intervals = [[-73,-26],[-65,-11],[-62,-49]]
    assert(obj.eraseOverlapIntervals(intervals)) == 2

def test_case_0005():
    intervals = [[1,100],[11,22],[1,11],[2,12]]
    assert(obj.eraseOverlapIntervals(intervals)) == 2

def test_case_0005():
    intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
    assert(obj.eraseOverlapIntervals(intervals)) == 7