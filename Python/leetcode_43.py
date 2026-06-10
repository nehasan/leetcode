class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        numOneStack = []
        numTwoStack = []

        numOneStack = [int(n) for n in num1]
        numTwoStack = [int(n) for n in num2]

        print(f"numOneStack: {numOneStack}")
        print(f"numTwoStack: {numTwoStack}")
        multipliedNums = []
        skipDigits = 0
        numOneLen = len(numOneStack)

        row = []
        while numOneLen > 0:
            row = [0 for i in range(skipDigits)]
            print(f"row after placing zeros: {row}")
            carry = 0
            numTwoLen = len(numTwoStack)
            while numTwoLen > 0:
                print(f"numOneStack[numOneLen - 1]: {numOneStack[numOneLen - 1]}, numTwoStack[numTwoLen - 1]: {numTwoStack[numTwoLen - 1]}")
                product = (numOneStack[numOneLen - 1] * numTwoStack[numTwoLen - 1]) + carry
                d = int(product % 10)
                carry = int(product / 10)
                row.append(d)

                numTwoLen -= 1
            
            if carry > 0:
                row.append(carry)
            
            # here the calculated nums are going to be like
            # if "22", "22" then, [[4,4], [0, 4, 4]]
            multipliedNums.append(row)
            print(multipliedNums)
            skipDigits += 1
            numOneLen -= 1
        
        # now its time to add them up
        maxLength = 0
        for row in multipliedNums:
            maxLength = max(maxLength, len(row))
        
        resDigits = []
        index = 0
        carry = 0
        while maxLength > 0:
            sum = 0
            for row in multipliedNums:
                try:
                    sum += row[index]
                except:
                    sum += 0
            
            sum += carry
            print(f"sum: {sum}")
            d = sum % 10
            carry = int(sum / 10)
            
            resDigits.append(d)
            index += 1
            maxLength -= 1
        
        if carry > 0:
            resDigits.append(carry)
        
        # reverse the digits, that would be the result
        length = len(resDigits)
        lastIndex = length - 1
        for i in range(int(length / 2)):
            temp = resDigits[lastIndex]
            resDigits[lastIndex] = resDigits[i]
            resDigits[i] = temp

            lastIndex -= 1

        return "".join(map(str, resDigits))



soln = Solution()
num1 = "0"
num2 = "0"
print(soln.multiply(num1, num2))
        


        
        