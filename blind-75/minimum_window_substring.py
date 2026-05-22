# leetcode 76

import copy
from typing import List
from collections import defaultdict

class Solution:

	'''
	Approach sliding window
	Map the t string, suppose tDict = {"A": 1, "B": 1, "C": 1}
	Now initialize two pointers at 0 left = right = 0
	Increase right pointer and check if the character exists in the tDict and decrease them
	from the total count
	If all of them are <= 0 then it idicates that all characters and covered.
	At this point check the length of the window and take a snapshot of the window
	Now until left < right increase left pointer and any char exists in the map release them from the decrement
	That means in the dictionary it increases and the moment any character is > 0 that means
	all characters are not covered and break the loop and increase the right pointer untill all covered again
	Within the middle loop try to take a snapshot of the window if all the characters are covered
	Runtime complexity: O(s * t)
	Space complexity: O(s + t)
	'''
	def minWindow(self, s: str, t: str) -> str:

		def tAllCovered(tDict: defaultdict) -> bool:
			for k, v in tDict.items():
				if v > 0:
					return False

			return True

		tDict = defaultdict(int)

		for char in t:
			tDict[char] += 1

		left, right = 0, 0
		minLen = float('inf')
		res = ""

		while left < len(s) and right < len(s):
			if s[right] in tDict:
				tDict[s[right]] -= 1

				if tAllCovered(tDict) == True:
					tempMinLen = (right - left) + 1
					if tempMinLen < minLen:
						minLen = tempMinLen
						res = s[left:right + 1]

					while left < right:
						if s[left] in tDict:
							tDict[s[left]] += 1
						
						left += 1

						if tAllCovered(tDict) == True:
							tempMinLen = (right - left) + 1
							if tempMinLen < minLen:
								minLen = tempMinLen
								res = s[left:right + 1]
						else:
							break
			
			right += 1


		return res



obj = Solution()

s = "bdab"
t = "ab"
print(obj.minWindow(s, t))

s = "ADOBECODEBANC"
t = "ABC"
print(obj.minWindow(s, t))

s = "a"
t = "a"
print(obj.minWindow(s, t))

s = "a"
t = "aa"
print(obj.minWindow(s, t))