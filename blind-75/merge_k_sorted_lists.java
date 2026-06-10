// leetcode 23

import java.util.*;

class ListNode {
	int val;
	ListNode next;

	ListNode() {}
	ListNode(int val) { this.val = val; }
	ListNode(int val, ListNode next) {
		this.val = val;
		this.next = next;
	}
}

class NodeInfo implements Comparable<NodeInfo> {
	int val;
	int index;
	ListNode node;

	NodeInfo (int val, int index, ListNode node) {
		this.val = val;
		this.index = index;
		this.node = node;
	}

	@Override
	public int compareTo(NodeInfo other) {
		if (this.val == other.val) {
			return Integer.compare(this.index, other.index);
		}
		return Integer.compare(this.val, other.val);
	}

	public String toString() {
		return this.val + " " + this.index + " " + this.node;
	}
}

class Solution {
	public void printList(ListNode node) {
		ListNode curr = node;
		while (curr != null) {
			System.out.print(curr.val + " ");
			curr = curr.next;
		}
	}

	/*
	* Approach, using min heap (priority queue)
	* Initially every first node of each list are added to the heap for example, for the example
	* data it has [[1,4,5], [1,3,5], [2,6]]. Now the heap becomes
	* [1,0]
	* |  		\
	* [1,1] [2,2] Storing the index is required, because what if two nodes gets same value
	* As we storing a complex value here, a comparable class is required to compare the values in the heap tree 
	* Now until the heap becomes empty we pop the heap, record the node value to our final
	* result node, make the node as current and set the node.next as the node of this current node.
	* Then we push these values (as new nodeInfo) to the heap if the nodeInfo.node is not null
	* Time complexity O(Nlog n) where n is the number of ListNodes present and logn for the heap manipulation
	* Space complexity O(N + K), N is the number of list nodes, K is the number nodes in the heap tree
	* The process:
	* [1,0]						[1,1]					[2,2]					[3,1]
	* |			\			 -> |			\		 -> |		 \		 -> |		 \
	* [1,1]	 [2,2]		[2,2]	[4,0]		[3,1]	[4,0]		[4,0] [5,0] .. so on.
	* The heap always mains K items in the tree
	*/

	public ListNode mergeKLists(ListNode[] lists) {
		PriorityQueue<NodeInfo> heap = new PriorityQueue<>();

		for (int i = 0; i < lists.length; i++) {
			ListNode node = lists[i];
			if (node != null) {
				heap.add(new NodeInfo(node.val, i, node));
			}
		}

		ListNode dummy = new ListNode();
		ListNode curr = dummy;

		while(!heap.isEmpty()) {
			NodeInfo nodeInfo = heap.poll();
			System.out.println("current nodeInfo " + nodeInfo);
			curr.next = nodeInfo.node;
			curr = nodeInfo.node;
			nodeInfo.node = nodeInfo.node.next;

			if (nodeInfo.node != null) {
				heap.add(new NodeInfo(nodeInfo.node.val, nodeInfo.index, nodeInfo.node));
			}
		}

		// printList(dummy.next);
		return dummy.next;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		ListNode[] lists = new ListNode[] {
			new ListNode(1, new ListNode(4, new ListNode(5))),
			new ListNode(1, new ListNode(3, new ListNode(4))),
			new ListNode(2, new ListNode(6))
		};

		System.out.println(obj.mergeKLists(lists));
	}
}