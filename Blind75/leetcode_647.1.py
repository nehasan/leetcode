class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAndCheckPalindrome(initialPos: str, s: str) -> int:
            count = 0

            for index in range(len(s)):
                left = index
                right = left if initialPos == "odd" else left + 1

                while left >= 0 and right < len(s):
                    print(f"checking for left {left}, right {right}, s[left] {s[left]}, s[right] {s[right]}")
                    if s[left] != s[right]:
                        break

                    left -= 1
                    right += 1
                    count += 1
            
            return count


        return expandAndCheckPalindrome("odd",s) + \
                expandAndCheckPalindrome("even",s)
    

obj = Solution()
s = "abc"
s = "aaa"
print(obj.countSubstrings(s))