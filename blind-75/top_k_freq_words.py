# leetcode 692

from typing import List
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop

class Solution:
	def topKFrequent(self, words: List[str], k: int) -> List[str]:
		
		countDict = defaultdict(int)
		wordDict = defaultdict(deque)
		maxHeap = []

		for word in words:
			countDict[word] += 1

		for key, val in countDict.items():
			wordQ = None
			if val not in wordDict:
				heappush(maxHeap, (0 - val))
				wordQ = deque()
			else:
				wordQ = wordDict[val]

			wordQ.append(key)
			wordDict[val] = wordQ

		res = []
		while k > 0:
			count = heappop(maxHeap)
			wordQ = wordDict[(0 - count)]
			wordQ = deque(sorted(wordQ, key=lambda x: x))
			while len(wordQ) > 0 and k > 0:
				res.append(wordQ.popleft())
				k -= 1

		return res

obj = Solution()
# words = ["i","love","leetcode","i","love","coding"]
# k = 2
# print(obj.topKFrequent(words, k))

def test_001():
	words = ["i","love","leetcode","i","love","coding"]
	k = 2
	assert(obj.topKFrequent(words, k)) == ["i", "love"]

def test_002():
	words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
	k = 4
	assert(obj.topKFrequent(words, k)) == ["the", "is", "sunny", "day"]

def test_003():
	words = ["i","love","leetcode","i","love","coding"]
	k = 3
	assert(obj.topKFrequent(words, k)) == ["i", "love", "coding"]