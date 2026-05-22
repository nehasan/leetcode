'''
Solution uses linkedin list.
Time complexity O(n)
Time limit exceeds

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None
    

class MedianFinder:
    def __init__(self):
        self.size = 0
        self.head = None
        
    def printList(self) -> None:
        curr = self.head
        while curr:
            print(f"- node: {curr.val}")
            curr = curr.next
    
    def addNum(self, num : int) -> None:
        curr = self.head
        
        # when head is null then simply add the new num to head
        if curr is None:
            self.head = ListNode(num)
            self.size += 1
            self.printList()
            
            return
            
        # when num is smaller than head
        if curr.val > num:
            tempNode = ListNode(num)
            tempNode.next = curr
            self.head = tempNode
            self.size += 1
            self.printList()
            
            return
            
        # when head is an only node
        if curr.next is None and curr.val <= num:
            curr.next = ListNode(num)
            self.size += 1
            self.printList()
            
            return
        
        prev = None
        while curr:
            if curr.val > num:
                break
            prev = curr
            curr = curr.next
        
        if curr is None:
            prev.next = ListNode(num)
        else:
            tempNode = curr
            prev.next = ListNode(num)
            prev.next.next = tempNode
        
        self.printList()
        self.size += 1

    
    def findMedian(self) -> float:
        curr = self.head
        totalElm = self.size
        # print(f"totalElm: {totalElm}")
        
        if totalElm == 1:
            return float(curr.val)
        if totalElm == 2:
            return (curr.val + curr.next.val) / 2.0
        
        fastIndex = 1
        while fastIndex < int(totalElm / 2.0):
            curr = curr.next
            
            fastIndex += 1
            # print(f"fastIndex now: {fastIndex}")
        
        if totalElm % 2 == 0:
            # print(f"curr.val: {curr.val}, curr.next.val: {curr.next.val}")
            return (curr.val + curr.next.val) / 2.0
        else:
            return float(curr.next.val)

'''
from heapq import heappush, heappop


'''
Approach using min and max heap
- Two heaps will be maintained minHeap and maxHeap
minHeap contains values anything less than or equal to maxHeap for example mnH = [3,4,5]
maxHeap contains values strictly larger or equal to minHeap for example mxH = [7,8,9]

- During insert op, usually a number will be added to minHeap, and then if we see len difference is more than 1 then
we shift one to maxHeap for example mnH = [-5, -4], mxH = [], then heappush(mxH, -1 * heappop(mnH))
results in mnH = [-4], mxH = [5].
opposite operation will be conducted if maxHeap has len difference 2
another checking is required in case of any value in minHeap is bigger than maxHeap, for example, mnH = [-7,-4], mxH = [5],
in this case we need the same operation to transfer the max of the min heap to the max heap, heappush(mxH, -1 * heappop(mnH))
push or pop complexity is alway O(logn) in heap

- Now for findMedian operation which is always O(1) operation, in case different length always return from the max lengthed heap
in case of equal length always takes from both heap and diveided by 2, ( - 1 * mnH[0]) + mxH[0] / 2.0
'''
class MedianFinder:

    def __init__(self):
        self.minHeap = [] # but will be used as max heap [-4, -2, -1]
        self.maxHeap = [] # but will be used as min heap [5, 6, 7]
        self.lenMinHeap = 0
        self.lenMaxHeap = 0

    def addNum(self, num: int) -> None:
        heappush(self.minHeap, -1 * num)
        self.lenMinHeap += 1
        
        # make sure every num in min heap is <= every num in max heap
        if (self.lenMinHeap > 0 and self.lenMaxHeap > 0) and ((-1 * self.minHeap[0]) > self.maxHeap[0]):
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -1 * val)
            self.lenMinHeap -= 1
            self.lenMaxHeap += 1
        
        # make sure len difference is ~ 1, otherwise exchange
        if self.lenMinHeap > self.lenMaxHeap and (self.lenMinHeap - self.lenMaxHeap) > 1:
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -1 * val)
            self.lenMinHeap -= 1
            self.lenMaxHeap += 1
        
        if self.lenMaxHeap > self.lenMinHeap and (self.lenMaxHeap - self.lenMinHeap) > 1:
            val = heappop(self.maxHeap)
            heappush(self.minHeap, -1 * val)
            self.lenMaxHeap -= 1
            self.lenMinHeap += 1

    def findMedian(self) -> float:
        if self.lenMinHeap > self.lenMaxHeap:
            return float(-1 * self.minHeap[0])
        elif self.lenMinHeap < self.lenMaxHeap:
            return float(self.maxHeap[0])
        else:
            return ((-1 * self.minHeap[0]) + self.maxHeap[0]) / 2.0
            
            
            
obj = MedianFinder()
ops = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
values = [[], [1], [2], [], [3], []] # passed
values = [[], [3], [2], [], [1], []] # passed
values = [[], [2], [1], [], [3], []] # passed

ops = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
values = [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]

ops = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
values = [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[],[-6],[]]

ops = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
values = [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[],[-6],[],[-7],[]]

ops = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
values = [[],[1],[],[2],[],[3],[],[4],[],[5],[],[6],[],[7],[],[8],[],[9],[],[10],[]]

index = 0
res = []
for op in ops:
    if op == "findMedian":
        res.append(obj.findMedian())
    elif op == "addNum":
        obj.addNum(values[index][0])
        res.append(None)
    else:
        res.append(None)
    
    index += 1

print(res)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        