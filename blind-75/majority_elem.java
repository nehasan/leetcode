import java.util.*;

class Solution {
	public int majorityElement(int[] nums) {
		HashMap<Integer, Integer> map = new HashMap<>();
		
		for(int i = 0; i < nums.length; i++) {
			map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
		}
		
		map.entrySet().stream()
			.forEach(e -> System.out.println(e.getKey() + " " + e.getValue()));
		
		return 1;
	}
}

class Main {
	public static void main(String[] args) {
		int[] nums = {2, 3, 2};
		Solution soln = new Solution();
		soln.majorityElement(nums);
	}
}