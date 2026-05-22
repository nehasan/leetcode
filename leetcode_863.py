'''
Leetcode 863. All Nodes Distance K in Binary Tree
Nahid Hasan Khan
'''

'''
Approach: Algorithm uses two tree data structures DFS and BFS to solve this problem.
In this problem looks like one needs to traverse from one node to other nodes,
    possibly going through the root node to the otherside of the tree. However,
    this binary tree is omnidirectional and first of all we need to convert this whole
    tree into a graph making it a bidirectional traversal
- Apply recursive DFS starting from the root node and map all the connected nodes attached to any
    single node
- After that apply BFS on the mapped hashtable (graph) to calculate the distance of the other nodes
    can be reached from the target node. If the distance equals to the current node then insert that
    node to the output list.
'''

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graphMap = {}
          
        def dfs(node: TreeNode, parent: TreeNode):
            '''
            Returns None
            Arguments:
            node - current node to be processed, must be a TreeNode
            parent - parent node of the current node to be enlisted as a connected node, must be a TreeNode
            '''
            if not node:
                return None

            value = node.val
            print(node.val)
      
            # if the value is not found in map, initialize it
            if value not in graphMap:
                graphMap[value] = []
      
            # if parent is present then include it as a connected one
            if parent:
                graphMap[value].append(parent.val)
      
            # traverse child nodes to build a bidirectional graph
            for child in [node.left, node.right]:
                if child:
                    graphMap[value].append(child.val)
                dfs(child, node)

        def bfs(node: int) -> List[int]:
            # maintain a queue to processe next node in the queue for BFS
            queue = [node]
            # maintain a set to include visited node and not to visit again
            visited = set()
            # maintain distance map to identify distance for each node from target node
            distanceMap = dict()
    
            visited.add(node)
            distanceMap[node] = 0
            output = []
          
            if k == 0:
                return [node]
              
            while queue:
                # get the nodes connected with the first node in the queue
                nodes = graphMap.get(queue[0], [])
              
                # get the current node value for distance calculation
                currNode = queue.pop(0)
              
                # traverse each nodes to enqueue nodes connected to them for further processing
                for n in nodes:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)
                      
                        # distance of the node n is always +1 of its parent (currentNode) node
                        distanceMap[n] = distanceMap[currNode] + 1
                      
                        # if distance of node n == k then include it into the final output list
                        if distanceMap[n] == k:
                              output.append(n)

            return output

        dfs(root, None)
        print(graphMap)
        return bfs(target.val)


def main():
  root = TreeNode(
      3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
      TreeNode(1, TreeNode(0), TreeNode(8)))
  
  # sample input #1
  # output: [1, 7, 4]
  target = root.left
  k = 2 # pass
  
  # sample input #2
  # output: [0, 8] 
  # target = root.left
  # k = 3 # pass
  
  # sample input #3
  # output: [7,4]
  # target = root.right.left
  # k = 5 # pass

  obj = Solution()
  print(obj.distanceK(root, target, k))


if __name__ == "__main__":
  main()
