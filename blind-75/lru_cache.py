# leetcode 146

from collections import defaultdict


class Node:
	def __init__(self, key=0, value=0, prev=None, next=None):
		self.key = key
		self.value = value
		self.prev = prev
		self.next = next


'''
Design approach, using double ended linked list
We maintain one hashmap (basically a node map dict[key] = Node) and a double ended
linked list to implement LRU cache.
Everytime we find a new key will be added to a hashmap and a that hash key usually points to a
node of the linked list we maintain.
Suppose [key=1, val=1] is added then cache[1] = Node(1, 1) will be added inside the
head and tail node. Head and tail are two dummy nodes to reach to the front and end of the linkedlist with 0(1) time
So the linkedlist will be: 
head <-> node(1) <-> tail
Now we add [key=2, val=2] then the linkedlist will be:
head <-> node(2) <-> node(1) <-> tail
We add the new node always at the head or if we fetch a key we simply remove the node from the list and
take back to the front.
Now if we fetch the node(1) the the updated list will be:
head <-> node(1) <-> node(2) <-> tail.
In case the linkedlist exceeds the capacity then we simply remove the tail node (which is least used node) from the list and create a new
one at the front
So the design paradigm of the LRU cache is, any node is added or updated or fetched should be
moved to the front of the list and always remove the tail node incase it exceeds capacity.
'''
class LRUCache:

	def __init__(self, capacity: int):
		self.capacity = capacity
		self.cache = dict()
		self.size = len(self.cache)

		self.head = Node()
		self.tail = Node()

		self.head.next = self.tail
		self.tail.prev = self.head

	def printList(self) -> None:
		# slow, fast = self.head, self.head
		# while fast and fast.next:
		# 	print(f"key: {slow.key}, val: {slow.value}")
		# 	slow = slow.next
		# 	fast = fast.next.next
		# 	if slow == fast:
		# 		break

		curr = self.head
		while curr:
			curr = curr.next

	def add(self, node: Node) -> None:
		headNext = self.head.next
		self.head.next = node
		node.prev = self.head
		node.next = headNext
		headNext.prev = node

	def remove(self, node: Node) -> None:
		prev_node = node.prev
		next_node = node.next

		prev_node.next = next_node
		next_node.prev = prev_node

	def getSize(self) -> int:
		return self.size

	def updateSize(self) -> None:
		self.size = len(self.cache)

	def get(self, key: int) -> int:
		node = self.cache.get(key)

		if node:
			self.remove(node)
			self.add(node)

			return node.value
		else:
			return -1


	def put(self, key: int, value: int) -> None:
		node = self.cache.get(key)

		if node:
			self.remove(node)
			node.value = value
			self.add(node)
			# self.printList()
		else:
			if (self.getSize() == self.capacity):
				tailKey = self.tail.prev.key
				self.cache.pop(tailKey)
				self.remove(self.tail.prev)

			newNode = Node(key, value)
			self.cache[key] = newNode
			self.add(newNode)
			self.updateSize()

			# self.printList()


obj = None

# ops = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

ops = ["LRUCache","put","put","get","put","put","get"]
values = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

res = []
for index, op in enumerate(ops):
	if op == "LRUCache":
		obj = LRUCache(values[index][0])
		res.append(None)
	elif op == "get":
		res.append(obj.get(values[index][0]))
	elif op == "put":
		obj.put(values[index][0], values[index][1])
		res.append(None)

print(res)