// leetcode 3

import java.util.*;

class Solution {
	public int lengthOfLongestSubstring(String s) {
		int left = 0, right = 0;
		int longest = 0;
		Set<Character> charSet = new HashSet<>();

		while (right < s.length()) {
			char currChar = s.charAt(right);

			if (charSet.contains(currChar)) {
				while (left < right) {
					if (s.charAt(left) == s.charAt(right)) {
						left++;
						break;
					}
					charSet.remove(s.charAt(left));
					left++;
				}
			} else {
				charSet.add(currChar);
				longest = Math.max(longest, (right - left) + 1);
			}

			right++;
		}

		return longest;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		String s = "abcabcbb";
		System.out.println(obj.lengthOfLongestSubstring(s));

		s = "bbbbbb";
		System.out.println(obj.lengthOfLongestSubstring(s));

		s = "pwwkew";
		System.out.println(obj.lengthOfLongestSubstring(s));
	}
}