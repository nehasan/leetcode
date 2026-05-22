# leetcode 438

import copy
from typing import List
from collections import defaultdict

class Solution:
	'''
	Approach, sliding window same as leetcode 567, permutation in string
	'''
	def findAnagrams(self, s: str, p: str) -> List[int]:

		def pAllCovered(pDict: defaultdict):
			for k, v in pDict.items():
				if v > 0:
					return False
			return True

		pDict = defaultdict(int)

		for char in p:
			pDict[char] += 1


		res = []
		left, right = 0, 0

		while left < len(s) and right < len(s):
			if s[right] in pDict and (pDict[s[right]] - 1) >= 0:
				pDict[s[right]] -= 1

				if pAllCovered(pDict) == True:
					res.append(left)

				right += 1
			elif s[right] in pDict and (pDict[s[right]] - 1) < 0:
				while left < right:
					if s[left] in pDict:
						pDict[s[left]] += 1
					left += 1
					if pDict[s[right]] > 0:
						break
			else:
				right += 1
				while left < right:
					if s[left] in pDict:
						pDict[s[left]] += 1
					left += 1
				# right += 1

		return res


obj = Solution()

# s = "cbaebabacd"
# p = "abc"
# print(obj.findAnagrams(s, p))

# s = "abab"
# p = "ab"
# print(obj.findAnagrams(s, p))

s = "bbddcabb"
p = "abc"
print(obj.findAnagrams(s, p))

s = "bbddcabb"
p = "abcd"
print(obj.findAnagrams(s, p))

# s = "baa"
# p = "aa"
# print(obj.findAnagrams(s, p))
