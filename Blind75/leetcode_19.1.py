class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def printList(self, head: Optional[ListNode]) -> None:
        curr = head
        while curr:
            print(f"curr.val {curr.val}")
            curr = curr.next
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next
        
        print(f"size: {size}")
        if size == n:
            # self.printList(head.next)
            return head.next

        curr = head
        nth = 0
        while curr:
            nth += 1
            if nth == size - n:
                curr.next = curr.next.next
                break

            curr = curr.next
        
        # self.printList(head)
        return head

obj = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# obj.removeNthFromEnd(head, 1)
# obj.removeNthFromEnd(head, 5)
head = ListNode(1, ListNode(2))
# obj.removeNthFromEnd(head, 1)
obj.removeNthFromEnd(head, 2)