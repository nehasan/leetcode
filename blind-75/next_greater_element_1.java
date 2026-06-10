// leetcode 496

import java.util.*;

class Solution {
	public int[] nextGreaterElement(int[] nums1, int[] nums2) {

		Map<Integer, Integer[2]> indexMap = new HashMap<>();
		Queue<Integer> queue = new LinkedList<>();

		for (int i = 0; i < nums2.length; i++) {
			// currElement = nums2[i];
			indexMap.put(nums2[i], new int[] {i, -1});
			while(!queue.isEmpty() && )
		}
	}
}