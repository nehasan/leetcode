// leetcode 133

import java.util.*;

class Node {
	int val;
	List<Node> neighbors;

	Node () {
		this.val = 0;
		this.neighbors = new ArrayList<Node>();
	}
	Node (int val) {
		this.val = val;
		this.neighbors = new ArrayList<Node>();
	}
	Node (int val, ArrayList<Node> neighbors) {
		this.val = val;
		this.neighbors = neighbors;
	}
}


class Solution {
	public void printNodes (Node node) {
		Set<Integer> visited = new HashSet<>();
		Queue<Node> q = new LinkedList<>();
		q.add(node);

		while(!q.isEmpty()) {
			Node currNode = q.poll();
			System.out.print("parent: " + currNode.val);

			if (!visited.contains(currNode.val)) {
				for(Node nei : currNode.neighbors) {
					System.out.print("children: " + nei.val + " ");
					q.add(nei);
				}
				visited.add(currNode.val);
			}
		}

	}

	public Node deepClone (Node node, Map<Integer, Node> nodeMap) {
		if (node != null) {
			
			if (nodeMap.containsKey(node.val)) {
				return nodeMap.get(node.val);
			} else {
				Node newNode = new Node(node.val);
				nodeMap.put(node.val, newNode);

				for (Node nei : node.neighbors) {
					newNode.neighbors.add(deepClone(nei, nodeMap));
				}

				return newNode;
			}
		}

		return null;
	}

	public Node cloneGraph (Node node) {
		Map<Integer, Node> nodeMap = new HashMap<>();

		// Node n = deepClone(node, nodeMap);
		// printNodes(n);
		return deepClone(node, nodeMap);
	}
}



class Main {
	public static void main (String[] args) {
		Solution obj = new Solution();
		Node node1 = new Node(1);
		Node node2 = new Node(2);
		Node node3 = new Node(3);
		Node node4 = new Node(4);

		node1.neighbors.add(node2);
		node1.neighbors.add(node4);

		node2.neighbors.add(node1);
		node2.neighbors.add(node3);

		node3.neighbors.add(node2);
		node3.neighbors.add(node4);

		node4.neighbors.add(node1);
		node4.neighbors.add(node3);

		obj.cloneGraph(node1);
	}
}