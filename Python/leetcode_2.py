# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def printList(self, l):
        curr = l
        while True:
            print(curr.val)
            if curr.next is None:
                break
            curr = curr.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # stackOne = []
        # stackTwo = []
        
        # curr = l1
        # while True:
        #     stackOne.append(curr.val)
        #     if curr.next is None:
        #         break
        #     curr = curr.next
        
        # curr = l2
        # while True:
        #     stackTwo.append(curr.val)
        #     if curr.next is None:
        #         break
        #     curr = curr.next
        
        # maxLen = max(len(stackOne), len(stackTwo))

        sum = 0
        carry = 0
        currOne = l1
        currTwo = l2
        resList = None
        curr = None
        while True:

            if currOne is None and currTwo is None:
                break

            numOne = currOne.val if currOne else 0
            numTwo = currTwo.val if currTwo else 0

            # print(f"numOne: {numOne}, numTwo: {numTwo}")
            sum = numOne + numTwo + carry
            digit = sum % 10
            carry = int(sum / 10)

            # print(f"sum: {sum}, digit: {digit}, carry: {carry}")
            if resList is None:
                resList = ListNode(digit)
                curr = resList
            else:
                curr.next = ListNode(digit)
                curr = curr.next
            
            if currOne is not None and currOne.next:
                currOne = currOne.next
            else:
                currOne = None

            if currTwo is not None and currTwo.next:
                currTwo = currTwo.next
            else:
                currTwo = None
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        # self.printList(resList)
        return resList


soln = Solution()
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
# l1 = ListNode(2, ListNode(4, ListNode(9)))
# l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
soln.addTwoNumbers(l1, l2)