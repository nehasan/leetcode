# leetcode 26 : remove duplicates from sorted array

# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  tempNums = []

  nums.each_with_index do |val, index|
    tempNums << val unless tempNums.last == val

    nums[index] = '_'
  end

  k = tempNums.length
  iter = 0
  while tempNums.any?
    nums[iter] = tempNums.shift
    iter += 1
  end

  puts "--- final k #{k}"
  puts "--- final nums #{nums}"
  k
end

# Testcase 1
# nums = [1, 1, 2]

# Testcase 2
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

remove_duplicates(nums)
