# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = slow
        if slow is None:
            return False
        
        while True:
            slow = slow.next
            if fast and fast.next and fast.next.next:
                fast = fast.next.next
            else:
                fast = None
            
            if slow is None or fast is None:
                break
            if slow == fast:
                return True
        
        return False


soln = Solution()
# head = ListNode(3)
# node1 = ListNode(2)
# node2 = ListNode(0)
# node3 = ListNode(-4)

# head.next = node1
# node1.next = node2
# node2.next = node3
# node3.next = node1

# head = ListNode(1)
# node1 = ListNode(2)
# head.next = node1
# node1.next = head

# head = ListNode(1)

# head = ListNode(1)
# node1 = ListNode(2)
# node2 = ListNode(3)
# head.next = node1
# node1.next = node2

head = None
print(soln.hasCycle(head))