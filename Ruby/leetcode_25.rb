# leetcode 25: remove element

# @param {Integer[]} nums
# @param {Integer} val
# @return {Integer}
def remove_element(nums, _val)
  tempNums = []
  nums.each_with_index do |val, index|
    tempNums << val if val != _val
    nums[index] = '-'
  end

  # puts "--- input nums:  #{nums}"
  k = tempNums.length
  # puts "--- res : #{k}"
  i = 0
  while tempNums.any?
    nums[i] = tempNums.shift
    i += 1
  end
  # puts "--- final nums: #{nums}"

  k
end

# Test case 1
# nums = [3, 2, 2, 3]
# val = 3

# Test case 2
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
remove_element(nums, val)
