// leetcode 150

import java.util.*;

class Solution {

	public int performArithmeticOp(int lhs, int rhs, String op) {
		switch (op) {
			case "+":
				return lhs + rhs;
			case "-":
				return lhs - rhs;
			case "*":
				return lhs * rhs;
			case "/":
				return (int) Math.floor(lhs / rhs);
		}
		return 0;
	}

	public int evalRPN (String[] tokens) {
		Stack<String> tokenStack = new Stack<>();
		String[] validOps = {"+", "-", "*", "/"};
		List<String> validOpList = new ArrayList<>(Arrays.asList(validOps));

		for (String token : tokens) {

			if (validOpList.contains(token)) {
				// evaluate the expression
				int rightExpression = Integer.parseInt(tokenStack.pop());
				int leftExpression  = Integer.parseInt(tokenStack.pop());

				System.out.println("rightExpression " + rightExpression + " leftExpression: " + leftExpression);

				int res = performArithmeticOp(leftExpression, rightExpression, token);

				tokenStack.push(String.valueOf(res));
				System.out.println("after operation current stack: " + tokenStack);
			} else {
				tokenStack.push(token);
			}
		}

		return Integer.parseInt(tokenStack.pop());
	}	
}


class Main {
	public static void main (String[] args) {
		Solution obj = new Solution();
		Test tester = new Test();

		String[] tokens = {"2","1","+","3","*"};
		tester.assertEqual("Test case 1", obj.evalRPN(tokens), 9);

		tokens = new String[] {"4","13","5","/","+"};
		tester.assertEqual("Test case 2", obj.evalRPN(tokens), 6);

		tokens = new String[] {"10","6","9","3","+","-11","*","/","*","17","+","5","+"};
		tester.assertEqual("Test case 2", obj.evalRPN(tokens), 22);
	}
}