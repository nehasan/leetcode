from typing import List
from collections import defaultdict

class Solution:
	'''
	Approach using SET instead of hashmap for an sweet advantage
	- If it is a new character then insert into the set and calculate the max length so far
	- If the char is known to set then move left pointer towards right pointer and remove the s[left_pointer]
	until s[right_pointer] found
	'''
	def lengthOfLongestSubstring(self, s: str) -> int:
		
		charSet = set()
		leftPtr = 0
		rightPtr = 0
		maxLength = 0

		while leftPtr < (len(s)) and rightPtr < (len(s)):
			char = s[rightPtr]

			if char not in charSet:
				charSet.add(char)
				maxLength = max(maxLength, (rightPtr - leftPtr) + 1)
			else:
				while s[leftPtr] != s[rightPtr]:
					if s[leftPtr] in charSet:
						charSet.remove(s[leftPtr])
					leftPtr += 1

				leftPtr += 1

			rightPtr += 1


		return maxLength


obj = Solution()
# s = "abcabcbb"
# print(obj.lengthOfLongestSubstring(s))

def test_001():
	s = "abcabcbb"
	assert(obj.lengthOfLongestSubstring(s)) == 3

def test_002():
	s = "bbbbbb"
	assert(obj.lengthOfLongestSubstring(s)) == 1

def test_003():
	s = "pwwkew"
	assert(obj.lengthOfLongestSubstring(s)) == 3

def test_004():
	s = "dvdf"
	assert(obj.lengthOfLongestSubstring(s)) == 3
