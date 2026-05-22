// leetcode 155

import java.util.*;

class MinStack {
	Stack<Integer> minStack;
	Stack<Integer> stack;

	MinStack () {
		this.stack = new Stack<>();
		this.minStack = new Stack<>();
	}

	public void push (int val) {
		this.stack.add(val);

		if (this.minStack.isEmpty()) {
			this.minStack.add(val);
		} else {
			this.minStack.add(Math.min(this.minStack.peek(), val));
		}
	}

	public void pop () {
		this.stack.pop();
		this.minStack.pop();
	}

	public int top () {
		return this.stack.peek();
	}

	public int getMin () {
		return this.minStack.peek();
	}

}


class Main {
	public static void main (String[] args) {
		MinStack obj = new MinStack();
		
		String[] ops = {"MinStack","push","push","push","getMin","pop","top","getMin"};
		int[][] values = {{}, {-2}, {0}, {-3}, {}, {}, {}, {}};
		List<Integer> res = new ArrayList<>();

		for (int i = 0; i < ops.length; i++) {
			switch(ops[i]) {
				case"push":
					obj.push(values[i][0]);
					res.add(null);
					break;
				case "pop":
					obj.pop();
					res.add(null);
					break;
				case "top":
					res.add(obj.top());
					break;
				case "getMin":
					res.add(obj.getMin());
					break;
			}
		}

		System.out.println(res);
	}
}