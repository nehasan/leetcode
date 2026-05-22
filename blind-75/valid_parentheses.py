class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        openBraces = ["(", "{", "["]
        closedBraces = [")", "}", "]"]
        
        for char in s:
            if char in openBraces:
                stack.append(char)
            elif char in closedBraces:
                if len(stack) == 0:
                    return False
                elif char == ")" and stack.pop() != "(":
                    return False
                elif char == "}" and stack.pop() != "{":
                    return False
                elif char == "]" and stack.pop() != "[":
                    return False
        
        return True if len(stack) == 0 else False


obj = Solution()
# print(obj.isValid("(]"))

def test__001():
    s = "()"
    assert(obj.isValid(s)) == True
    
def test__002():
    s = "()[]{}"
    assert(obj.isValid(s)) == True

def test__003():
    s = "(]"
    assert(obj.isValid(s)) == False

def test__004():
    s = " "
    assert(obj.isValid(s)) == True

def test__005():
    s = "["
    assert(obj.isValid(s)) == False