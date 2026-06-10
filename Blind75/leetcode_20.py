class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openParentheses = ['(', '{', '[']
        closedParentheses = [')', '}', ']']

        for c in s:
            if c in openParentheses:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if (c == closedParentheses[0] and temp != openParentheses[0]) \
                        or (c == closedParentheses[1] and temp != openParentheses[1]) \
                        or (c == closedParentheses[2] and temp != openParentheses[2]):
                        
                        return False
            
        
        return True if len(stack) == 0 else False


soln = Solution()
# s = "()"
# s = "()[]{}"
# s = "(]"
# s = "([])"
s = "([)]"
print(soln.isValid(s))