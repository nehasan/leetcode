import java.util.*;

class Solution {
	public int[][] insert(int[][] intervals, int[] newInterval) {
		if (intervals.length == 0) {
			return new int[][] {newInterval};
		}
		
		boolean flag = false;
		int start, end;
		int newStart = newInterval[0];
		int newEnd   = newInterval[1];
		int[] lastInserted, currInterval;
		List<int[]> inserted = new ArrayList<>();
		
		// insert into the array
		inserted.add(new int[] {0, 0});
		for (int i = 0; i < intervals.length; i++) {
			currInterval = intervals[i];
			start = currInterval[0];
			end   = currInterval[1];
			
			lastInserted = inserted.get(inserted.size() - 1);
			if (newStart >= lastInserted[0] && newStart <= start) {
				inserted.add(newInterval);
				flag = true;
			}
			
			inserted.add(currInterval);
		}
		
		if (!flag) {
			inserted.add(newInterval);
		}
		
		for (int[] x: inserted) {
			System.out.println(Arrays.toString(x));
		}
		
		List<int[]> merged = new ArrayList<>();
		merged.add(inserted.get(1));
		
		// fix overlaps
		int prevStart, prevEnd;
		for (int i = 2; i < inserted.size(); i++) {
			currInterval = inserted.get(i);
			System.out.println("processing currInterval: " + Arrays.toString(currInterval));
			start = currInterval[0];
			end   = currInterval[1];
			
			prevStart = merged.get(merged.size() - 1)[0];
			prevEnd   = merged.get(merged.size() - 1)[1];
			
			if (prevEnd >= start) {
				System.out.println("before merge valeu: " + Arrays.toString(merged.get(merged.size() - 1)));
				merged.remove(merged.size() - 1);
				merged.add(new int[] {Math.min(prevStart, start), Math.max(prevEnd, end)});
				System.out.println("after merge valeu: " + Arrays.toString(merged.get(merged.size() - 1)));
			} else {
				merged.add(currInterval);
				System.out.println("normal adding to  merge: " + Arrays.toString(merged.get(merged.size() - 1)));
			}
		}
		
		return merged.toArray(new int[merged.size()][]);
	}
}

class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();
		Test tester = new Test();
		
		int[][] intervals = new int[][] {{1,3},{6,9}};
		int[] newInterval = new int[] {2,5};
		// int[][] res = obj.insert(intervals, newInterval);
// 		for(int[] a: res) {
// 			System.out.println(Arrays.toString(a));
// 		}
//
// 		intervals = new int[][] {{1,2},{3,5},{6,7},{8,10},{12,16}};
// 		newInterval = new int[] {4,8};
// 		res = obj.insert(intervals, newInterval);
// 		for(int[] a: res) {
// 			System.out.println(Arrays.toString(a));
// 		}
//
// 		intervals = new int[][] {};
// 		newInterval = new int[] {5,7};
// 		res = obj.insert(intervals, newInterval);
// 		for(int[] a: res) {
// 			System.out.println(Arrays.toString(a));
// 		}
//
// 		intervals = new int[][] {{1,5}};
// 		newInterval = new int[] {2,7};
// 		res = obj.insert(intervals, newInterval);
// 		for(int[] a: res) {
// 			System.out.println(Arrays.toString(a));
// 		}
//
// 		intervals = new int[][] {{2,5},{6,7},{8,9}};
// 		newInterval = new int[] {0,1};
// 		res = obj.insert(intervals, newInterval);
// 		for(int[] a: res) {
// 			System.out.println(Arrays.toString(a));
// 		}
		
		intervals = new int[][] {{3,5},{12,15}};
		newInterval = new int[] {6,6};
		int[][] res = obj.insert(intervals, newInterval);
		for(int[] a: res) {
			System.out.println(Arrays.toString(a));
		}
	}
}