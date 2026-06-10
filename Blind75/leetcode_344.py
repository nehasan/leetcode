'''
https://leetcode.com/problems/reverse-string/description/

'''

class Solution:
    def reverseString(self, s: list) -> list:
        sLen = len(s)
        i = 0
        j = sLen - 1

        while i < sLen / 2:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j -= 1

        return s
    

soln = Solution()
s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]
s = ["H", "h"]
s = ["H", "e", "l"]
print("".join(soln.reverseString(s)))