# leetcode 424

from typing import List
from collections import defaultdict

class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		charFrequency = defaultdict(int)
		left, right, longestLength = 0, 0, 0
		mostFreqeunt = []

		while(right < len(s)):
			charFrequency[s[right]] += 1

			if (len(mostFreqeunt) == 0):
				mostFreqeunt.append(s[right])
				mostFreqeunt.append(1)
			else:
				if (charFrequency.get(s[right]) >= mostFreqeunt[1]):
					mostFreqeunt[0] = s[right]
					mostFreqeunt[1] = charFrequency.get(s[right])

			# print(f"current charFrequency {charFrequency}")
			currWinLen = (right - left) + 1
			if (currWinLen - mostFreqeunt[1]) <= k:
				longestLength = max(longestLength, currWinLen)
			else:
				while True:
					maxLen = 0
					charFrequency[s[left]] -= 1

					# update the mostFrequent data
					for key, value in charFrequency.items():
						print(f"{key}, {value}")
						if value >= maxLen:
							mostFreqeunt[0] = key
							mostFreqeunt[1] = value
							maxLen = value

					left += 1
					currWinLen = (right - left) + 1
					# print(f"currWinLen {currWinLen} mostFreqeunt[1] {mostFreqeunt[1]}")
					if (currWinLen - mostFreqeunt[1]) <= k: break

			right += 1

		return longestLength


obj = Solution()

print(obj.characterReplacement("ABAB", 2)) # should output 4
print(obj.characterReplacement("AABABBA", 1)) # should output 4