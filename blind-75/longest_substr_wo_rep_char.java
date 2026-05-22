import java.util.*;

class Solution {
	int lengthOfLongestSubstring (String s) {
		Set<Character> set = new HashSet<>();

		int lPtr = 0, rPtr = 0, maxLength = 0;

		while (lPtr < s.length() && rPtr < s.length()) {
			char c = s.charAt(rPtr);

			if (set.contains(c)) {
				while (s.charAt(lPtr) != s.charAt(rPtr)) {
					if (set.contains(s.charAt(lPtr))) {
						set.remove(s.charAt(lPtr));
					}
					lPtr++;
				}
				lPtr++;
			} else {
				set.add(c);
				maxLength = Math.max(maxLength, (rPtr - lPtr) + 1);
			}
			rPtr++;
		}

		return maxLength;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();
		Test tester = new Test();

		String s = new String("abcabcbb");
		tester.assertEqual("Test case 1", obj.lengthOfLongestSubstring(s), 3);

		s = new String("bbbbb");
		tester.assertEqual("Test case 2", obj.lengthOfLongestSubstring(s), 1);

		s = new String("pwwkew");
		tester.assertEqual("Test case 3", obj.lengthOfLongestSubstring(s), 3);

		s = new String("dvdf");
		tester.assertEqual("Test case 4", obj.lengthOfLongestSubstring(s), 3);
	}
}