# leetcode 56

from typing import List

class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		pass

		intervals.sort()

		merged = []
		merged.append(intervals[0])

		for interval in intervals[1:]:

			start = interval[0]
			end   = interval[1]

			if start <= merged[-1][1]:
				merged[-1][0] = min(merged[-1][0], start)
				merged[-1][1] = max(merged[-1][1], end)
			else:
				merged.append(interval)


		return merged


obj = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(obj.merge(intervals))

intervals = [[1,4],[4,5]]
print(obj.merge(intervals))

intervals = [[4,7],[1,4]]
print(obj.merge(intervals))