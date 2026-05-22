import sys
from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, listOne: Optional[ListNode], listTwo: Optional[ListNode]) -> Optional[ListNode]:

        def printList(head: ListNode) -> None:
            curr = head
            while curr.next != None:
                print(curr.val)
                curr = curr.next

        def getListLength(head: ListNode) -> int:
            if head == None:
                return 0
            else:
                len = 1
                curr = head
                while curr.next != None:
                    len += 1
                    curr = curr.next
                
                return len
        
        arr = []
        currOne = listOne
        currTwo = listTwo
        head = None
        tail = None

        while currOne != None or currTwo != None:
            numOne = sys.maxsize if currOne == None else currOne.val
            numTwo = sys.maxsize if currTwo == None else currTwo.val

            print(f'--- DEBUG numOne: {numOne}, numTwo: {numTwo}')
            if numOne < numTwo:
                print(f'--- DEBUG numOne: {numOne} < numTwo: {numTwo}')
                arr.append(numOne)
                tempNode = ListNode(numOne)
                if head == None:
                    head = tempNode
                    tail = head
                else:
                    tail.next = tempNode
                    tail = tail.next

                currOne = currOne.next
            elif numTwo < numOne:
                print(f'--- DEBUG numOne: {numOne} > numTwo: {numTwo}')
                arr.append(numTwo)
                tempNode = ListNode(numTwo)
                if head == None:
                    head = tempNode
                    tail = head
                else:
                    tail.next = tempNode
                    tail = tail.next
                currTwo = currTwo.next
            
            elif numOne == numTwo:
                print(f'--- DEBUG numOne: {numOne} == numTwo: {numTwo}')
                arr.append(numOne)
                arr.append(numTwo)
                tempNode = ListNode(numOne, ListNode(numTwo))
                if head == None:
                    head = tempNode
                    tail = head
                else:
                    tail.next = tempNode
                    tail = tail.next

                currOne = currOne.next
                currTwo = currTwo.next
        
        print(arr)
        printList(head)
        return head


obj = Solution()
list1 = None
# list1 = ListNode(4, ListNode(6, ListNode(6, ListNode(9, ListNode(9)))))
list2 = ListNode(5, ListNode(6, ListNode(10)))

obj.mergeTwoLists(list1, list2)
