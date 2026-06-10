# leetcode 88 : Merge two sorted array in-place

# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, _n)
  tempNums = []
  for index in 1..m do
    tempNums << nums1[index - 1]
  end

  # nums1 = []
  iter = 0
  # puts "--- tempNums: #{tempNums}"
  while tempNums.any? || nums2.any?
    if tempNums.any? && nums2.any?
      if tempNums.first < nums2.first
        nums1[iter] = tempNums.shift
        iter += 1
      elsif tempNums.first > nums2.first
        nums1[iter] = nums2.shift
        iter += 1
      else
        nums1[iter] = tempNums.shift
        iter += 1
        nums1[iter] = nums2.shift
        iter += 1
      end

    elsif tempNums.any?
      nums1[iter] = tempNums.shift
      iter += 1
    elsif nums2.any?
      nums1[iter] = nums2.shift
      iter += 1
    end
  end

  # puts "--- final nums: #{nums1}"
end

# Test case 1
# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# m = n = 3

# Test case 2
# nums1 = [1]
# nums2 = []
# m = 1
# n = 0

# Test case 3
nums1 = []
nums2 = [1]
m = 0
n = 1
merge(nums1, m, nums2, n)
