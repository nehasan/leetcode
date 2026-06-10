"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional

class Solution:
    nodeMap = dict()
    visitedMap = dict()

    def printGraph(self, node: Optional['Node']) -> None:
        if node:
            self.visitedMap.clear()
            q = deque()
            q.append(node)

            # print(f"neighbors: {[n.val if n else None for n in node.neighbors]}")
            while len(q) > 0:
                curr = q.popleft()

                print(f"Node: {curr.val}")
                print(f"Neighbors: ")
                for n in curr.neighbors:
                    print(f"{n.val} ")
                    if self.visitedMap.get(n.val) is None:
                        q.append(n)
                
                self.visitedMap[curr.val] = True
            
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def deepClone(node: Optional['Node']) -> Optional['Node']:
            q = deque()
            q.append(node)
            _node = Node(node.val)
            self.nodeMap[node.val] = _node
            newGraph = _node

            while len(q) > 0:
                currNode = q.popleft()
                print(f"current node val: {currNode.val}")
                _currNode = self.nodeMap[currNode.val]

                if self.visitedMap.get(currNode.val) is None:
                    for neighbor in currNode.neighbors:
                        print(f"next neighbor to be queued: {neighbor.val}")
                        q.append(neighbor)

                        _neighbor = None
                        if self.nodeMap.get(neighbor.val) is None:
                            self.nodeMap[neighbor.val] = Node(neighbor.val)
                        
                        _neighbor = self.nodeMap[neighbor.val]
                        _currNode.neighbors.append(_neighbor)
                        
                    
                    self.visitedMap[currNode.val] = True
            
            return newGraph
        
        if node is None:
            return None
        if node.neighbors == []:
            return Node(node.val)
        graph = deepClone(node)
        self.printGraph(graph)
        return graph

soln = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# node1.neighbors = [node2, node4]
# node2.neighbors = [node1, node3]
# node3.neighbors = [node2, node4]
# node4.neighbors = [node1, node3]

node1.neighbors = [node2]
node2.neighbors = [node1]

soln.cloneGraph(node1)