'''
Docstring for Blind75.leetcode_234
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    Docstring for Solution
    Read the linked list into an array and then reverse the array to check for palindrome.
    '''
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     vals = []
    #     while head:
    #         vals.append(head.val)
    #         head = head.next
    #     return vals == vals[::-1]

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # move slow one step further if the length is odd
        slow = slow.next if not fast else slow

        current = slow
        while current:
            if stack.pop() != current.val:
                return False
            current = current.next
        
        return True
    
# Example usage:
sol = Solution()
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(sol.isPalindrome(head))  # Output: True

# Case 2:
# head = ListNode(1, ListNode(2))
print(sol.isPalindrome(head))  # Output: False

# Case 3:
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
print(sol.isPalindrome(head))  # Output: True

# Case 4:
# head = ListNode(1)
print(sol.isPalindrome(head))  # Output: True

# Case 5:
# head = ListNode(1, ListNode(0, ListNode(1)))
print(sol.isPalindrome(head))  # Output: True