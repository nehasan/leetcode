// leetcode 127

import java.util.*;

class Solution {
	Solution() {}

	public boolean isOneDistance(String s1, String s2) {
		int changeCount = 0;

		for (int i = 0; i < s1.length(); i++) {
			if (s1.charAt(i) != s2.charAt(i)) {
				changeCount++;
			}
		}

		return changeCount == 1;
	}

	public List<String> findOneDistanceWords(String word, Set<String> wordSet) {
		List<String> words = new ArrayList<>();

		for (int i = 0; i < word.length(); i++) {
			StringBuilder tempWord = new StringBuilder(word);
			for (char c = 'a'; c <= 'z'; c++) {
				tempWord.setCharAt(i, c);
				if (wordSet.contains(tempWord.toString())) {
					words.add(tempWord.toString());
					wordSet.remove(tempWord.toString());
				}
			}
		}

		return words;
	}

	/*
	* Approach, find one distance words in the wordSet and BFS traverse through the 
	* one distance words to get to the desired word.
	* - Put the beginWord into the wordSet and simply return 0 if the endWord does not belong
	* to the wordSet
	* - Now start the BFS search starting with the beginWord and within the BFS search
	* try to find all the one distance words corresponding to the current processing word
	* - Suppose the word is hit, so now change each position of of the hit word with some a-z
	* character to see if those words exist in the wordSet. If those exist then put them
	* into queue for next processing and simply remove from the wordSet so that BFS does not pick those words again to process
	* - For example : word is hit -> [a-z]it words exist or h[a-z]t exist or hi[a-z] exist?
	* - Continue the process until we find the endWord
	* - However, the level can be calculated by simply storing the current level of the current processing word
	* - Suppose initially pathMap {hit: 1}
	* - Now oneDistanceWords found hot so the pathMap would be {hit: 1, hot:2}
	* - Again next oneDistanceWords found are dot and lot so the pathMap would be {hit:1, hot:2, dot:3, lot:3}
	* Time complexity: O(26*n*m) where n is the number of characters of a string (currWord) and m is the number of oneDistanceWords to be visited
	*/

	public int ladderLength(String beginWord, String endWord, List<String> wordList) {
		Set<String> wordSet = new HashSet<>();
		Set<String> visitSet = new HashSet<>();
		Queue<String> queue = new LinkedList<>();
		Map<String, Integer> transLength = new HashMap<>();
		Map<String, List<String>> oneDistanceGraph = new HashMap<>();

		for (String word: wordList) {
			wordSet.add(word);
		}

		if (!wordSet.contains(endWord)) {
			return 0;
		}

		wordSet.add(beginWord);
		queue.add(beginWord);
		transLength.put(beginWord, 1);
		transLength.put(endWord, Integer.MAX_VALUE);

		while (!queue.isEmpty()) {
			String currWord = queue.poll();
			wordSet.remove(currWord);

			List<String> oneDistanceWords = findOneDistanceWords(currWord, wordSet);

			for (String word : oneDistanceWords) {
				if (!visitSet.contains(word)) {
					if (word == endWord) {
						int prevLength = transLength.get(word);
						transLength.put(word, Math.min(prevLength, (transLength.get(currWord) + 1)));
					} else {
						transLength.put(word, transLength.get(currWord) + 1);
						queue.add(word);
					}
				}
			}

			visitSet.add(currWord);
		}

		int shortestLength = transLength.get(endWord);
		return shortestLength == Integer.MAX_VALUE ? 0 : shortestLength;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		String beginWord = "hit", endWord = "cog";
		String[] words = new String[] {"hot", "dot", "dog", "lot", "log", "cog"};

		// String beginWord = "hot", endWord = "dog";
		// String[] words = new String[] {"hot", "dog"};

		// String beginWord = "hot", endWord = "dog";
		// String[] words = new String[] {"hot", "dog", "dot"};

		List<String> wordList = new ArrayList<>(Arrays.asList(words));
		System.out.println(obj.ladderLength(beginWord, endWord, wordList));
	}
}