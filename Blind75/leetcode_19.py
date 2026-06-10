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
            print(curr.val)
            if curr.next is None:
                break
            curr = curr.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while True:
            size += 1
            if curr.next is None:
                break
            curr = curr.next

        print(f'size: {size}, n: {n}')
        if size == n:
            # self.printList(head.next)
            return head.next
        
        i = 0
        nth = size - n
        curr = head

        while True:
            i += 1
            if i == nth:
                curr.next = curr.next.next
                break

            curr = curr.next
        
        # self.printList(head)
        return head

soln = Solution()
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# head = ListNode(1, ListNode(2))
head = ListNode(1)
soln.removeNthFromEnd(head, 1)