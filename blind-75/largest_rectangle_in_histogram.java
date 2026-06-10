// leetcode 84

import java.util.*;

class Pair {
	int height;
	int index;

	Pair () {}
	Pair (int height, int index) {
		this.height = height;
		this.index = index;
	}

	public String toString() {
		return "(" + this.height + "," + this.index + ")";
	}
}

class Solution {
	/*
	* Approach, using stack DS and finding the left and right limit of each bar
	* In this approach we push a pair (height, index) to the stack
	* When we find a height is bigger than the current one then we push it to the stack
	* This means the prev height can be extended to the right upto this current hegiht
	* When we find a height lower than the current one then we keep popping the left bigger
	* ones until we find a lower one.
	* This means the current height can be extended to the left just after that lowest height
	* When popping the height we keep track of the last popped one to update the stack with the 
	* current height as stack.push((current_height, last_popped_index))
	* Also we keep measuring the maxArea while popping.
	* And if the stack is not empty that means those heights can be extended to the further right
	* While measuring the area for those heights we take outBoundIndex as heights.length
	*/
	public int largestRectangleArea(int[] heights) {
		Stack<Pair> heightIndexStack = new Stack<>();
		int maxArea = Integer.MIN_VALUE;

		heightIndexStack.push(new Pair(heights[0], 0));
		for (int i = 1; i < heights.length; i++) {
			if (heights[i] <= heights[i - 1]) {
				// current height is lower than the prev one
				// need to pop the stack until a lower one is found
				Pair lastHeightIndex = null, prevLastHeightIndex = null;
				while(true) {
					if (heightIndexStack.isEmpty()) {
						prevLastHeightIndex.index = 0;
						break;
					}
					lastHeightIndex = heightIndexStack.peek();
					if (lastHeightIndex.height < heights[i]) {
						break;
					}
					maxArea = Math.max(maxArea, ((i - lastHeightIndex.index) * lastHeightIndex.height));
					prevLastHeightIndex = heightIndexStack.pop();
				}

				heightIndexStack.push(new Pair(heights[i], prevLastHeightIndex.index));
			} else {
				// current height is greater than the prev one
				heightIndexStack.push(new Pair(heights[i], i));
			}
		}

		int outBoundIndex = heights.length;
		while(!heightIndexStack.isEmpty()) {
			Pair heightIndex = heightIndexStack.pop();
			maxArea = Math.max(maxArea, ((outBoundIndex - heightIndex.index) * heightIndex.height));
		}

		return maxArea;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		// int[] heights = {2,1,5,6,2,3};
		int[] heights = {2,1,6,6,2,3};
		// int[] heights = {1,1};
		// int[] heights = {2,4};
		// int[] heights = {2,1,2};
		// int[] heights = {3,6,5,7,4,8,1,0};
		// int[] heights = {4,2,0,3,2,5};
		System.out.println(obj.largestRectangleArea(heights));
	}
}