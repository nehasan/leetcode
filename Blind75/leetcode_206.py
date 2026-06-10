# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def printList(self, head) -> None:
        curr = head
        while True:
            if curr is None:
                break
            print(curr.val)
            curr = curr.next
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
            
        stack = []
        curr = head
        while True:
            if curr is None:
                break
            stack.append(curr.val)
            curr = curr.next
        
        res = ListNode()
        curr = res
        print(stack)
        while True:
            curr.val = stack.pop()
            if len(stack) == 0:
                break
            curr.next = ListNode()
            curr = curr.next
        
        # self.printList(res)

        return res


soln = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(soln.reverseList(head))