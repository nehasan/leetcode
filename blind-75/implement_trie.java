// leetcode 208

import java.util.*;

class TrieNode {
	Map<Character, TrieNode> children;
	boolean isWord;

	TrieNode () {
		this.children = new HashMap<Character, TrieNode>();
		this.isWord = false;
	}

	TrieNode (HashMap<Character, TrieNode> children, boolean isWord) {
		this.children = children;
	}
}

class Trie {

	TrieNode root;

	Trie () {
		this.root = new TrieNode();
	}

	public void insert (String word) {
		TrieNode currNode = this.root;

		for (int i = 0; i < word.length(); i++) {
			char c = word.charAt(i);
			
			if (currNode.children.containsKey(c)) {
				currNode = currNode.children.get(c);
			} else {
				TrieNode newNode = new TrieNode();
				currNode.children.put(c, newNode);
				currNode = currNode.children.get(c);
			}
		}

		currNode.isWord = true;
	}

	public boolean search (String word) {
		TrieNode currNode = this.root;

		for (int i = 0; i < word.length(); i++) {
			char c = word.charAt(i);
			
			System.out.println("curr node's children " + currNode.children);
			System.out.println("looking for char " + c);
			if (currNode.children.containsKey(c)) {
				System.out.println("char is found in the children ");
				currNode = currNode.children.get(c);
			} else {
				System.out.println("char is not found returning false ");
				return false;
			}
		}

		System.out.println("all char is found and the isWord is " + currNode.isWord);
		return currNode.isWord;
	}

	public boolean startsWith (String prefix) {
		TrieNode currNode = this.root;

		for (int i = 0; i < prefix.length(); i++) {
			char c = prefix.charAt(i);
			
			if (currNode.children.containsKey(c)) {
				currNode = currNode.children.get(c);
			} else {
				return false;
			}
		}

		return true;
	}
}


class Main {
	public static void main (String[] args) {
		Trie obj = null;
		String[] ops = new String[] {"Trie", "insert", "search", "search", "startsWith", "insert", "search"};
		String [][] values = new String[][] {{""}, {"apple"}, {"apple"}, {"app"}, {"app"}, {"app"}, {"app"}};
		List<Boolean> out = new ArrayList<Boolean>();

		for (int i = 0; i < ops.length; i++) {
			switch (ops[i]) {
				case "Trie":
					obj = new Trie();
					out.add(null);
					break;
				case "insert":
					if (obj == null) {
						obj = new Trie();
					}
					obj.insert(values[i][0]);
					out.add(null);
					break;
				case "search":
					if (obj == null) {
						obj = new Trie();
					}
					out.add(obj.search(values[i][0]));
					break;
				case "startsWith":
					if (obj == null) {
						obj = new Trie();
					}
					out.add(obj.startsWith(values[i][0]));
					break;
			}
		}

		System.out.println(out);
	}
}