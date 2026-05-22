from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
      self.q.append(x)
        
    def pop(self) -> int:
      return self.q.pop()
    
    def top(self) -> int:
      return self.q[len(self.q) - 1]
    
    def empty(self) -> bool:
      return True if len(self.q) == 0 else False


obj = None
ops = ["MyStack", "push", "push", "top", "pop", "empty"]
values = [[], [1], [2], [], [], []]
res = []

for i, op in enumerate(ops):
  if op == "MyStack":
    obj = MyStack()
    res.append(None)
  elif op == "push":
    obj.push(values[i][0])
    res.append(None)
  elif op == "top":
    res.append(obj.top())
  elif op == "pop":
    res.append(obj.pop())
  elif op == "empty":
    res.append(obj.empty())

print(res)