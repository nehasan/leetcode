# Definition for singly-linked list.

class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end

# @param {ListNode} head
# @return {Integer}
def pair_sum(head)
    max_sum = 0
    slow = head
    fast = head
    stack = []

    while fast && fast.next
        stack.push(slow.val)
        slow = slow.next
        fast = fast.next.next
    end

    current = slow
    while current
        max_sum = [max_sum, current.val + stack.pop].max
        current = current.next
    end

    max_sum
end


# Example usage:
# Creating the linked list: 5 -> 4 -> 2 -> 1
head = ListNode.new(5)
head.next = ListNode.new(4)
head.next.next = ListNode.new(2)
head.next.next.next = ListNode.new(1)

# Calling the function
result = pair_sum(head)
puts result  # Output: 6

# Case 2:
# Creating the linked list: 4 -> 2 -> 2 -> 3
head2 = ListNode.new(4)
head2.next = ListNode.new(2)
head2.next.next = ListNode.new(2)
head2.next.next.next = ListNode.new(3)

# Calling the function
result2 = pair_sum(head2)
puts result2  # Output: 7

# Case 3:
# Creating the linked list: 1 -> 1000000
head3 = ListNode.new(1)
head3.next = ListNode.new(1000000)

# Calling the function
result3 = pair_sum(head3)
puts result3  # Output: 1000001
