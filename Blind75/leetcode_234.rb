# 234. Palindrome Linked List

# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end

# @param {ListNode} head
# @return {Boolean}
def is_palindrome(head)
  return true if head.next.nil?

  slow = head
  fast = head
  stack = []

  while fast && fast.next
    stack.push(slow.val)
    slow = slow.next
    fast = fast.next.next
  end

  # move slow one step further if the length is odd
  slow = slow.next unless fast.nil?

  current = slow
  while current
    return false if current.val != stack.pop
    current = current.next
  end

  true
end

# head = ListNode.new(1)
# head.next = ListNode.new(2)
# head.next.next = ListNode.new(3)
# head.next.next.next = ListNode.new(4)
# head.next.next.next.next = ListNode.new(5)

# result = is_palindrome(head)
# puts result  # Output: false


# Example usage:
# Creating the linked list: 1 -> 2 -> 2 -> 1
head = ListNode.new(1)
head.next = ListNode.new(2)
head.next.next = ListNode.new(2)
head.next.next.next = ListNode.new(1)

# Calling the function
result = is_palindrome(head)
puts result  # Output: true

# Case 2:
# Creating the linked list: 1 -> 2
head2 = ListNode.new(1)
head2.next = ListNode.new(2)

# Calling the function
result2 = is_palindrome(head2)
puts result2  # Output: false

# Case 3:
# Creating the linked list: 1
# (single node)
head3 = ListNode.new(1)
result3 = is_palindrome(head3)
puts result3  # Output: true

# Case 4:
# Creating the linked list: 1 -> 0 -> 1
head4 = ListNode.new(1)
head4.next = ListNode.new(0)
head4.next.next = ListNode.new(1)

# Calling the function
result4 = is_palindrome(head4)
puts result4  # Output: true
