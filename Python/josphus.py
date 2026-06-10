'''
Author: Nahid Hasan Khan
Solved josephus problem
Problem url: https://www.cut-the-knot.org/recurrence/flavius.shtml
Algorithm used doubly linked list here that deals with the problem, and the problem\
    identifies itself as a node deletion process within a list of nodes
'''

from typing import List

class Node:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Josephus:
    def solve(self, soldiers: List[int], step) -> int:

        # prints doubly linked list
        def printNodes(head):
            slow = head
            fast = head.next

            while slow != fast:
                print(slow.val)
                slow = slow.next
                fast = fast.next.next
            print(slow.val)
        
        # build doubly linked list
        head = None
        curr = None

        for i in soldiers:
            if head == None:
               head = Node(i)
               curr = head
            else:
                tempNode = Node(i, curr)
                curr.next = tempNode
                curr = curr.next
        
        curr.next = head
        head.prev = curr

        printNodes(head)

        currOne = head
        print(f'--- DEBUG previous node of head (to confirm doubly linked list) {head.prev.val}')

        # loop keeps going until current node points to itself as next
        while currOne.next != currOne:
            remove = currOne
            for i in range(step - 1):
                remove = remove.next
            
            # node deletion process happens here
            prev = remove.prev
            nextNext = remove.next
            prev.next = nextNext
            nextNext.prev = prev
            print(f'--- DEBUG deleted node {remove.val}')

            currOne = prev
        
        return currOne.val

josephus = Josephus()
# print(josephus.solve([1, 2, 3, 4, 5, 6, 7], 2))
# print(josephus.solve([1, 2, 3, 4, 5], 2))
print(josephus.solve([1, 2, 3, 4, 5, 6, 7], 3))


