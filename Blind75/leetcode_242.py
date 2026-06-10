class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphaMap = dict()
        for c in s:
            if alphaMap.get(c) is None:
                alphaMap[c] = 1
            else:
                alphaMap[c] += 1
        
        for c in t:
            if alphaMap.get(c) is None:
                return False
            elif alphaMap[c] <= 0:
                return False
            else:
                alphaMap[c] -= 1
        
        return True

soln = Solution()
# s = 'anagram'
# t = 'nagaram'
s = 'rat'
t = 'cat'
print(soln.isAnagram(s, t))