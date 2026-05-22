import java.util.Set;
import java.util.HashSet;

class Solution {
	public boolean containsDuplicate(int[] nums) {
		Set<Integer> set = new HashSet<Integer>();
		
		for(int n: nums) {
			// System.out.println(n);
			if (set.contains(n)) {
				return true;
			} else {
				set.add(n);
			}
		}
		
		return false;
	}
}

class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();
		Test tester = new Test();
		
		int[] nums = new int[] {1, 2, 3, 1};
		tester.assertEqual("Test case 1", obj.containsDuplicate(nums), true);
			
		nums = new int[] {1, 2, 3, 4};
		tester.assertEqual("Test case 1", obj.containsDuplicate(nums), false);
	}
}