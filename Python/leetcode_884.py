from typing import List
from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        _dict = defaultdict(int)

        words1 = s1.split(" ")
        words2 = s2.split(" ")
        for w in words1 + words2:
            _dict[w] += 1
        
        output = []
        for k,v in _dict.items():
            if v == 1:
                output.append(k)
        
        return output

# Test cases
sol = Solution()
print(sol.uncommonFromSentences("this apple is sweet", "this apple is sour")) # ["sweet","sour"]
print(sol.uncommonFromSentences("apple apple", "banana")) # ["banana"]
print(sol.uncommonFromSentences("s z z z s", "s z ejt")) # ["ejt"]