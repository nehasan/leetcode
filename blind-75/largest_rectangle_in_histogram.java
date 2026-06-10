// leetcode 84

import java.util.*;

class Pair {
	public int height;
	public int index;

	Pair() {}
	Pair(int height, int index) {
		this.height = height;
		this.index = index;
	}

	public String toString() {
		return this.height + " " + this.index;
	}
}

class Solution {

	/*
	* Approach, using stack
	* When we find a larger height we simply put that into the stack as a pair of (height, index)
	* When we find a height lower than the prev height then we pop off the heights
	* until we find a lower height. In this case the newly added height,index pair would be the
	* current height and the index of the last popped index. This process indicates the current
	* height can be extended further left till this index. However, within this process we calculate
	* the maxArea = lastIndexHeight.height * (i - lastHeightIndex.index)
	* After the original iteration stack will may have some heights which indicate that they can be
	* extended to the right till the end.
	* Now we take the outBoundIndex = heights.length and pop off each left height,index pair and 
	* calculate the maxArea
	* Time & Space complexity : O(n)
	*/
	public int largestRectangleArea(int[] heights) {
		Stack<Pair> heightIndexStack = new Stack<>();
		int maxArea = Integer.MIN_VALUE;

		heightIndexStack.add(new Pair(heights[0], 0));
		for (int i = 1; i < heights.length; i++) {
			if (heights[i] <= heights[i - 1]) {
				Pair lastHeightIndex = new Pair(-1, -1);
				while(true) {
					if (heightIndexStack.isEmpty()) {
						lastHeightIndex.index = -1;
						break;
					}
					lastHeightIndex = heightIndexStack.peek();
					maxArea = Math.max(maxArea, (lastHeightIndex.height  * (i - lastHeightIndex.index)));
					if (lastHeightIndex.height < heights[i]) {
						break;
					}
					heightIndexStack.pop();
				}

				System.out.println("lastHeightIndex here " + lastHeightIndex);
				heightIndexStack.push(new Pair(heights[i], lastHeightIndex.index + 1));
			} else {
				heightIndexStack.add(new Pair(heights[i], i));
			}
		}

		System.out.println("current heightIndexStack " + heightIndexStack);

		int outBoundIndex = heights.length;
		while (!heightIndexStack.isEmpty()) {
			Pair lastHeightIndex = heightIndexStack.pop();
			System.out.println("lastHeightIndex " + lastHeightIndex);
			maxArea = Math.max(maxArea, (lastHeightIndex.height  * (outBoundIndex - lastHeightIndex.index)));
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
		// int[] heights = {3,6,5,7,4,8,1,0};
		// int[] heights = {1,1};
		// int[] heights = {2,1,2};
		int[] heights = {4,2,0,3,2,5};
		System.out.println(obj.largestRectangleArea(heights));
	}
}