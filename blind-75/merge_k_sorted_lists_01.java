// leetcode 23

import java.util.*;

class ListNode {
	int val;
	ListNode next;
	ListNode () {}
	ListNode (int val) {
		this.val = val;
	}
	ListNode (int val, ListNode next) {
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

	public String toString () {
		return "(val: " + this.val + ", index: " + this.index + ", node: " + this.node + ")";
	}
}

class Solution {
	public ListNode mergeKLists(ListNode[] lists) {

		ListNode dummy = new ListNode();
		PriorityQueue<NodeInfo> minHeap = new PriorityQueue<>();

		for (int i = 0; i < lists.length; i++) {
			ListNode node = lists[i];
			if (node != null) {
				minHeap.add(new NodeInfo(node.val, i, node));
			}
		}

		ListNode curr = dummy;
		while (!minHeap.isEmpty()) {
			// pop the top node
			NodeInfo topNode = minHeap.poll();
			System.out.println("node: " + topNode.val + " ");
			// include this topnode to the final answer list
			curr.next = new ListNode(topNode.val);
			curr = curr.next;
			// now add the next node of the topnode to the min heap
			if (topNode.node.next != null) {
				minHeap.add(new NodeInfo(topNode.node.next.val, topNode.index, topNode.node.next));
			}
		}

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