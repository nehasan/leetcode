# leetcode 23

from heapq import heappush, heappop

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeKLists(lists: List[ListNode]) -> ListNode:
		heap = []

		for i, node in enumerate(lists):
			if node:
				heappush(heap, (node.val, i, node))

		heappush(heap)

		D = ListNode()
		curr = D

		while heap:
			val, i, node = heappop(heap)
			curr.next = node
			curr = node
			node = node.next
			if node:
				heappush(heap, (node.val, i, node))


		return D.next

