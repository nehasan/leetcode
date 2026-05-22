// leetcode 224

import java.util.*;

class Solution {

	public Stack<Character> operatorStack = new Stack<>();
	public	Stack<Integer> operandStack = new Stack<>();
	Character[] operators = {'+', '-', '*', '/', '(', ')'};
	public	Set<Character> operatorSet = new HashSet<>(
		Arrays.asList(operators)
	);

	public void evaluateExpression() {
		int rhs = operandStack.pop();
		int lhs = operandStack.size() > 0 ? operandStack.pop() : 0;
		char operator = operatorStack.pop();
		int res;
		System.out.println("lhs " + lhs + " rhs " + rhs + " op " + operator);

		if (operator == '+') {
			res = lhs + rhs;
		} else if (operator == '-') {
			res = lhs - rhs;
		} else if (operator == '*') {
			res = lhs * rhs;
		} else {
			if (rhs == 0) {
				res = 0;
			} else {
				res = lhs / rhs;
			}
		}

		operandStack.push(res);
	}

	public String listToString(List<Character> list) {
		StringBuilder sb = new StringBuilder(list.size());
		for (Character c : list) {
			sb.append(c);
		}

		return sb.toString();
	}

	public int calculate(String s) {
		// Stack<Character> operatorStack = new Stack<>();
		// Stack<Integer> operandStack = new Stack<>();
		// Set<Character> operatorSet = new HashSet<>(
		// 	Arrays.asList(new char[] {'+', '-', '*', '/', '(', ')'})
		// );


		List<Character> operand = new ArrayList<Character>();
		for (char ch : s.toCharArray()) {
			if (operatorSet.contains(ch)) {
				operatorStack.push(ch);
				if (operand.size() > 0) {
					// System.out.println("before operandStack " + operandStack);
					// System.out.println("before operand " + operand);
					operandStack.push(Integer.parseInt(listToString(operand)));
					operand.clear();

					System.out.println("current operatorStack " + operatorStack);
					System.out.println("current operandStack " + operandStack);
				}

				if (ch == ')') {
					evaluateExpression();
					operatorStack.pop(); // removes closing '('
				}
			} else if (ch >= '0' && ch <= '9'){
				operand.add(ch);
			}
		}

		if (operand.size() > 0) {
			operandStack.push(Integer.parseInt(listToString(operand)));
			operand.clear();
		}

		while(operandStack.size() > 1) {
			evaluateExpression();
		}

		return operandStack.pop();
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		// String s = "1 + 1";
		String s = " 2-1 + 2";  
		System.out.println(obj.calculate(s));
	}
}
