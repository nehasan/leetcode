# leetcode 150

from typing import List

class Solution:

	def evaluate(self, lhs: str, rhs: str, op: str) -> int:
		if op == "+":
			return int(lhs) + int(rhs)
		elif op == "-":
			return int(lhs) - int(rhs)
		elif op == "*":
			return int(lhs) * int(rhs)
		elif op == "/":
			return int(int(lhs) / int(rhs))

	def evalRPN(self, tokens: str) -> int:
		
		validOps = ["+", "-", "*", "/"]
		tokenStack = list()

		for token in tokens:
			if token in validOps:
				rightExpression = tokenStack.pop()
				leftExpression = tokenStack.pop()

				res = self.evaluate(leftExpression, rightExpression, token)
				tokenStack.append(res)
			else:
				tokenStack.append(token)


		return int(tokenStack.pop())


obj = Solution()

def test_001():
	tokens = ["2","1","+","3","*"]
	assert(obj.evalRPN(tokens)) == 9

def test_002():
	tokens = ["4","13","5","/","+"]
	assert(obj.evalRPN(tokens)) == 6

def test_003():
	tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
	assert(obj.evalRPN(tokens)) == 22