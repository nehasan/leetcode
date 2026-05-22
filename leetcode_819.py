import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dictionary = {}
        
        _paragraph = re.sub(r"[^a-zA-Z]", " ", paragraph)
        print(_paragraph)
        _paragraph = _paragraph.split(" ")
        print(_paragraph)
        
        for word in _paragraph:    
            _word = word.lower()
            
            if _word != '' and _word not in banned:
                if _word in dictionary:
                    dictionary[_word] += 1
                else:
                    dictionary[_word] = 1
        
        print(dictionary)
        maxNumber = 0
        res = None
        for k, v in dictionary.items():
            if v > maxNumber:
                res = k
                maxNumber = v
        
        return res
    

sol = Solution()
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# print(sol.mostCommonWord(paragraph, banned)) # Output "ball"

# paragraph = "a."
# banned = []
# print(sol.mostCommonWord(paragraph, banned)) # Output "a"

# paragraph = "a b.b"
# banned = []
# print(sol.mostCommonWord(paragraph, banned)) # Output "b"

paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]
print(sol.mostCommonWord(paragraph, banned)) # Output "b"