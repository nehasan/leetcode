class Solution:
    def reverse(self, x: int) -> int:
        n = 0 - x if x < 0 else x
        
        digits = []
        MAX_INT = pow(2, 31) - 1
        while n > 0:
            digits.append(n % 10)
            n = int(n / 10)
        
        res = 0

        print(digits)
        for digit in digits:
            res = res * 10 + digit
        
        res = 0 if res > MAX_INT else res
        return 0 - res if x < 0 else res


soln = Solution()
# x = 123
# x = 120
# x = -120
# x = 1534236469
x = 1563847412
print(soln.reverse(x))