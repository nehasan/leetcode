# leetcode 139

from typing import List

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:

		'''
		Wrong solution, solved in that way that if any word in the dictionary
		can be found in the original s
		suppose s = leetcode, now word_dict leetcode can be found in s as well as code
		'''
		'''
		alphaIndicesDict = defaultdict(list)
		
		# mark each alphabet's index of the word
		for index, sChar in enumerate(s):
			alphaIndicesDict[sChar] += [index]

		print(alphaIndicesDict)

		for word in wordDict:
			wordQ = deque()
			wordSet = set()
			wordSet.add(word)
			initialIndices = alphaIndicesDict[word[0]]

			for initIndex in initialIndices:
				print(f"checking index in s at: {initIndex}")
				wordQ = deque(list(word))

				for i in range(len(word)):
					if initIndex < len(s):
						if s[initIndex] != wordQ.popleft():
							break
						initIndex += 1

				if len(wordQ) == 0:
					wordSet.remove(word)

			if word in wordSet:
				return False

		return True
	'''

		pass

		left, right = 0, 0
		dictionary = set()

		for word in wordDict:
			dictionary.add(word)

		while left < len(s) and right < len(s):
			if left == right:
				if s[left] in dictionary:
					left += 1
			else:
				if s[left:right + 1] in dictionary:
					left = right + 1

			right += 1

		

		return True

obj = Solution()

# s = "leetcodel"
# wordDict = ["leet", "code"]
# print(obj.wordBreak(s, wordDict))

# s = "applepenapple"
# wordDict = ["apple","pen"]
# print(obj.wordBreak(s, wordDict))


# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# print(obj.wordBreak(s, wordDict))
s = "bb"
wordDict = ["a","b","bbb","bbbb"]
print(obj.wordBreak(s, wordDict))