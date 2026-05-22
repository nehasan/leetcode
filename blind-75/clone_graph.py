# leetcode 133

from typing import List, Optional
from collections import defaultdict
from collections import deque

class Node:
	def __init__(self, val=0, neighbors=[]):
		self.val = val
		self.neighbors = neighbors

class Solution:

	def printGraph(self, node: Optional[Node]) -> None:
		q = deque()
		s = set()
		q.append(node)

		while len(q) > 0:
			curr = q.popleft()
			print(f"parent: {curr.val} ")

			if curr.val not in s:
				for nei in curr.neighbors:
					print(f"child: {nei.val} ")
					q.append(nei)

			s.add(curr.val)

	def deepClone(self, node: Optional[Node], nodeDict: defaultdict) -> Optional[Node]:
		if node:
			if node.val in nodeDict:
				print(f"node exists : {node.val}")
				return nodeDict[node.val]
			else:
				print(f"cr node : {node.val}")
				newNode = Node(node.val)
				nodeDict[node.val] = newNode

				for nei in node.neighbors:
					print(f"node {node.val}, cr child {nei.val}")
					newNode.neighbors.append(self.deepClone(nei, nodeDict))
					print(f"- - - node {node.val}, cr child {nei.val} assigned")

				return newNode
		else:
			return None

	def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
		nodeDict = defaultdict(Node)

		cloned = self.deepClone(node, nodeDict)
		# self.printGraph(cloned)
		return None
		# return self.deepClone(node, nodeDict)


obj = Solution()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# node1.neighbors = [node2]
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

obj.cloneGraph(node1)
