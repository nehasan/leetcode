class ListNode
  attr_accessor :val, :next_node

  #   :type val: Integer
  #   :type next_node: ListNode
  def initialize(val = 0, next_node = nil)
    @val = val
    @next_node = next_node
  end
end

class List
  attr_accessor :head, :size

  #   :type head: ListNode
  def initialize(head = nil)
    @head = head
    @size = 0
  end

  #     :type val: Integer
  def insert(val)
    curr = @head
    prev = nil

    # Make new node head if head is nil
    if curr.nil?
      new_node = ListNode.new(val)
      @head = new_node
    # Incase the list has only one element
    elsif curr.next_node.nil?
      # Place the new value either front or end
      if curr.val > val
        new_head = ListNode.new(val)
        new_head.next_node = curr
        @head = new_head
      else
        curr.next_node = ListNode.new(val)
      end
    # When the list has multiple value
    else
      # Find the node which has bigger value than the new one
      while curr.next_node && curr.val <= val
        prev = curr
        curr = curr.next_node
      end

      # If prev nil that means new value will be added to front
      if prev.nil?
        new_node = ListNode.new(val)
        new_node.next_node = curr
        @head = new_node
      # If the curr is last node then add it to the end of the list
      elsif curr.val <= val
        new_node = ListNode.new(val)
        curr.next_node = new_node
      # Else will be added to the middle of the prev and current nodes
      else
        temp = curr
        new_node = ListNode.new(val)
        prev.next_node = new_node
        new_node.next_node = temp
      end
    end

    @size += 1
  end
end

class MedianFinder
  def initialize
    @list_nums = List.new
    @size = 0
  end

  #     :type num: Integer
  #     :rtype: Void
  def add_num(num)
    @list_nums.insert(num)
    @size += 1
  end

  #     :rtype: Float
  def find_median
    return @list_nums.head.val if @size == 1

    nums = []
    curr = @list_nums.head
    while curr.next_node
      nums << curr.val
      curr = curr.next_node
    end
    nums << curr.val
    puts "--- nums: #{nums}"

    if @size.even?
      middle = @size / 2
      median = ((nums[middle - 1] + nums[middle]) / 2.0).round(5)
    else
      median = nums[@size / 2].round(5)
    end

    median
  end
end

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder.new
# obj.add_num(1)
# obj.add_num(2)
# puts(obj.find_median)
# obj.add_num(3)
# puts(obj.find_median)

ops = %w[MedianFinder addNum addNum findMedian addNum findMedian]
# vals = [[], [1], [2], [], [3], []]
# vals = [[], [1], [3], [], [2], []]

# ops = %w[MedianFinder addNum findMedian addNum findMedian addNum findMedian addNum findMedian addNum
#          findMedian addNum findMedian addNum findMedian addNum findMedian addNum findMedian addNum findMedian addNum findMedian]
# vals = [[], [6], [], [10], [], [2], [], [6], [], [5], [], [0], [], [6], [], [3], [], [1], [], [0], [], [0], []]

i = 0
obj = nil
res = []
for op in ops
  case op
  when 'MedianFinder'
    obj = MedianFinder.new
    res << 'null'
  when 'addNum'
    obj.add_num(vals[i][0])
    res << 'null'
  when 'findMedian'
    res << obj.find_median
  end
  i += 1
end

puts res
