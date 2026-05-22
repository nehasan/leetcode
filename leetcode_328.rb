# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end

def print(node)
  curr = node
  # while(curr.next)
#     puts "print node: #{curr.val}"
#     curr = curr.next
#   end

  loop do
    puts "print node: #{curr.val}"
    curr = curr.next
    break if curr.nil?
  end
end

# @param {ListNode} head
# @return {ListNode}
def odd_even_list(head)
  oddBeg = head
  evenBeg = head.next
  oddCurr = head
  evenCurr = head.next
  
  
  loop do
    break if evenCurr.nil?
    
    temp = evenCurr.next
    break if temp.nil?
    
    # puts "--- temp : #{temp&.val}"
    evenCurr.next = temp&.next
    # puts "--- even next : #{evenCurr.next&.val}"
    oddCurr.next = temp
    # puts "--- odd next : #{oddCurr.next&.val}"
    temp.next = evenBeg
    # puts "--- temp next : #{temp.next&.val}"
    
    oddCurr = oddCurr&.next
    # puts "current odd : #{oddCurr&.val}"
    evenCurr = evenCurr&.next
    # puts "current even : #{evenCurr&.val}"
  end
  
  # qOdd = []
#   qEven = []
#   loop do
#     qOdd << odd.val
#     qEven << even.val
#
#     break if odd.next&.next&.nil? || even.next&.next&.nil?
#
#     odd = odd.next&.next
#     even = even.next&.next
#   end
#
#   puts "--- qOdd : #{qOdd.inspect}"
#   puts "--- qOdd : #{qEven.inspect}"
#   curr = head
#   while qEven.length > 0
#     if !qOdd.shift.nil?
#       curr.val = qOdd.shift
#     else
#       curr.val = qEven.shift
#     end
#
#       curr = curr.next
#   end
#
#   # print(oddOrig)
#   # print(evenOrig)
#
#   # odd.next = evenOrig
  
  # print(head)
  return head
  
end

# Testcase
# Head: 1
# Expctd output: 1 // passed
# head = ListNode.new(1)

# Testcase
# Head: 1 2
# Expctd output: 1 2 // passed
# head = ListNode.new(1, ListNode.new(2))

# Testcase
# Head: 1 2 3
# Expctd output: 1 3 2 // passed
# head = ListNode.new(1, ListNode.new(2, ListNode.new(3)))

# Testcase
# Head: 1 2 3 4
# Expctd output: 1 3 2 4 // passed
# head = ListNode.new(1, ListNode.new(2, ListNode.new(3, ListNode.new(4))))

# Testcase
# Head: 1 2 3 4 5
# Expctd output: 1 3 5 2 4
# head = ListNode.new(1, ListNode.new(2, ListNode.new(3, ListNode.new(4, ListNode.new(5)))))

# Testcase
# Head: 2 1 3 5 6 4 7
# Expctd output: 2 3 6 7 1 5 4
# head = ListNode.new(2, ListNode.new(1, ListNode.new(3, ListNode.new(5, ListNode.new(6, ListNode.new(4, ListNode.new(7)))))))

# odd_even_list(head)