# Definition for singly-linked list.
from typing import Optional
from typing import Dict

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    '''
    Approach 1: Using SET to keep track of the visited nodes
    Does not meet O(1) memory limit requirement
    '''
    # def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head: return
    #     visited = set()
    #     curr = head
        
    #     while True:
    #         if not curr: break
    #         if curr in visited:
    #             return curr
            
    #         visited.add(curr)
    #         curr = curr.next
        
    #     return
    
    '''
    Approach 2: Using slow - runner technique
    Using slow runner technique find and stop in the slow node when slow == fast
    Now take slow2 = head and this time when slow == slow2 then that slow is the starter of the cycle
    '''
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        
        if not fast.next or not fast.next.next: return
        
        slow2 = head
        while slow.next:
            if slow == slow2: return slow
            slow = slow.next
            slow2 = slow2.next
        
        return
        

sol = Solution()

# node3 = ListNode(-4)
# node2 = ListNode(0)
# node1 = ListNode(2)
# head = ListNode(3)
# head.next = node1
# node1.next = node2
# node2.next = node3
# node3.next = node1
# print(sol.detectCycle(head).val) # Output 2

# node1 = ListNode(2)
# head = ListNode(1)
# head.next = node1
# node1.next = head
# print(sol.detectCycle(head).val) # Output 1

# head = ListNode(1) # Output False
# print(sol.detectCycle(head).val) # Output None

node1 = ListNode(2)
head = ListNode(1)
head.next = node1
print(sol.detectCycle(head).val) # Output None