// leetcode 424

import java.util.*;

class Solution {
	class MostFrequent {
		public char ch;
		public int frequency;

		MostFrequent() {}
		MostFrequent(char ch, int frequency) {
			this.ch = ch;
			this.frequency = frequency;
		}

		public String toString() {
			return "(" + ch + " " + frequency + ")";
		}
	}

	public int characterReplacement(String s, int k) {
		int longestLength = 0;
		int left = 0, right = 0;
		Map<Character, Integer> charFrequency = new HashMap<>();
		MostFrequent mostFreq = null;

		while(right < s.length()) {
			char ch = s.charAt(right);
			charFrequency.put(ch, charFrequency.getOrDefault(ch, 0) + 1);
			
			if (mostFreq == null) {
				mostFreq = new MostFrequent(ch, 1);
			} else {
				int currCharFreq = charFrequency.getOrDefault(ch, 0);
				if (mostFreq.frequency <= currCharFreq) {
					mostFreq.ch = ch;
					mostFreq.frequency = currCharFreq;
				}
			}
			// System.out.println("left : " + left + " right : " + right + " mostFreq " + mostFreq);

			int currWinLen = (right - left) + 1;
			if ((currWinLen - mostFreq.frequency) <= k) {
				longestLength = Math.max(longestLength, currWinLen);
			} else {
				do {
					int maxFreq = 0;
					char leftChar = s.charAt(left);
					charFrequency.put(leftChar, charFrequency.get(leftChar) - 1);

					// after the above change most freq can be changed so update it again
					for (Map.Entry<Character, Integer> entry : charFrequency.entrySet()) {
						if (entry.getValue() >= maxFreq) {
							mostFreq.ch = entry.getKey();
							mostFreq.frequency = entry.getValue();
							maxFreq = entry.getValue();
						}
					}
					left++;
					currWinLen = (right - left) + 1;
					// System.out.println("current charFrequency " + charFrequency);
					// System.out.println("window was invalid, shrinking left and updating mostFreq " + " left : " + left + " right " + right + " mostFreq " + mostFreq);
				} while ((currWinLen - mostFreq.frequency) > k);
			}

			right++;
		}

		return longestLength;
    }
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		System.out.println(obj.characterReplacement(new String("ABAB"), 2));
		System.out.println(obj.characterReplacement(new String("AABABBA"), 1));
	}
}