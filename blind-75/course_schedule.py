# leetcode 207

from typing import List
from collections import defaultdict

class Solution:

	def __init__(self):
		self.visiting = set()
		self.visited = set()

	def validateScheduling(self, course: int, graph: defaultdict) -> bool:
		if course in self.visited:
			return True

		if course in self.visiting:
			return False

		self.visiting.add(course)

		for preq_course in graph[course]:
			if self.validateScheduling(preq_course, graph) == False:
				return False

		self.visited.add(course)
		return True

	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		graph = defaultdict(list)
		courses = list()

		for course, preq_course in prerequisites:
			graph[course] += [preq_course]
			courses.append(course)


		for course in courses:
			self.visiting.clear()
			self.visited.clear()

			if self.validateScheduling(course, graph) == False:
				return False

		return True



obj = Solution()

def test_001():
	assert(obj.canFinish(2, [[1, 0]])) == True

def test_002():
	assert(obj.canFinish(2, [[1, 0], [0, 1]])) == False

def test_003():
	assert(obj.canFinish(2, [[1, 4], [2, 4], [3, 1], [3, 2]])) == True