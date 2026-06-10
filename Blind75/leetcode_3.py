class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 2 and s[0] != s[1]:
            return 2
        if len(s) == 2 and s[0] == s[1]:
            return 1
        
        lPtr = 0
        rPtr = 1
        _set = set()
        maxLength = 1

        sLength = len(s)
        _set.add(s[0])
        while lPtr < sLength - 1 and rPtr < sLength:
            if s[rPtr] not in _set:
                _set.add(s[rPtr])
                maxLength = max(maxLength, (rPtr - lPtr) + 1)
            else:
                while s[lPtr] != s[rPtr]:
                    if s[lPtr] in _set:
                        _set.remove(s[lPtr])
                    
                    lPtr += 1
                lPtr += 1
            
            rPtr += 1

        return maxLength


obj = Solution()
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
s = "aab"
print(obj.lengthOfLongestSubstring(s))