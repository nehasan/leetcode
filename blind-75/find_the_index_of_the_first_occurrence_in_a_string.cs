// leetcode 28

using System;

public class Solution {
	public int StrStr(string haystack, string needle) {
		for(int i = 0; i < haystack.Count(); i++) {
			if(haystack[i] == needle[0]) {
				int firstIndex = i;
				int lenNeedle = needle.Count();
				if ((i + (lenNeedle - 1)) < haystack.Count()) {
					if (haystack.Substring(i, lenNeedle).Equals(needle)) {
						return firstIndex;
					}
				}
			}
		}
		return -1;
	}
}

public class Program {
	static void Main (string[] args) {
		Solution soln = new Solution();

		Console.WriteLine(soln.StrStr("sadbutsad", "sad")); // 0
		Console.WriteLine(soln.StrStr("sabbutsad", "sad")); // 6
		Console.WriteLine(soln.StrStr("leetcode", "leeto")); // -1
		Console.WriteLine(soln.StrStr("aaa", "aaaa")); // -1
	} 
}