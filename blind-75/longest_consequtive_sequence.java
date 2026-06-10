// leetcode 128

import java.util.*;

class Solution {

	/*
	* Approach, hashset and continuously keep finding consequtive numbers if 
	* a number does not have a previous number (num - 1)
	*/
	public int longestConsecutive(int[] nums) {

		Set<Integer> numSet = new HashSet<>();
		int longest = Integer.MIN_VALUE;

		for (int n : nums) {
			numSet.add(n);
		}
		
		for (int n : nums) {
			int length;

			if (!numSet.contains(n - 1)) {
				int nextNum = n + 1;
				length = 1;

				while (numSet.contains(nextNum)) {
					nextNum += 1;
					length++;
				}

				longest = Math.max(longest, length);
			}
		}

		return longest;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		// int[] nums = {100,4,200,1,3,2};
		int[] nums = {0,3,7,2,5,8,4,6,0,1};
		// int[] nums = {1,0,1,2};
		System.out.println(obj.longestConsecutive(nums));
	}
}