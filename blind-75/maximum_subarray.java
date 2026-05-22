class Solution {
	public int maxSubArray(int[] nums) {
		int maxSum = Integer.MIN_VALUE;
		int currSum = 0;
		
		for(int n: nums) {
			currSum = Math.max(currSum + n, n);
			maxSum = Math.max(maxSum, currSum);
		}
		
		return maxSum;
	}
}

class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();
		Test tester = new Test();
		
		int[] nums = new int[] {-2,1,-3,4,-1,2,1,-5,4};
		tester.assertEqual("Test case 1", obj.maxSubArray(nums), 6);
		
		nums = new int[] {1};
		tester.assertEqual("Test case 2", obj.maxSubArray(nums), 1);
		
		nums = new int[] {5,4,-1,7,8};
		tester.assertEqual("Test case 3", obj.maxSubArray(nums), 23);
	}
}