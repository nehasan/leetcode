'''
https://leetcode.com/problems/longest-palindromic-subsequence/description/
Same algorithm approach as leetcode 647. Palindromic substring
Starting from l = r = i, expand left and right and check if two chars are same, increase the count, including s[l]
Starting from l = i, r = i + 1 expand left and right and check if two chars are same, increase the count including s[l] and s[r]
'''


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        maxSubStringCount = 0
        def expandAndCheckPalindrome(odd: bool, globalMaxCount: int) -> int:
            localMaxCount = globalMaxCount
            for i in range(len(s)):
                leftPointer = i
                rightPointer = i if odd else i + 1
                lastIndex = len(s) - 1
                localStringCount = 0

                while True:
                    if leftPointer < 0 or rightPointer > lastIndex:
                        break
                    if s[leftPointer] != s[rightPointer]:
                        break
                    if s[leftPointer] == s[rightPointer]:
                        localStringCount += 1
                    
                    leftPointer -= 1
                    rightPointer += 1
                
                localMaxCount = max(localMaxCount, localStringCount)
            
            return localMaxCount
        
        maxSubStringCount = max(
            maxSubStringCount, 
            expandAndCheckPalindrome(True, maxSubStringCount)
        )

        maxSubStringCount = max(
            maxSubStringCount, 
            expandAndCheckPalindrome(False, maxSubStringCount)
        )

        return maxSubStringCount

soln = Solution()
s = "bbbab" # 4
print(soln.longestPalindromeSubseq(s))

        

