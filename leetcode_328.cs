using System;

public class ListNode {
	public int val;
  public ListNode next;
  public ListNode(int val = 0, ListNode next = null) {
    this.val = val;
    this.next = next;
  }
} 

public class Solution {

  public printList(ListNode head) {
    ListNode currNode = head;

    do {
      Console.WriteLine("print node : " + currNode);
      currNode = currNode.next;
    } while (currNode != null);
  }

  public ListNode OddEvenList(ListNode head) {
    ListNode oddBeg = head;
    ListNode evenBeg = head.next;
    ListNode oddCurr = head;
    ListNode evenCurr = head.next;

    while (evenCurr != null) {
      ListNode tempNode = evenCurr.next;
      if (tempNode == null) break;

      Console.Writeline("--- tempNode : " + tempNode.val);

      oddCurr.next = tempNode;
      Console.WriteLine("--- oddCurr.next : " + oddCurr.next.val);
      evenCurr.next = tempNode.next;
      Console.WriteLine("--- evenCurr.next : " + evenCurr.next.val);
      tempNode.next = evenBeg;
      Console.WriteLine("--- tempNode.next : " + tempNode.next.val);

      oddCurr = oddCurr.next;
      evenCurr = evenCurr.next;
    }

    printList(head);

    return head;
  }
};

public static void main() {
  ListNode head = new ListNode(1, new ListNode(2, new ListNode(3)));
  sln = new Solution();
  sln.OddEvenList(head);
}