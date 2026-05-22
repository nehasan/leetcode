from collections import deque

class MyQueue:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
      self.q.append(x)
        

    def pop(self) -> int:
      return self.q.popleft()
    
    def peek(self) -> int:
      return self.q[0]
    
    def empty(self) -> bool:
      return True if len(self.q) == 0 else False


obj = None
ops = ["MyQueue", "push", "push", "peek", "pop", "empty"]
values = [[], [1], [2], [], [], []]
res = []

for i, op in enumerate(ops):
  if op == "MyQueue":
    obj = MyQueue()
    res.append(None)
  elif op == "push":
    obj.push(values[i][0])
    res.append(None)
  elif op == "peek":
    res.append(obj.peek())
  elif op == "pop":
    res.append(obj.pop())
  elif op == "empty":
    res.append(obj.empty())

print(res)