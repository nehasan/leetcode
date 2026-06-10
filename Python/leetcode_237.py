from typing import Any, List


class ListNode:
    def __init__(self, val: int, next = None) -> None:
        self.val = val
        self.next = next
    


class Solution:
    def __init__(self, head: ListNode) -> None:
        self.head = head

    def printNode(self):
        curr = self.head
        while curr.next != None:
            print(curr.val)
            curr = curr.next

    def deleteNode(self, node: ListNode) -> ListNode:
        def try_or(fn, default):
            try:
                return fn()
            except:
                return default

        slow = self.head
        fast = self.head.next.next

        if fast == None:
            return self.head.next

        while slow.next != None:
            if slow.next.val == node.val:
                slow.next = fast
                self.printNode()
                return self.head
            
            slow = slow.next
            fast = try_or(fast.next.next, None)


node7 = ListNode(7)
node6 = ListNode(6, node7)
node5 = ListNode(5, node6)
head = ListNode(4, node5)


# head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
print(head.next.next.val)

obj = Solution(head)
obj.deleteNode(node6)