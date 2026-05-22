import java.util.*;

class Solution {
	public List<List<Integer>> threeSum (int[] nums) {

		List<List<Integer>> res = new ArrayList<>();

		Arrays.sort(nums);
		System.out.println(Arrays.toString(nums));

		for (int i = 0;i < nums.length; i++){
			if (nums[i] > 0) {
				break;
			}
			if (i > 0 && nums[i] == nums[i - 1]) {
				continue;
			}

			int lPointer = i + 1;
			int rPointer = nums.length - 1;

			while (lPointer < rPointer) {
				int sum = nums[i] + nums[lPointer] + nums[rPointer];

				if (sum == 0) {
					List<Integer> threeNums = new ArrayList<>();
					threeNums.add(nums[i]);
					threeNums.add(nums[lPointer]);
					threeNums.add(nums[rPointer]);
					res.add(threeNums);
					lPointer++;
					rPointer--;

					while (lPointer < rPointer && nums[lPointer] == nums[lPointer - 1]) {
						lPointer++;
					}

					while (lPointer < rPointer && nums[rPointer] == nums[rPointer + 1]) {
						rPointer--;
					}
				} else if (sum > 0) {
					rPointer--;
				} else {
					lPointer++;
				}
			}
		}

		return res;
	}
}

class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		int[] nums = new int[] {-1,0,1,2,-1,-4};
		System.out.println(obj.threeSum(nums));
	}
}