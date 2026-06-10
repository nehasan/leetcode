#include <iostream>
#include <string>
#include <stack>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
#include <sstream>
#include <memory>
#include <map>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    TreeNode(int x, TreeNode *leftNode, TreeNode *rightNode) : val(x), left(leftNode), right(rightNode) {}
};

class Codec
{
public:
    std::string
    onesComplement(int binary[])
    {
        std::string res;

        for (int i = 0; i < 8; i++)
        {
            res += std::to_string(binary[i] == 1 ? 0 : 1);
        }

        // std::cout << res << std::endl;
        return res;
    }

    std::string
    numberToBinary(int num)
    {
        int tempNum = abs(num);
        // std::cout << tempNum << std::endl;
        std::string res;
        std::stack<int> digits;

        do
        {
            int rem = tempNum % 2;
            tempNum /= 2;
            // std::cout << rem << std::endl;
            digits.push(rem);
        } while (tempNum > 0);

        // int len = sizeof(digits) / sizeof(digits[0]);
        int len = digits.size();
        // std::cout << "len " << len << std::endl;
        int binary[8];
        memset(binary, 0, sizeof(binary));
        for (int i = 8 - len; i < 8; i++)
        {
            binary[i] = digits.top();
            digits.pop();
        }

        for (int n : binary)
        {
            // std::cout << n << std::endl;
            res += std::to_string(n);
        }
        // std::cout << res << std::endl;
        return num > 0 ? res : onesComplement(binary);
    }

    int binaryToNumber(std::string s)
    {
        int len = s.size();
        // std::cout << len << std::endl;
        int num = 0;

        int n = 0;
        for (int i = len - 1; i >= 0; i--)
        {
            // std::cout << (s[i] - '0') << std::endl;
            num += (pow(2, n) * (s[i] - '0'));
            // std::cout << "num: " << num << ", n: " << n << ", i: " << i << std::endl;
            n++;
        }

        // std::cout << num << std::endl;
        return num;
    }

    std::string serialize(TreeNode *root)
    {
        std::string res;
        std::queue<TreeNode *> q;
        q.push(root);
        std::set<int> visited;

        while (q.size() > 0)
        {
            TreeNode *curr = q.front();
            q.pop();

            if (curr == NULL)
            {
                // std::cout << "NULL ptr found" << std::endl;
                res += (res == "" ? ("11111111") : (" 11111111"));
            }
            else
            {
                // std::cout << curr->val << std::endl;
                res += (res == "" ? numberToBinary(curr->val) : (" " + numberToBinary(curr->val)));

                q.push(curr->left);
                q.push(curr->right);
            }
        }

        std::cout << "serialized: " << res << std::endl;
        return res;
    }

    TreeNode *buildTree(int index, std::vector<std::string> tokens, std::map<int, TreeNode *> nodeMap)
    {
        TreeNode *root = NULL;
        if (index >= tokens.size() || tokens[index] == "11111111")
        {
            return NULL;
        }

        int rootValue = binaryToNumber(tokens[index]);
        if (nodeMap.count(rootValue) > 0)
        {
            root = nodeMap[rootValue];
        }
        else
        {
            root = new TreeNode(rootValue);
            // root->val = rootValue;
            nodeMap[rootValue] = root;
        }

        root->left = buildTree(2 * index + 1, tokens, nodeMap);
        root->right = buildTree(2 * index + 2, tokens, nodeMap);

        return root;
    }

    TreeNode *deserialize(std::string s)
    {
        std::istringstream iss(s);
        std::string token;
        std::vector<std::string> tokens;
        std::map<int, TreeNode *> nodeMap;

        while (iss >> token)
        {
            tokens.push_back(token);
        }

        TreeNode *root = buildTree(0, tokens, nodeMap);

        return root;
    }
};

int main()
{
    // int n = 16;
    // int n = -5;
    // numberToBinary(n);
    // std::string s = "00000101";
    // binaryToNumber(s);

    // TreeNode *node2 = new TreeNode();
    // node2->val = 2;
    // node2->left = NULL;
    // node2->right = NULL;

    // TreeNode *node3 = new TreeNode();
    // node3->val = 3;
    // node3->left = NULL;
    // node3->right = NULL;

    // TreeNode *root = new TreeNode();
    // root->val = 1;
    // root->left = node2;
    // root->right = node3;

    // std::cout << serialize(root) << std::endl;

    Codec ser, deser;

    // std::string text = "00000001 00000010 00000011 11111111 11111111 11111111 11111111";
    // TreeNode *root = deser.deserialize(text);
    // std::cout << ser.serialize(root) << std::endl;
    // TreeNode *root = new TreeNode(
    //     1,
    //     TreeNode(2),
    //     TreeNode(
    //         3,
    //         TreeNode(4),
    //         TreeNode(5)));
    TreeNode *root = new TreeNode(1);
    TreeNode *node2 = new TreeNode(2);
    TreeNode *node3 = new TreeNode(3);
    TreeNode *node4 = new TreeNode(4);
    TreeNode *node5 = new TreeNode(5);

    root->left = node2;
    root->right = node3;

    node3->left = node4;
    node3->right = node5;

    std::cout << deser.deserialize(ser.serialize(root)) << std::endl;
    return 0;
}