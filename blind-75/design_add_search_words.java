// leetcode 211

import java.util.*;

class TrieNode {
	Map<Character, TrieNode> children;
	boolean isWord;

	TrieNode () {
		children = new HashMap<>();
		isWord = false;
	}
}

class WordDictionary {
	TrieNode root;

	WordDictionary() {
		this.root = new TrieNode();
	}

	public void addWord(String word) {
		TrieNode currNode = this.root;

		for (int i = 0; i < word.length(); i++) {
			char c = word.charAt(i);
			if (currNode.children.containsKey(c)) {
				currNode = currNode.children.get(c);
			} else {
				TrieNode newNode = new TrieNode();
				currNode.children.put(c, newNode);
				currNode = newNode;
			}
		}
		currNode.isWord = true;
	}

	public boolean dfsSearch(String word, int index, TrieNode currNode) {
		if (index == word.length()) {
			return currNode.isWord;
		}

		char c = word.charAt(index);
		if (c == '.') {
			for(Map.Entry<Character, TrieNode> entry : currNode.children.entrySet()) {
				if (dfsSearch(word, index + 1, entry.getValue())) {
					return true;
				}
			}
		} else {
			if (currNode.children.containsKey(c)) {
				return dfsSearch(word, index + 1, currNode.children.get(c));
			}
		}
		return false;
	}

	public boolean search(String word) {
		if (!dfsSearch(word, 0, this.root)) {
			return false;
		}
		return true;
	}
}


class Main {
	public static void main(String[] args) {
		WordDictionary obj = new WordDictionary();
		// String[] ops = {"WordDictionary","addWord","addWord","addWord","search","search","search","search"};
		// String[][] values = {{""}, {"bad"}, {"dad"}, {"mad"}, {"pad"}, {"bad"}, {".ad"}, {"b.."}};

		String[] ops = {"WordDictionary","addWord","addWord","search","search","search","search","search","search"};
		String[][] values = {{""}, {"a"}, {"a"}, {"."}, {"a"}, {"aa"}, {"a"}, {".a"}, {"a."}};

		List<Boolean> res = new ArrayList<>();
		for (int i = 0; i < ops.length; i++) {
			if (ops[i] == "addWord") {
				obj.addWord(values[i][0]);
				res.add(null);
			} else if (ops[i] == "search") {
				res.add(obj.search(values[i][0]));
			} else {
				res.add(null);
			}
		}

		System.out.println(res);
	}
}