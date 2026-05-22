// leetcode 238

import java.util.*;

class Solution {

	public int[] reverseArray(int[] arr) {
		int beg = 0;
		int end = arr.length - 1;

		while (beg < end) {
			int temp = arr[beg];
			arr[beg] = arr[end];
			arr[end] = temp;

			beg++;
			end--;
		}

		return arr;
	}

	/*public int[] productExceptSelf(int[] nums) {
		int prefixSum;
		int[] prefixArr = new int[nums.length + 1];
		Arrays.fill(prefixArr, 1);
		System.out.println("prefix arr before: " + Arrays.toString(prefixArr));

		for (int i = 0; i < nums.length; i++) {
			prefixSum = nums[i] * prefixArr[i];
			prefixArr[i + 1] = prefixSum;
		}

		System.out.println("prefix arr after: " + Arrays.toString(prefixArr));

		int postfixSum;
		int[] postfixArr = new int[nums.length + 1];
		Arrays.fill(postfixArr, 1);

		System.out.println("postfix arr before: " + Arrays.toString(postfixArr));

		for(int i = nums.length - 1, j = nums.length; i >= 0; i--, j--) {
			postfixSum = nums[i] * postfixArr[j];
			postfixArr[j - 1] = postfixSum;
		}

		// Arrays.reverse(postfixArr);
		// postfixArr = reverseArray(postfixArr);
		System.out.println("postfix arr after: " + Arrays.toString(postfixArr));


		int[] res = new int[nums.length];

		for (int i = 0; i < nums.length; i++) {
			res[i] = prefixArr[i] * postfixArr[i + 1];
		}

		return res;
	}*/

	public int[] productExceptSelf(int[] nums) {
		List<Integer> prefixArr = new ArrayList<>();
		List<Integer> postfixArr = new ArrayList<>();
		prefixArr.add(1);
		postfixArr.add(1);

		for (int n : nums) {
			prefixArr.add(n * prefixArr.get(prefixArr.size() - 1));
		}

		for(int i = nums.length - 1; i >= 0; i--) {
			postfixArr.add(nums[i] * postfixArr.get(postfixArr.size() - 1));
		}

		Collections.reverse(postfixArr);

		int[] res = new int[nums.length];
		for(int i = 0; i < prefixArr.size() - 1; i++) {
			res[i] = prefixArr.get(i) * postfixArr.get(i + 1);
		}

		return res;
	}
}


class Main {
	public static void main (String[] args) {
		Solution obj = new Solution();

		int[] nums = new int[] {1,2,3,4};
		System.out.println(Arrays.toString(obj.productExceptSelf(nums)));
	}
}