# leetcode 295

from typing import List
from heapq import heappush, heappop
from collections import defaultdict

class MedianFinder:
	def __init__(self):
		self.minHeap = [] # will be used as max heap (-4,-2,-1)
		self.maxHeap = [] # will be used as min heap (4, 5, 6)
		self.lenMinHeap = 0
		self.lenMaxHeap = 0


	def addNum(self, num: int) -> None:
		heappush(self.minHeap, (-1 * num))
		self.lenMinHeap += 1

		# make sure min heap always gets the min value than max heap
		if (self.lenMinHeap > 0 and self.lenMaxHeap > 0) \
					and ((-1 * self.minHeap[0]) > self.maxHeap[0]):
			val = heappop(self.minHeap)
			heappush(self.maxHeap, -1 * val)
			self.lenMinHeap -= 1
			self.lenMaxHeap += 1

		# make sure length diff ~1 otherwise transfer to max heap
		if (self.lenMinHeap > self.lenMaxHeap) and (self.lenMinHeap - self.lenMaxHeap) > 1:
			val = heappop(self.minHeap)
			heappush(self.maxHeap, -1 * val)
			self.lenMinHeap -= 1
			self.lenMaxHeap += 1

		# make sure length diff ~1 otherwise transfer to min heap
		if (self.lenMinHeap < self.lenMaxHeap) and (self.lenMaxHeap - self.lenMinHeap) > 1:
			val = heappop(self.maxHeap)
			heappush(self.minHeap, -1 * val)
			self.lenMinHeap += 1
			self.lenMaxHeap -= 1

	def findMedian(self) -> float:
		if self.lenMinHeap == self.lenMaxHeap:
			return ((-1 * self.minHeap[0]) + self.maxHeap[0]) / 2.0
		elif self.lenMinHeap > self.lenMaxHeap:
			return float(-1 * self.minHeap[0])
		else:
			return float(self.maxHeap[0])


obj = MedianFinder()

ops = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# values = [[], [1], [2], [], [3], []]
values = [[], [3], [2], [], [1], []] # passed
# values = [[], [2], [1], [], [3], []] # passed
res = []

for i, op in enumerate(ops):
	if op == "addNum":
		obj.addNum(values[i][0])
		res.append(None)
	elif op == "findMedian":
		res.append(obj.findMedian())

print(res)
