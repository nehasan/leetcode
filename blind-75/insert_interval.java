// leetcode 57

import java.util.*;

class Solution {
	public int[][] insert(int[][] intervals, int[] newInterval) {

		// first insert the interval into its right position
		List<int[]> inserted = new ArrayList<>();

		boolean done = false;
		for (int[] interval : intervals) {
			if (!done) {
				// insert when new interval start is less than the current interval
				if (newInterval[0] < interval[0]) {
					inserted.add(newInterval);
					done = true;
				}
			}
			inserted.add(interval);
		}

		if (!done) {
			inserted.add(newInterval);
		}

		// now merge the intervals
		List<int[]> merged = new ArrayList<>();
		merged.add(inserted.get(0));
		for (int i = 1; i < inserted.size(); i++) {
			int[] a = merged.get(merged.size() - 1);
			int[] b = inserted.get(i);
			// conflict example a [1,3] b [2,5]
			if (b[0] <= a[1]) {
				int[] c = {Math.min(a[0], b[0]), Math.max(a[1], b[1])};
				merged.remove(merged.size() - 1);
				merged.add(c);
			} else {
				merged.add(b);
			}
		}

		return merged.toArray(new int[merged.size()][]);
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		int[][] intervals = {{1,3},{6,9}};
		int[] newInterval = {2,5};

		intervals = new int[][] {};
		newInterval = new int[] {5,7};

		intervals = new int[][] {{1,5}};
		newInterval = new int[] {2,7};
		System.out.println(Arrays.deepToString(obj.insert(intervals, newInterval)));
	}
}