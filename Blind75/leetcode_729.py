from typing import List, Optional

class ListNode:
    def __init__(self, val: List[int], next = None ):
        self.val = val
        self.next = next

class MyCalendar:

    def __init__(self):
        self.head = None

    def printBookList(self, head: ListNode) -> None:
        curr = head
        while curr:
            print(f"node -> [start, end]: [{curr.val[0]}, {curr.val[1]}]")
            curr = curr.next

    '''
    Algorithm: Return false if the new interval cannot be added into the right position of the sorted list, else add the interval based on the suitable position
    Time complexity O(n), need to traverse through the linked list to find the suitable position or return false if cannot be added
    '''
    def book(self, startTime: int, endTime: int) -> bool:
        curr = self.head

        # insert it at the head if head is null
        if curr is None:
            self.head = ListNode([startTime, endTime])
            self.printBookList(self.head)
            return True
        
        # check if the head conflicts with the new interval
        if curr.val[0] <= startTime and curr.val[1] > startTime:
            return False
        
        # insert the node at the begining if the value is small
        if curr.val[0] >= endTime:
            tempNode = self.head
            self.head = ListNode([startTime, endTime], tempNode)
            self.printBookList(self.head)
            return True
        
        prev = None
        while curr:
            currStartTime = curr.val[0]
            currEndTime   = curr.val[1]
            nextStartTime = curr.next.val[0] if curr.next else -1
            if currEndTime <= startTime and nextStartTime >= endTime:
                break
            if currStartTime > startTime and currStartTime >= endTime:
                break
            if currEndTime > startTime:
                return False

            prev = curr
            curr = curr.next
        
        # Now insert between prev and curr
        if curr is None:
            prev.next = ListNode([startTime, endTime])
        else:
            tempNode = curr.next
            newNode = ListNode([startTime, endTime], tempNode)
            curr.next = newNode

        self.printBookList(self.head)
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

obj = MyCalendar()
# print(obj.book(10, 20))
# print(obj.book(15, 21))
# print(obj.book(15, 19))
# print(obj.book(20, 25))

# print(obj.book(1, 2))
# print(obj.book(1, 2))
# print(obj.book(2, 5))
# print(obj.book(10, 15))
# print(obj.book(11, 15))
# print(obj.book(15, 20))

# ops = ["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
# inputs = [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
# ops = ["MyCalendar", "book", "book", "book"]
# inputs = [[], [10, 20], [15, 25], [20, 30]]
# ops = ["MyCalendar","book","book","book","book","book"]
# inputs = [[],[37,50],[33,50],[4,17],[35,48],[8,25]]
# ops = ["MyCalendar","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
# inputs = [[],[20,29],[13,22],[44,50],[1,7],[2,10],[14,20],[19,25],[36,42],[45,50],[47,50],[39,45],[44,50],[16,25],[45,50],[45,50],[12,20],[21,29],[11,20],[12,17],[34,40],[10,18],[38,44],[23,32],[38,44],[15,20],[27,33],[34,42],[44,50],[35,40],[24,31]]
ops = ["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
inputs = [[],[48,50],[0,6],[6,13],[8,13],[15,23],[49,50],[45,50],[29,34],[3,12],[38,44]]
outputs = []

for i, x in enumerate(ops):
    if x == "book":
        print(f"input: [{inputs[i][0]}, {inputs[i][1]}]")
        outputs.append(obj.book(inputs[i][0], inputs[i][1]))
        print("\n")
    else:
        outputs.append([])

print(outputs)