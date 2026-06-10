from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prevInterval = intervals[0]

        index = 0
        for interval in intervals[1:]:
            start = interval[0]
            end   = interval[1]
            prevStart = prevInterval[0]
            prevEnd = prevInterval[1]

            if start <= prevEnd:
                if end > prevEnd:
                    interval[0] = prevStart
                else:
                    interval[0] = prevStart
                    interval[1] = prevEnd
                intervals[index] = None

            prevInterval = interval
            index += 1
        
        res = []
        for interval in intervals:
            if interval is not None:
                res.append(interval)
        
        return res


soln = Solution()
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[4,7],[1,4]]
intervals = [[1,10]]
print(soln.merge(intervals))