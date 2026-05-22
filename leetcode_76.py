from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def allAlphaInT(alphaMap: dict, tMap: dict):
            for k, v in tMap.items():
                # print(x)
                if alphaMap[k] < v:
                    return False
            
            return True
        
        if s == t: return s
        if len(s) < len(t): return ""
        
        alphaMap = defaultdict(int)
        tMap = defaultdict(int)
        minWindow = 10e9
        output = ''
        
        for x in t:
            alphaMap[x] += 0
            tMap[x] += 1
        
        # print(alphaMap)
        k = 0
        for j in range(0, len(s)):
            if s[j] in t:
                alphaMap[s[j]] += 1
                if allAlphaInT(alphaMap, tMap) == True:
                    if k == j:
                        minWindow = 1
                        output = s[k:j + 1]
                    for i in range(k, j + 1):
                        currWindow = (j - i) + 1
                        if currWindow < minWindow:
                            minWindow = currWindow
                            output = s[i:j + 1]
                            # print(f"currWindow: {currWindow} output: {output}")
                        
                        if s[i] in t:
                            alphaMap[s[i]] -= 1
                            k = i + 1
                            
                        if allAlphaInT(alphaMap, tMap) == False: break
        
        return output


sol = Solution()
# s = "ADOBECODEBANC"
# t = "ABC"
s = "bbaa"
t = "aba"
print(sol.minWindow(s, t))

def test_case_0001():
    s = "ADOBECODEBANC"
    t = "ABC"
    assert sol.minWindow(s, t) == "BANC"

def test_case_0002():
    s = "a"
    t = "a"
    assert sol.minWindow(s, t) == "a"

def test_case_0003():
    s = "a"
    t = "aa"
    assert sol.minWindow(s, t) == ""
    
def test_case_0004():
    s = "ab"
    t = "a"
    assert sol.minWindow(s, t) == "a"