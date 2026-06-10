// leetcode 435

import java.util.*;

class Solution {
	public int eraseOverlapIntervals(int[][] intervals) {
        
        List<int[]> erased = new ArrayList<>();
        int count = 0;

        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));
        erased.add(intervals[0]);

        for (int i = 1; i < intervals.length; i++) {
        	int[] prevInterval = erased.get(erased.size() - 1);
        	if (intervals[i][0] < prevInterval[1]) {
        		count++;
        		erased.remove(erased.size() - 1);
        		erased.add(new int[] {Math.min(prevInterval[0], intervals[i][0]), Math.min(prevInterval[1], intervals[i][1])});
        	} else {
        		erased.add(intervals[i]);
        	}
        }

        return count;
    }
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		int[][] intervals = {{1,2}, {2,3}, {3,4}, {1,3}};
		System.out.println(obj.eraseOverlapIntervals(intervals));

		intervals = new int[][] {{1,2}, {1,2}, {1,2}};
		System.out.println(obj.eraseOverlapIntervals(intervals));

		intervals = new int[][] {{1,2}, {2,3}};
		System.out.println(obj.eraseOverlapIntervals(intervals));
	}
}