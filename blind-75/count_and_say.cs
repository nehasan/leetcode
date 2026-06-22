using System;
using System.Collections.Generic;

public class Solution {
	public string CountAndSay(int n) {
		List<string> rle = new List<string>();
		List<string> tempList = new List<string>{ "1" };

		for (int i = 0; i < n; i++) {
			string curr = "";
			foreach (string s in tempList) {
				curr += s;
			}

			// insert every finalized string to final string list RLE
			rle.Add(curr);
			
			char prev = curr[0];
			int count = 1;
			tempList.Clear();
			for (int j = 1; j < curr.Count(); j++) {
				if (curr[j] == prev) {
					count++;
				} else {
					tempList.Add(count.ToString() + prev.ToString());
					prev = curr[j];
					count = 1;
				}
			}

			// if count is not 0 that means we have some string left to be considered
			if (count > 0) {
				tempList.Add(count.ToString() + prev.ToString());
			}
		}

		return rle[n - 1];
	}
}

public class Program {
	static void Main (string[] args) {
		Solution obj = new Solution();

		Console.WriteLine(obj.CountAndSay(4));
		Console.WriteLine(obj.CountAndSay(1));
		Console.WriteLine(obj.CountAndSay(5));
	}
}