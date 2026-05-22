# leetcode 973

from typing import List
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop

class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

		distPointsDict = defaultdict(list)
		minHeap = []

		for i, [x, y] in enumerate(points):
			print(f"i {i} x: {x} y: {y}")
			xDistance = (0 - x) * (0 - x)
			yDistance = (0 - y) * (0 - y)

			distance = xDistance + yDistance

			distPointsDict[distance] += [i]
			heappush(minHeap, distance)

		index = k
		res = []
		while index > 0:
			minDistance = heappop(minHeap)
			pointsInDict = distPointsDict[minDistance]

			for pointIndex in pointsInDict:
				res.append(points[pointIndex])
				index -= 1
				if index == 0: break
			# while len(pointsInDict) > 0 and index > 0:
			# 	res.append(points[pointsInDict.popleft()])
			# 	index -= 1

		return res

obj = Solution()
points = [[1, 3], [-2, 2]]
k = 1
print(obj.kClosest(points, k)) # [[-2, 2]]

def test_case_001():
	points = [[1, 3], [-2, 2]]
	k = 1
	assert(obj.kClosest(points, k)) == [[-2, 2]]

def test_case_002():
	points = [[3, 3], [5, -1], [-2, 4]]
	k = 2
	assert(obj.kClosest(points, k)) == [[3, 3], [-2, 4]]


def test_case_003():
	points = [[0, 1], [1, 0]]
	k = 2
	assert(obj.kClosest(points, k)) == [[0, 1], [1, 0]]