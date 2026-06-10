// leetcode 84

import java.util.*;

class Solution {

	/*
	* Approach, using stack and finding the left and rightmost limit of a bar (height) in the histogram
	* The brute force solution for this problem is that for a single height height[i] we expand left
	* to find a lower height where we stop and this is called the left limit of that height. Because
	* If a height in the left is lower than the height[i] then the height cannot be a part of this area
	* So we cap the index there. Now we do the same for the right side and find a height that is lower 
	* than the current height[i]. We cap the expansion here. That is the maxArea of a single height
	* Which is (rightLimitIndex - leftLimitIndex) * height[i]
	* However, the above solution is O(n^2), To optimize the solution we traverse the array from left to right
	* to find the leftLimit and again right to left to find the rightLimit. The process uses a stack to memorize the 
	* last index used
	* - Left to right traverse : Initially the stack is empty and we put the index 0 in it.
	* - Now if the current height[i] is bigger than the  previous height[i - 1] then this a left cap for this height
	* - Stack is inserted with the stack top + 1
	* - Else we pop the stack until we find a lower height and cap the index by top of the stack + 1. The process actually store the
	* left caps (limits) for each of the height
	* - Right to left traverse: We start iterating over the heights again but this time right to left
	* - This process follow the exact procedues and store the limits for right
	* - Now the maxArea would be max of (rightCap[i] - leftCap[i]) * height[i]
	* - Time complexity is O(n)
	*/
	public int largestRectangleArea(int[] heights) {
		Stack<Integer> indexStack = new Stack<>();
		List<Integer> leftLimits = new ArrayList<>();
		List<Integer> rightLimits = new ArrayList<>();
		int maxArea = Integer.MIN_VALUE;

		indexStack.push(0);
		leftLimits.add(0);
		for (int i = 1; i < heights.length; i++) {
			System.out.println("curr ht : " + heights[i] + " last ht " + heights[i - 1]);
			
			// the current height is less or equal to the previous one
			// so limit would be the same as last
			if (heights[i] <= heights[i - 1]) {
				System.out.println("ht is lower or eq, so popping till find a lower ht or empty stack");
				int lastIndexInStack;
				do {
					if (indexStack.isEmpty()) {
						lastIndexInStack = -1;
						break;
					}
					lastIndexInStack = indexStack.peek();
					if (heights[lastIndexInStack] < heights[i]) {
						break;
					}
					indexStack.pop();
					System.out.println("popping stack top " + indexStack + " top was " + lastIndexInStack);
				} while(true);
				leftLimits.add(lastIndexInStack + 1);
				System.out.println("curr leftLimits " + leftLimits);
				indexStack.push(i);

			// the current height is bigger than the previous one
			// so cap the limit to the current index
			} else {
				System.out.println("ht is bigger, so capping the limit");
				// find the last left limit from the stack
				int lastIndex = indexStack.peek();
				// push index at the top of the stack + 1
				leftLimits.add(lastIndex + 1);
				System.out.println("leftLimits.add(lastIndex + 1) : " + leftLimits);
				indexStack.push(i);
			}
		}

		System.out.println("leftLimits " + leftLimits);

		indexStack.clear();
		indexStack.push(heights.length - 1);
		rightLimits.add(heights.length - 1);
		for (int i = heights.length - 2; i >= 0; i--) {
			System.out.println("curr ht : " + heights[i] + " last ht " + heights[i + 1]);
			
			// the current height is less or equal to the previous one
			// so limit would be the same as last
			if (heights[i] <= heights[i + 1]) {
				System.out.println("ht is lower or eq, so popping till find a lower ht or empty stack");
				int lastIndexInStack;
				do {
					if (indexStack.isEmpty()) {
						lastIndexInStack = heights.length;
						break;
					}
					lastIndexInStack = indexStack.peek();
					if (heights[lastIndexInStack] < heights[i]) {
						break;
					}
					indexStack.pop();
					System.out.println("popping stack top " + indexStack + " top was " + lastIndexInStack);
				} while(heights[lastIndexInStack] >= heights[i]);
				rightLimits.add(lastIndexInStack - 1);
				System.out.println("curr rightLimits " + rightLimits);
				indexStack.push(i);

			// the current height is bigger than the previous one
			// so cap the limit to the current index
			} else {
				System.out.println("ht is bigger, so capping the limit");
				// find the last right limit from the stack
				int lastIndex = indexStack.peek();
				// push index at the top of the stack - 1
				rightLimits.add(lastIndex - 1);
				System.out.println("rightLimits.add(lastIndex - 1) : " + rightLimits);
				indexStack.push(i);
			}
		}

		Collections.reverse(rightLimits);
		System.out.println("rightLimits " + rightLimits);

		for (int i = 0; i < leftLimits.size(); i++) {
			int width = (rightLimits.get(i) - leftLimits.get(i)) + 1;
			maxArea = Math.max(maxArea, (width * heights[i]));
		}

		return maxArea;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		// int[] heights = {2,1,5,6,2,3};
		// int[] heights = {2,1,6,6,2,3};
		// int[] heights = {2,4};
		int[] heights = {3,6,5,7,4,8,1,0};
		System.out.println(obj.largestRectangleArea(heights));
	}
}