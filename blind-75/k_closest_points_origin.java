import java.util.*;

class Solution {
	/*
	* Approach, using priority queue and hashmap
	* Complexity, Traverse points O(n) + Priority Queue sorting O(nlogn)
	* Traverse the points and calculate the distances without sqrt, sqrt(10) and sqrt(8) are almost same, 4.0
	* While calculating distances d = x + y, hash the d as key and store the index i into an array, map[d] = [1,2,3]
	* The values are array because same distance can be found
	* Now read the min heap and map the index minH = i(map value) from the map and add points[minH] to the output array
	*/
	public int[][] kClosest(int[][] points, int k) {
		HashMap<Integer, Queue<Integer>> distanceDict = new HashMap<>();
		PriorityQueue<Integer> minHeap = new PriorityQueue<>();

		for (int i = 0; i < points.length; i++) {
			int[] point = points[i];
			Queue<Integer> values;
			int x = (int)Math.pow((0 - point[0]), 2);
			int y = (int)Math.pow((0 - point[1]), 2);
			int distance = x + y;

			if (distanceDict.containsKey(distance)) {
				values = distanceDict.get(distance);
			} else {
				values = new LinkedList<>();
			}
			values.add(i);

			distanceDict.put(distance, values);
			minHeap.add(distance);
		}

		ArrayList<int[]> res = new ArrayList<>();
		int index = k;
		Queue<Integer> values;
		while (index > 0) {
			int minValue = minHeap.poll();
			values = distanceDict.get(minValue);
			while(!values.isEmpty() && index > 0) {
				res.add(points[values.poll()]);
				index--;
			}
		}

		return res.toArray(new int[k][]);
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();
		Test tester = new Test();

		int[][] points = new int[][] {{1,3}, {-2,2}};
		int k = 1;
		int[][] res = obj.kClosest(points, k);
		// tester.assertEqual("Test case 1", Arrays.toString(res), Arrays.toString(new int[][] {{-2, 2}}));
		for (int[] point : res) {
			System.out.println(Arrays.toString(point));
		}

		points = new int[][] {{3,3}, {5,1}, {-2,4}};
		k = 2;
		res = obj.kClosest(points, k);
		// tester.assertEqual("Test case 1", Arrays.toString(res), Arrays.toString(new int[][] {{-2, 2}}));
		for (int[] point : res) {
			System.out.println(Arrays.toString(point));
		}

		points = new int[][] {{0,1}, {1,0}};
		k = 2;
		res = obj.kClosest(points, k);
		// tester.assertEqual("Test case 1", Arrays.toString(res), Arrays.toString(new int[][] {{-2, 2}}));
		for (int[] point : res) {
			System.out.println(Arrays.toString(point));
		}
	}
}