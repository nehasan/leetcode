from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stack = []
        length = len(digits)

        for d in digits:
            stack.append(d)
        
        carry = 0
        plusOne = 1
        resDigits = []

        while length > 0:
            sum = 0
            n = stack.pop()
            sum = n + carry + plusOne

            d = int(sum % 10)
            carry = int(sum / 10)
            resDigits.append(d)

            plusOne = 0
            length -= 1
        
        if carry > 0:
            resDigits.append(carry)

        # print(resDigits)
        resLength = len(resDigits)
        # print(resLength)
        lastPos = resLength - 1

        for i in range(int(resLength / 2)):
            temp = resDigits[i]
            resDigits[i] = resDigits[lastPos]
            resDigits[lastPos] = temp

            lastPos -= 1
        
        return resDigits


soln = Solution()
digits = [1,2,3]
digits = [4,3,2,1]
digits = [9]
print(soln.plusOne(digits))

