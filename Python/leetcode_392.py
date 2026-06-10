'''
Algorithm:
Map the letter indices of t into a hashmap (dictionary in python)
Iterate over s and check if the fetched index from the map is valid as:
1. map[c] is not None and map[c] index list is empty
2. map[c] contains any bigger index than the current index
If none of the above meets return false, else check through the whole s and update current index and
pop the index that was fetched
'''

from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0;
        map = dict()
        for c in t:
            if map.get(c) == None:
                map[c] = deque()
                map[c].append(i)
            else:
                map[c].append(i)
        
            i += 1

        currIndex = -1

        for c in s:
            indices = map.get(c)
            if indices == None or len(indices) == 0:
                return False
            
            # Check if is there any index bigger than the current index
            filtered = [x for x in indices if x > currIndex]
            if len(filtered) == 0:
                return False
            
            currIndex = filtered[0]
        
        return True

soln = Solution()
# s = 'abc'
# s = 'axc'
# t = 'ahbgdc'
s = 'ab'
t = 'baab'
print(soln.isSubsequence(s, t))
