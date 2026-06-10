// leetcode 295

import java.util.*;

class MedianFinder {
	public PriorityQueue<Integer> minHeap;
	public PriorityQueue<Integer> maxHeap;

	public MedianFinder () {
		minHeap = new PriorityQueue<>();
		maxHeap = new PriorityQueue<>();
	}

	public void addNum(int num) {
		minHeap.add((-1 * num));

		if (!minHeap.isEmpty() && !maxHeap.isEmpty() && (-1 * minHeap.peek()) > maxHeap.peek()) {
			int val = -1 * minHeap.poll();
			maxHeap.add(val);
		}

		if (!minHeap.isEmpty() && (minHeap.size() - maxHeap.size()) > 1) {
			int val = -1 * minHeap.poll();
			maxHeap.add(val);
		}

		if (!maxHeap.isEmpty() && (maxHeap.size() - minHeap.size()) > 1) {
			int val = maxHeap.poll();
			minHeap.add((-1 * val));
		}
	}

	public double findMedian () {
		if (minHeap.size() > maxHeap.size()) {
			return (double)(-1 * minHeap.peek());
		} else if (maxHeap.size() > minHeap.size()) {
			return (double)(maxHeap.peek());
		} else {
			return (double) ((-1 * minHeap.peek()) + maxHeap.peek()) / 2.0;
		}
	}
}


class Main {
	public static void main(String[] args) {
		MedianFinder obj = new MedianFinder();

		String[] ops = {"MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"};
		int[][] values = {{}, {1}, {2}, {}, {3}, {}};

		List<Double> res = new ArrayList<>();
		int index = 0;
		for (String op : ops) {
			if (op.equals("addNum")) {
				obj.addNum(values[index][0]);
				res.add(null);
			} else if (op.equals("findMedian")) {
				double val = obj.findMedian();
				res.add(val);
			} 
			index++;
		}

		System.out.println(res);
	}
}