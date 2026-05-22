# leetcode 981

from typing import List
from collections import defaultdict

class TimeMap:

	def __init__(self):
		self.dictionary: [str, list] = defaultdict(list)


	def set(self, key: str, value: str, timestamp: int) -> None:
		if key in self.dictionary:
			self.dictionary[key].append((timestamp, value))
		else:
			self.dictionary[key] = [(timestamp, value)]


	def get(self, key: str, timestamp: int) -> str:
		values = self.dictionary.get(key, [])
			
		low, high = 0, len(values) - 1
		res = ""
		
		while low <= high:
			mid = (low + high) // 2

			if values[mid][0] <= timestamp:
				res = values[mid][1]
				low = mid + 1
			elif values[mid][0] <= timestamp:
				low = mid + 1
			else:
				high = mid - 1

		return res




obj = TimeMap()

# ops = ["TimeMap", "set", "get", "get", "set", "get", "get"]
# values = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

ops = ["TimeMap","set","set","get","get","get","get","get"]
values = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

res = []
for i, op in enumerate(ops):
	if op == "set":
		key, value, timestamp = values[i][0], values[i][1], values[i][2]
		obj.set(key, value, timestamp)
		res.append(None)
	elif op == "get":
		key, timestamp = values[i][0], values[i][1]
		ans = obj.get(key, timestamp)
		res.append(ans)


print(res)