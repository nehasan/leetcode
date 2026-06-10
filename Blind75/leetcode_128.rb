# @param {Integer[]} nums
# @return {Integer}
def longest_consecutive(nums)
  nums.sort!
  puts(nums)

  i = 0
  num_len = nums.length
  max_len = 0
  temp_len = 1
  return 1 if num_len == 1

  while i < num_len - 1
    if (nums[i] - nums[i + 1]).abs == 1
      temp_len += 1
    elsif (nums[i] - nums[i + 1]).abs > 1
      temp_len = 1
    end

    max_len = [temp_len, max_len].max
    i += 1
  end

  max_len
end

# nums = [100, 4, 200, 1, 3, 2]
# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# nums = [1, 0, 1, 2]
# nums = [0]
# nums = [1, 0]
# nums = [0, 0]
# nums = [1, 1]
# nums = [1, 2]
puts(longest_consecutive(nums))
