// Leet code 2095 Delete Middle Node of A Linked List
// Oct 14th 2023, Nahid Hasan Khan

class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

/**
 * Algorithm uses hash map to store the information of each list node
 * Initialize the list size with one and as we move forward iterating over the list node
 * we keep tracking the size and store the current node into hashmap by its position set(size/pos, nodeInfo)
 * Then we calculate middle and connect the next node of the middle to previous of the middle node.
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    if (head == null) return head;

    let size = 1;
    let nodeMap = new Map();

    let curr = head;
    // insert the first node to nodeMap
    nodeMap.set(size, curr);

    // counting size and storing nodes to nodeMap
    while (curr.next !== null) {
        size++;
        curr = curr.next;
        nodeMap.set(size, curr);
    }

    // console.log(size);
    curr = head;

    if (size == 1) {
        // if the list has only 1 nodes
        return null;
    } else if (size == 2) {
        // if the list has only 2 nodes
        curr.next = null;
        // printList(curr);
        return curr;
    } else {
        // fore nodes more than 3
        let middle = Math.floor(size / 2);
        nodeMap.get(middle).next = nodeMap.get(middle + 2);

        // printList(head);
        return head;
    }

};

const getNextFastPointer = (node) => {
    try {
        console.log('HERE1');
        return node.next.next
    } catch (error) {
        try {
            console.log('HERE2');
            return node.next
        } catch (error) {
            return null
        }
    }
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const deleteMiddle2 = (head) => {
    if (head == null) return null;
    if (head.next.next == null) {
        head.next = null;
        // printList(head);
        return head;
    }

    let preMiddle = head;
    let slowPointer = head;
    let fastPointer = head;

    while (fastPointer.next && fastPointer.next.next) {
        preMiddle = slowPointer;
        slowPointer = slowPointer.next;
        fastPointer = fastPointer.next.next;
    }
    
    // do {
    //     preMiddle = slowPointer;
    //     slowPointer = slowPointer.next;
    //     fastPointer = getNextFastPointer(fastPointer);
    // } while (fastPointer != null || fastPointer != undefined);

    preMiddle.next = slowPointer.next;

    printList(head);
    return head;
}

var printList = (head) => {
    let curr = head;

    do {
        console.log(curr.val);
        if (curr.next == null) break;
        curr = curr.next;
    } while (true);

    // while(curr.next != null) {
    //     console.log(curr.val);
    //     curr = curr.next;
    // }
}

// head = new ListNode(1);
// head = new ListNode(1, new ListNode(2));
// head = new ListNode(2, new ListNode(3, new ListNode(4)));
head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))))
// head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))))
// head = new ListNode(
//     1, new ListNode(
//         3, new ListNode(
//             4, new ListNode(
//                 7, new ListNode(
//                     1, new ListNode(
//                         4, new ListNode(
//                             6, new ListNode(8, null)
//                         )
//                     )
//                 )
//             )
//         )
//     )
// )

// console.log(deleteMiddle(head));
// deleteMiddle(head);
deleteMiddle2(head);