
// leetcode 61

using System;

public class ListNode {
    public int val;
    public ListNode next;
    Public ListNode (int val=0, ListNode next=null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode RotateRight(ListNode head, int k) {
        if (head == null) return head;

        int nodeSize = 0;
        ListNode curr = head;
        while (curr != null) {
            nodeSize++;
            curr = curr.next;
        }

        if (k == nodeSize) return head;

        if (k > nodeSize) {
            k = k % nodeSize;
        }

        while (k-- > 0) {
            curr = head.next;
            int prevNum = head.val;
            while (curr != null) {
                int tempNum = curr.val;
                curr.val = prevNum;
                prevNum = tempNum;
                curr = curr.next;
            }
            head.val = prevNum;
        }

        // printList(head);
        return head;
    }

    private void printList(ListNode head) {
        ListNode curr = head;
        while (curr != null) {
            Console.WriteLine(curr.val);
            curr = curr.next;
        }
    }
}