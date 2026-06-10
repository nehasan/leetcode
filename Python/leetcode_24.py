# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def printList(self, head: Optional[ListNode]) -> None:
        curr = head
        while True:
            if curr is None:
                break

            print(curr.val)
            curr = curr.next
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while True:
            if curr is None or curr.next is None:
                break

            tempVal = curr.next.val
            curr.next.val = curr.val
            curr.val = tempVal

            curr = curr.next.next

        self.printList(head)
        return head


soln = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# head = ListNode(1, ListNode(2, ListNode(3)))
# head = None
soln.swapPairs(head)