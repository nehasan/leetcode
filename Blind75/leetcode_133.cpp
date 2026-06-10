#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <set>

class Node
{
public:
    int val;
    std::vector<Node *> neighbors;

    Node()
    {
        this->val = 0;
        this->neighbors = std::vector<Node *>();
    }

    Node(int val)
    {
        this->val = val;
        this->neighbors = std::vector<Node *>();
    }

    Node(int val, std::vector<Node *> neighbors)
    {
        this->val = val;
        this->neighbors = neighbors;
    }
};

class Solution
{
public:
    void printGraph(Node *node)
    {
        std::set<int> visited;
        std::queue<Node *> q;
        q.push(node);

        while (q.size() > 0)
        {
            Node *curr = q.front();
            q.pop();

            std::cout << "curr node:" << curr->val << std::endl;
            if (visited.count(curr->val) == 0)
            {
                std::vector<Node *> neighbors = curr->neighbors;
                std::cout << "neighbors: ";
                // for (auto it = neighbors.begin(); it != neighbors.end(); ++it)
                // {
                //     std::cout << it->val << " ";
                //     std::cout << *it << "";
                //     zsq.push(it);
                // }
                for (Node *neighbor : neighbors)
                {
                    std::cout << neighbor->val << " ";
                    // std::cout <<  << "";
                    q.push(neighbor);
                }
                std::cout << std::endl;
                visited.insert(curr->val);
            }
        }
    }

    Node *clone(Node *node)
    {
        std::map<int, Node *> nodeMap;
        std::set<int> visited;
        std::queue<Node *> q;
        q.push(node);

        Node *_node = new Node(node->val);
        nodeMap[node->val] = _node;

        while (q.size() > 0)
        {
            Node *currNode = q.front();
            q.pop();
            Node *_currNode = nodeMap[currNode->val];

            if (visited.count(currNode->val) == 0)
            {
                std::vector<Node *> neighbors = currNode->neighbors;
                for (Node *neighbor : neighbors)
                {
                    q.push(neighbor);
                    if (nodeMap.count(neighbor->val) == 0)
                    {
                        nodeMap[neighbor->val] = new Node(neighbor->val);
                    }
                    _currNode->neighbors.push_back(nodeMap[neighbor->val]);
                }

                visited.insert(currNode->val);
            }
        }

        return _node;
    }

    Node *cloneGraph(Node *node)
    {
        if (node == nullptr)
        {
            return nullptr;
        }

        if (node->neighbors.size() == 0)
        {
            return new Node(node->val);
        }

        Node *cloned = clone(node);
        printGraph(cloned);
        return cloned;
        // return clone(node);
    }
};

int main()
{
    Node *node1 = new Node(1);
    Node *node2 = new Node(2);
    Node *node3 = new Node(3);
    Node *node4 = new Node(4);

    node1->neighbors.push_back(node2);
    node1->neighbors.push_back(node4);

    node2->neighbors.push_back(node1);
    node2->neighbors.push_back(node3);

    node3->neighbors.push_back(node2);
    node3->neighbors.push_back(node4);

    node4->neighbors.push_back(node1);
    node4->neighbors.push_back(node3);

    Solution soln;
    soln.cloneGraph(node1);
    return 0;
}