'''
https://leetcode.com/problems/palindromic-substrings/
O(n^2 * n) solution: Its not an efficient one but still works
For every single char, set l = r = i, that means pointing the same char
From that point expand to left and right to check if the left or right value same and increase the substring sum including s[l]
Second, for every two consecutive char, one odd and another even index, set l = i, r = i + 1
From that point expand to left and right to check if the left or right value same and increase the substring sum including s[l] and s[l + 1]
During expanding if s[l] != s[r] break search iteration immediately
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        totalSubString = 0
        def expandAndCheckPalindrome(odd: bool) -> None:
            subStringCount = 0
            for i in range(len(s)):
                leftPointer = i
                rightPointer = i if odd else i + 1

                lastIndex = len(s) - 1
                while True:
                    if leftPointer < 0 or rightPointer > lastIndex:
                        break
                    # If any two chars from left or right is not same break
                    if s[leftPointer] != s[rightPointer]:
                        break
                    if s[leftPointer] == s[rightPointer]:
                        subStringCount += 1
                    
                    leftPointer -= 1
                    rightPointer += 1
            
            return subStringCount
        
        # Check palindrome starting from odd index
        # Means if string is aaa then l and r will always start at l = r
        totalSubString =  expandAndCheckPalindrome(True)
        # Check palindrome starting from odd + even index
        # Means if string is aaa then l and r will always start at l = i r = i + 1
        totalSubString += expandAndCheckPalindrome(False)

        return totalSubString


soln = Solution()
s = 'abc' # 3
s = 'aaa' # 6
s = 'aaab' # 7
print(soln.countSubstrings(s))