# leetcode 155

from collections import deque


'''
Approach used maintaining double stacks. One stack normally stores values and another
stores the min value corresponding to each value in the normal stack.
Suppose stack gets -2, so -2 gets into the minStack as min value,
Now stack gets 0, the minStack still gets -2 as the min value. At this point stack is [-2, 0]
And minStack is [-2,-2]
Now stack gets -3, so the current values will be [-2, 0, -3] and [-2, -2, -3] respectively
'''
class MinStack:
	def __init__(self):
		self.stack = deque()
		self.minStack = deque()

	def push(self, val: int) -> None:
		self.stack.append(val)

		if len(self.minStack) == 0:
			self.minStack.append(val)
		else:
			self.minStack.append(min(self.minStack[-1], val))

	def pop(self) -> None:
		self.stack.pop()
		self.minStack.pop()

	def top(self) -> int:
		return self.stack[-1]

	def getMin(self) -> int:
		return self.minStack[-1]


obj = MinStack()

ops = ["MinStack","push","push","push","getMin","pop","top","getMin"]
values = [[],[-2],[0],[-3],[],[],[],[]]

res = list()
for i, op in enumerate(ops):
	if op == "push":
		obj.push(values[i][0])
		res.append(None)
	elif op == "pop":
		obj.pop()
		res.append(None)
	elif op == "top":
		res.append(obj.top())
	elif op == "getMin":
		res.append(obj.getMin())

print(res)