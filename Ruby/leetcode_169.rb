# leetcode 169: majority element

# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
  # maxSeen = 0
  seenHash = {}

  for elm in nums do
    if seenHash[elm].nil?
      seenHash[elm] = 1
    else
      seenHash[elm] += 1
    end

    # puts "--- seenHash: #{seenHash}"
    return elm if nums.length / 2 < seenHash[elm]
  end
end

# Testcase 1
# nums = [3, 2, 3]

# Testcase 2
nums = [2, 2, 1, 1, 1, 2, 2]
puts majority_element(nums)
