from typing import List

class Solution:
    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     res = 0
    #     intervals.sort()
    #     # print(intervals)
    #     for i in range(len(intervals) - 1):
    #         if intervals[i][1] > intervals[i + 1][0]:
    #             res += 1
    #             if intervals[i][1] > intervals[i + 1][1]:
    #                 intervals[i] = None
    #             else:
    #                 intervals[i + 1][0] = intervals[i][0]
    #                 intervals[i + 1][1] = intervals[i][1]
    #                 intervals[i] = None
                
        
    #     # print(intervals)
    #     return res

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prevInterval = intervals[0]

        print(intervals)
        index = 0
        for interval in intervals[1:]:
            start = interval[0]
            end   = interval[1]
            if start < prevInterval[1]:
                res += 1
                if end > prevInterval[1]:
                    interval[0] = prevInterval[0]
                    interval[1] = prevInterval[1]
                    intervals[index] = None
                else:
                    intervals[index] = None
                    
            prevInterval = interval
            index += 1

        print(intervals)
        return res



soln = Solution()
# intervals = [[1,2], [2, 3], [3, 4], [1, 3]]
# intervals = [[1,2],[1,2],[1,2]]
# intervals = [[1,2],[2,3]]
# intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
print(soln.eraseOverlapIntervals(intervals))