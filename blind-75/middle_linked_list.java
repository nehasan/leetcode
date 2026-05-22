class ListNode {
	int val;
	ListNode next;
	
	ListNode(int val) {
		this.val = val;
	}
	ListNode(int val, ListNode next) {
		this.val = val;
		this.next = next;
	}
}

class Solution {
	/*
	public ListNode middleNode(ListNode head) {
		int size = 0;
		
		ListNode curr = head;
		while (curr != null) {
			size++;
			curr = curr.next;
		}
		
		if (size == 1 || size == 0) {
			return head;
		} else if (size == 2 || size == 3) {
			return head.next;
		}
		
		curr = head;
		int middle = size / 2;
		int index = 0;
		while (index < middle) {
			curr = curr.next;
			index++;
		}
		
		return curr;
	}*/
	
	public ListNode middleNode(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		} else if (head.next.next == null) {
			return head.next;
		}
	
		ListNode slow = head, fast = head;
	
		while (fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
	
		return slow;	
	}
}

class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();
		Test test = new Test();
		
		// Test case 1
		ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
		test.assertEqual("Test 1... ", obj.middleNode(head).val, 3);
		
		// Test case 2
		head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
		test.assertEqual("Test 2... ", obj.middleNode(head).val, 3);
		
		// Test case 2
		head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6))))));
		test.assertEqual("Test 3... ", obj.middleNode(head).val, 4);
	}
}