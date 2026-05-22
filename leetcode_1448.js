// Leetcode 1448 Count The Good Nodes of A Binary Tree
// Author: Nahid Hasan Khan

/**
 * Class definition of TreeNode
 */

class TreeNode {
    constructor (val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

/**
 * Algorithm utilizes DFS approach to count good nodes from the top root node
 * In each path to a targeted node we simply inject maximum value which has been\
    	calculated so far to check whether the next node value is greater or less
 * If the next node value (either left or right) is less then we simply ignore the\
    	current node value by adding 0 with the rest
 * If the next node value (...) is greater then we add 1 + rest
 */

/**
 * @param {TreeNode} root
 * @return {number}
 */
var goodNodes = function(root) {
    return checkNextGood(root.left, root.val) + checkNextGood(root.right, root.val) + 1;
};

const checkNextGood = (node, maxValue) => {
    if (node != null) {
		let nextMaxVal = Math.max(maxValue, node.val);
		
        if (node.val < maxValue) {
        	return checkNextGood(node.left, nextMaxVal) + checkNextGood(node.right, nextMaxVal);
        } else {
			return checkNextGood(node.left, nextMaxVal) + checkNextGood(node.right, nextMaxVal) + 1;
        }
    }
	
    return 0;
}

// sample root = [3, 1, 4, 3, null, 1, 5]
// output: 4 // passed
// const root = new TreeNode(
//     3,
//     new TreeNode(1, new TreeNode(3), null),
//     new TreeNode(4, new TreeNode(1), new TreeNode(5))
// )


// sample root = [3, 3, null, 4, 2]
// output: 3 // passed
// const root = new TreeNode(
//     3,
//     new TreeNode(
//         3,
//         new TreeNode(4),
//         new TreeNode(2)
//     ),
//     null
// )

// sample root = [1]
// output: 1 // passed
// const root = new TreeNode(1)

// sample root = [9, null, 3, 6, null]
// output: 1 // passed
const root = new TreeNode(
    9,
    null,
    new TreeNode(
        3,
        new TreeNode(6),
		   null
    )
);

console.log(goodNodes(root));