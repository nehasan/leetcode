# leetcode 23

from typing import List, Optional
from heapq import heappush, heappop

class ListNode:
	def __init__(self, val = 0, next = None ):
		self.val = val
		self.next = next

class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		minHeap = []

		# include each first node of the list to heap
		for i, node in enumerate(lists):
			if node:
				heappush(minHeap, (node.val, i, node))

		dummy = ListNode()

		curr = dummy

		while(len(minHeap) > 0):
			# pop the top info of the heap that represents the smallest node
			topNode = heappop(minHeap)
			# print(f"node val: {topNode[0]}")

			# include the smallest node to the final list
			curr.next = ListNode(topNode[0])
			curr = curr.next

			# if the top of the heap has next node then set that node to the next
			if topNode[2].next:
				heappush(minHeap, (topNode[2].next.val, topNode[1], topNode[2].next))

		return dummy.next



obj = Solution()

lists = [
	ListNode(1, ListNode(4, ListNode(5))),
	ListNode(1, ListNode(3, ListNode(4))),
	ListNode(2, ListNode(6))
]

obj.mergeKLists(lists)
