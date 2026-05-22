# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        if head.next is None: return False
        
        slow = head
        fast = head.next.next
        cycle = False
        
        while True:
            if slow is None or fast is None: break
            if fast and fast.next is None: break
            if slow == fast:
                cycle = True
                break
            slow = slow.next
            fast = fast.next.next
        
        return cycle

# Example use cases
sol = Solution()
# node3 = ListNode(-4)
# node2 = ListNode(0)
# node1 = ListNode(2)
# head = ListNode(3)
# head.next = node1
# node1.next = node2
# node2.next = node3
# node3.next = node1 # Output True

# node1 = ListNode(2)
# head = ListNode(1)
# head.next = node1
# node1.next = head # Output True

# head = ListNode(1) # Output False

node1 = ListNode(2)
head = ListNode(1)
head.next = node1

print(sol.hasCycle(head))