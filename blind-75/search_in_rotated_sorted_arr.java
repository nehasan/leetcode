// leetcode 33

import java.util.*;

class Solution {

	/*
	if nums[beg] < nums[mid] for example [4,5,6,7,0,1,2,3] or [0,1,2,3,4,5,6,7,8]
	now check if nums[beg] <= target < nums[mid] then consider first half else second half
	if nums[beg] > nums[mid] for example [7,0,1,2,3,4,5,6] or [6,7,0,1,2,3,4,5]
	now check if target < nums[mid] means <0,1...num[mid]> range or target >= nums[beg] means <...0,1,2> this range
	then first half else second half needs to be considered
	*/
	public int binarySearch(int[] nums, int target, int beg, int end) {
		int mid = (int)((beg + end) / 2);

		System.out.println(Arrays.toString(nums));
		System.out.println("beg : " + beg + " end: " + end + " mid: " + mid);
		System.out.println("nums[beg]: " + nums[beg] + " nums[end]: " + nums[end] + " nums[mid]: " + nums[mid]);

		if (beg == end) {
			if (nums[beg] == target) {
				return beg;
			}
			return -1;
		} else if (nums[mid] == target) {
			return mid;
		} else if (nums[beg] <= nums[mid]) {
			if (target >= nums[beg] && target < nums[mid]) {
				//first half
				end = mid;
			} else {
				// second half
				beg = mid + 1;
			}
		} else { // nums[beg] > nums[mid]
			if (target < nums[mid] || target >= nums[beg]) {
				//first half
				end = mid;
			} else {
				// second half
				beg = mid + 1;
			}
		}

		return binarySearch(nums, target, beg, end);
	}

	public int search(int[] nums, int target) {
		return binarySearch(nums, target, 0, (nums.length - 1));
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		int[] nums = {4,5,6,7,0,1,2};
		int target = 0;
		System.out.println(obj.search(nums, target)); // should print 4

		nums = new int[] {4,5,6,7,0,1,2};
		target = 3;
		System.out.println(obj.search(nums, target)); // should print -1

		nums = new int[] {1};
		target = 0;
		System.out.println(obj.search(nums, target)); // should print -1

		nums = new int[] {7,0,1,2,4,5,6};
		target = 1;
		System.out.println(obj.search(nums, target)); // should print 2

		nums = new int[] {1,3};
		target = 1;
		System.out.println(obj.search(nums, target)); // should print 0

		nums = new int[] {1,3};
		target = 3;
		System.out.println(obj.search(nums, target)); // should print 1
	}
}