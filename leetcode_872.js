// Leet code 872 Similar Leaf
// Oct 09 2023 By Nahid Hasan Khan

/**
 * Definition for a binary tree node.
 */

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        // this.val = (val === undefined ? 0 : val);
        // this.left = (left === undefined ? null : left);
        // this.right = (right === undefined ? null : right);
        this.val = val;
        this.left = left;
        this.right = right;
    }

    static printTree = (node) => {
        if (node !== null) {
            console.log(node.val);
            this.printTree(node.left);
            this.printTree(node.right);
        }
    }
}

/** 
 * Algorithm recursive pre order tree traverse
 * Check if the node has no left and right node, means a leaf
 * Collect all the leafs for tree 1 and tree 2 and later match the string created
 *  from those leafs
*/

/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {
    let leafsOne = [];
    let leafsTwo = [];

    // traverse the trees and collect the leaf nodes
    preOrderTraverse(root1, leafsOne);
    preOrderTraverse(root2, leafsTwo);

    console.log(leafsOne);
    console.log(leafsTwo);

    // check if the two array have same contents
    if (leafsOne.length != leafsTwo.length) return false;

    for (var i = 0; i < leafsOne.length; i++) {
        if (leafsOne[i] != leafsTwo[i]) return false;
    }

    return true;
};

const preOrderTraverse = (node, leafs) => {
    if (node !== null) {
        if (node.left == null && node.right == null) {
            leafs.push(node.val);
        }

        preOrderTraverse(node.left, leafs);
        preOrderTraverse(node.right, leafs);
    }
}

const root1 = new TreeNode(1, new TreeNode(2, null, null), new TreeNode(4));
const root2 = new TreeNode(1, new TreeNode(2, null, null), new TreeNode(3, null, null));

console.log(leafSimilar(root1, root2));
// TreeNode.printTree(root1);