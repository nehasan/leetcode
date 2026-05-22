import java.util.*;

class Solution {
	public List<String> topKFrequent(String[] words, int k) {
		Map<String, Integer> countMapper = new HashMap<>();
		Map<Integer, PriorityQueue<String>> wordMapper = new HashMap<>();
		PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
		List<String> res = new ArrayList<>();

		for (String word: words) {
			countMapper.put(word, countMapper.getOrDefault(word, 0) + 1);
		}

		for (Map.Entry<String, Integer> entry : countMapper.entrySet()) {
			if (!wordMapper.containsKey(entry.getValue())) {
				maxHeap.add((0 - entry.getValue()));
			}
			PriorityQueue<String> wordQ = wordMapper.getOrDefault(entry.getValue(), new PriorityQueue<>());
			wordQ.add(entry.getKey());
			wordMapper.put(entry.getValue(), wordQ);
		}

		System.out.println(countMapper);
		System.out.println(wordMapper);

		while (k-- > 0) {
			int currCount = (0 - maxHeap.poll());
			System.out.println("currCount: " + currCount);
			Queue<String> wordQ = wordMapper.get(currCount);
			// Collections.sort(wordQ);
			System.out.println(wordQ);
			do {
				System.out.println("k is: " + k);
				System.out.println("wordQ peek " + wordQ.peek());
				res.add(wordQ.poll());
			} while (!wordQ.isEmpty() && k-- > 0);
		}

		return res;
	}
}


class Main {
	public static void main (String[] args) {
		Solution obj = new Solution();

		String[] words = new String[] {"i", "love", "leetcode", "i", "love", "coding"};
		int k = 3;
		List<String> topFreqWords = obj.topKFrequent(words, k);
		System.out.println(Arrays.toString(topFreqWords.toArray()));


		words = new String[] {"the","day","is","sunny","the","the","the","sunny","is","is"};
		k = 4;
		topFreqWords = obj.topKFrequent(words, k);
		System.out.println(Arrays.toString(topFreqWords.toArray()));
	}
}