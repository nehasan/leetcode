class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        numStack1 = [int(n) for n in num1]
        numStack2 = [int(n) for n in num2]

        maxLen = max(len(numStack1), len(numStack2))

        addedDigits = []
        carry = 0
        while maxLen > 0:
            sum = 0
            firstNum = numStack1.pop() if len(numStack1) > 0 else 0
            secNum = numStack2.pop() if len(numStack2) > 0 else 0

            sum += firstNum + secNum + carry
            d = sum % 10
            carry = int(sum / 10)

            addedDigits.append(d)
            
            maxLen -= 1
        
        if carry > 0:
            addedDigits.append(carry)
        
        print(f"addedDigits : {addedDigits}")

        length = len(addedDigits)
        lastIndex = length - 1

        for i in range(int(length / 2)):
            temp = addedDigits[i]
            addedDigits[i] = addedDigits[lastIndex]
            addedDigits[lastIndex] = temp

            lastIndex -= 1

        return "".join(map(str, addedDigits))


soln = Solution()
num1 = "999"
num2 = "999"
print(soln.addStrings(num1, num2))