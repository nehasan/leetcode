class Solution:
  def addBinary(self, a: str, b: str) -> str:
    
    arrA = list(a)
    arrB = list(b)
    
    res = []
    carry = 0
    while len(arrA) > 0 or len(arrB) > 0:
      x = int(arrA.pop()) if len(arrA) > 0 else 0
      y = int(arrB.pop()) if len(arrB) > 0 else 0
      
      if x + y + carry == 3:
        res.append("1")
        carry = 1
      elif x + y + carry == 2:
        res.append("0")
        carry = 1
      else:
        res.append(str(x + y + carry))
        carry = 0
      
    if carry == 1:
      res.append("1")
    
    res = res[::-1]
    
    return "".join(res)
    

obj = Solution()
# a = "11"
# b = "1"
# print(obj.addBinary(a, b))

def test__001():
  a = "11"
  b = "1"
  assert(obj.addBinary(a, b)) == "100"
  
def test__002():
  a = "1010"
  b = "1011"
  assert(obj.addBinary(a, b)) == "10101"