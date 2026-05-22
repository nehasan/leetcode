# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def printList(head: Optional[ListNode]) -> None:
            curr = head
            while curr:
                print(f"{curr.val}")
                curr = curr.next
            
        def recursiveReverse(prevNode: Optional[ListNode], currNode: Optional[ListNode]) -> Optional[ListNode]:
            # Need to implement later
            return None
        
        def iterativeReverse(head: Optional[ListNode]) -> Optional[ListNode]:
            curr = head
            stack = []
            
            while curr:
                stack.append(curr.val)
                # print(f"curr.val: {curr.val}")
                curr = curr.next
            
            res = ListNode(stack.pop())
            curr = res
            while len(stack) > 0:
                newNode = ListNode(stack.pop())
                curr.next = newNode
                curr = curr.next

            return res
            
                   
        if not head or head.next is None: return head
        # recursiveReverse(head, head.next)
        resultHead = iterativeReverse(head)
        printList(resultHead)
        return resultHead
        
        # curr = head
        # res = None
        # while curr:
        #     if res is None:
        #         res = curr
        #         res = res.next
        #         curr = curr.next
        
        # return res
        

sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol.reverseList(head)