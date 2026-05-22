class Solution:

    def decodeString(self, s: str) -> str:
        stackArr = []
        stackNums = []
        number = ''

        for c in s:
            if c >= '0' and c <= '9':
                number += c
            elif c == '[':
                stackArr.append(c)
                print(int(number))
                stackNums.append(int(number))
                number = ''
            elif c == ']':
                tempStackArr = []
                tempChar = stackArr.pop()
                print(f'--- {tempChar}')

                while tempChar != '[':
                    tempStackArr.append(tempChar)
                    tempChar = stackArr.pop()
                
                # tempStr = ''.join(str(x) for x in tempStackArr)[::-1]
                tempStr = ''.join(tempStackArr[::-1])
                print(f'--- {tempStr}')

                repeat = stackNums.pop()
                for i in range(0, repeat):
                    stackArr.append(tempStr)
            else:
                stackArr.append(c)
        

        return ''.join(str(x) for x in stackArr)
    

obj = Solution()
# print(obj.decodeString('3[a]2[bc]'))
# print(obj.decodeString('3[a2[bc]]'))
print(obj.decodeString("2[abc]3[cd]ef"))