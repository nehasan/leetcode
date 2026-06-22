// leetcode 68

using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> FullJustify(string[] words, int maxWidth) {
        Queue<string> queue = new Queue<string>();
        foreach (string word in words) {
            queue.Enqueue(word);
        }

        IList<string> res = new List<string>();
        List<List<string>> tempList = new List<List<string>>();
        List<string> currWordList = new List<string>();

        int currTextLength = 0;
        string nextWord = null;
        while (queue.Count() > 0) {
            nextWord = queue.Dequeue();
            if ((currTextLength + nextWord.Count() + currWordList.Count()) > maxWidth) {
                // then enlist the curr word list for final processing
                tempList.Add(currWordList);
                currWordList = new List<string>();
                
                // then start again for the next line
                currWordList.Add(nextWord);
                currTextLength = nextWord.Count();
            } else if ((currTextLength + nextWord.Count() + currWordList.Count()) == maxWidth) {
                currWordList.Add(nextWord);
                tempList.Add(currWordList);
                currWordList = new List<string>();
                currTextLength = 0;
            } else {
                currWordList.Add(nextWord);
                currTextLength += nextWord.Count();
            }
        }

        if (currWordList.Count() > 0) {
            tempList.Add(currWordList);
        }

        for (int i = 0; i < tempList.Count(); i++) {
            if (i == (tempList.Count() - 1)) {
                res.Add(ApplyJustification(tempList[i], maxWidth, true));
            } else {
                res.Add(ApplyJustification(tempList[i], maxWidth));
            }
        }

        // foreach (string s in res) {
        // 	Console.WriteLine(s);
        // }
        return res;
    }

    private string ApplyJustification(List<string> words, int maxWidth, bool lastLine=false) {
        int currCharSize = 0;
        foreach (string s in words) {
            currCharSize += s.Count();
        }

        int charDiff = maxWidth - currCharSize;

        // for last line it is a bit tricky process, for first n - 1 words
        // we put a single space and for the last one we space it until it reaches maxWidth
        if (lastLine) {
        	int wordSize = words.Count();
        	for (int i = 0; i < wordSize - 1; i++) {
        		words[i] = words[i] + " ";
        		charDiff--;
        		if (charDiff == 0) break;
        	}
        	while (charDiff > 0) {
        		words[wordSize - 1] = words[wordSize - 1] + " ";
        		charDiff--;
        	}
        // except last line we always space the first word and rest of the words, then we
        // iterate the whole process again until it reaches maxWidth
        } else {
        	while (charDiff > 0) {
	        	int wordSize = words.Count();
	        	// space the first word always
	        	words[0] = words[0] + " ";
	        	charDiff--;
	        	if (charDiff <= 0) break;
	        	// space the rest of the words until before the last one
	            for (int i = 1; i < wordSize - 1; i++) {
	                words[i] = words[i] + " ";
	                charDiff--;
	                if (charDiff <= 0) break;
	            }
	        }
        }

        return string.Join("", words);
    }
}

public class Program {
	static void Main (string[] args) {
		Solution obj = new Solution();

		// string[] words = new string[] {"This", "is", "an", "example", "of", "text", "justification."};
		// Console.WriteLine(obj.FullJustify(words, 16).ToString());

		// string[] words = new string[] {"What", "must", "be", "acknowledgment", "shall", "be"};
		// Console.WriteLine(obj.FullJustify(words, 16));
		
		string[] words = new string[] {"Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"};
		Console.WriteLine(obj.FullJustify(words, 20));
	}
}