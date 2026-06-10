// leetcode 647

import java.util.*;

class Solution {
	private int findAndCountPalindromic(String s, boolean oddPalindorme) {
		int count = 0;

		int startingAt = 0;
		while(startingAt < s.length()) {
			int low = startingAt;
			int high = oddPalindorme ? startingAt : startingAt + 1;

			while (low >= 0 && high < s.length()) {
				if (s.charAt(low) != s.charAt(high)) break;

				System.out.println("plaindrome found : low: " + low + " high: " + high + " " + s.substring(low, high));
				count++;
				low--;
				high++;
			}

			startingAt++;
		}

		return count;
	}

	public int countSubstrings(String s) {
		int totalSubstrings = 0;

		totalSubstrings = findAndCountPalindromic(s, true);
		totalSubstrings += findAndCountPalindromic(s, false);

		return totalSubstrings;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		String s = "abc";
		System.out.println(obj.countSubstrings(s));

		s = "aaa";
		System.out.println(obj.countSubstrings(s));

		s = "a";
		System.out.println(obj.countSubstrings(s));
	}
}