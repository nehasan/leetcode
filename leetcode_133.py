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

from typing import Optional
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def printGraph(node: Optional['Node'], visited) -> None:
            if node:
                if node.val not in visited:
                    print(f"Node: {node.val}")
                    visited[node.val] = True
                    for nei in node.neighbors:
                        print(f"Nei: {nei.val}")
                    for nei in node.neighbors:
                        printGraph(nei, visited)
        
        def deepClone(node: Optional['Node'], nodeMapper: defaultdict, visited: defaultdict) -> Optional['Node']:
            if node:
                # If node is not visited already then process it first and then return
                if node.val not in visited:
                    _node = None
                    
                    if nodeMapper.get(node.val) is None:
                        nodeMapper[node.val] = Node(node.val)
                    
                    _node = nodeMapper[node.val]
                    visited[node.val] = True
                    
                    for nei in node.neighbors:
                        # Build the neighbors recursively
                        _node.neighbors.append(deepClone(nei, nodeMapper, visited))
                    
                    # Return the processed node
                    return _node
                
                # If already visited then return the stored node directly
                return nodeMapper[node.val]
            
            return None
        
        if not node:
            return node
        if len(node.neighbors) == 0:
            return Node(node.val)
        
        nodeMapper = defaultdict(Node)
        visited = defaultdict(bool)
        # graph = deepClone(node, nodeMapper, visited)
        # visited.clear()
        # printGraph(graph, visited)
        # return graph
        return deepClone(node, nodeMapper, visited)
        

obj = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

obj.cloneGraph(node1)