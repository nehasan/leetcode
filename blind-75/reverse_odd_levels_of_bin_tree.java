import java.util.*;

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode () {}
    TreeNode (int val) { this.val = val; }
    TreeNode (int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    /*
    * Approach, BFS traversal and read the data to stack
    * On the next level when level %2 == 0 and while processing the current node value then change node
    * value from the prevStack.pop()
    */
    public TreeNode reverseOddLevels(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        Stack<Integer> stack, prevStack;

        int level = 0;
        queue.add(root);
        stack = new Stack<>();
        prevStack = new Stack<>();
        stack.add(root.val);
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            stack = new Stack<>();
            while(levelSize-- > 0) {
                TreeNode currNode = queue.poll();
                if (currNode.left != null) {
                    queue.add(currNode.left);
                    stack.add(currNode.left.val);
                }
                if (currNode.right != null) {
                    queue.add(currNode.right);
                    stack.add(currNode.right.val);
                }
            
                if (!prevStack.isEmpty() && (level % 2 != 0)) {
                    currNode.val = prevStack.pop();
                }
            }

            prevStack = new Stack<>();
            for (int value : stack) {
                prevStack.push(value);
            }

            level++;
        }

        return root;
    }
}