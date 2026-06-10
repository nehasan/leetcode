class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result  = 0
        for i, c in enumerate(columnTitle[::-1]):
            result += (ord(c) - ord('A') + 1) * (26 ** i)
        
        return result
    

# Test cases
sol = Solution()
print(sol.titleToNumber("A")) # 1
print(sol.titleToNumber("AB")) # 28
print(sol.titleToNumber("ZY")) # 701