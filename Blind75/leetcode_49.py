from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = dict()
        for s in strs:
            sTemp = ''.join(sorted(s))
            if map.get(sTemp) is None:
                map[sTemp] = [s]
            else:
                map[sTemp].append(s)
        
        return [v for v in map.values()]


soln = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(soln.groupAnagrams(strs))