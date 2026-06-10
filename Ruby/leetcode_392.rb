# Leetcode 392. Is Subsecquence
# Author: Nahid Hasan Khan
# Dec 12 2024

# @param {String} s
# @param {String} t
# @return {Boolean}
def is_subsequence(s, t)
  hashT = {}
  
  # Store each element in a hash with the position index
  t.split("").each_with_index do |c, index|
    puts "--- t: #{c}"
    hashT[c].nil? ? hashT[c] = [index] : hashT[c] << index
  end
  
  puts "--- hashT: #{hashT}"
  
  hashT.each_key do |key, val|
    hashT[key] = hashT[key].sort
  end
  
  return true if s == ""
  
  positionArr = []
  
  s.split("").each_with_index do |c, index|
    puts "--- here c: #{c}"
    return false if hashT[c].nil? || hashT[c].length == 0
    positionArr << hashT[c][0]
  
    puts "--- hashT before shift: #{hashT}"
    hashT[c].shift
    puts "--- hashT after shift: #{hashT}"
  end
  
  positionArr.each_with_index do |val, index|
    next if index == 0
    return false if positionArr[index - 1] > val
  end
  
  return true
end


# Testcase 1
# Output: true
# s = "ace"
# t = "abcde"

# Testcase 2
# Output: false
# s = "aec"
# t = "abcde"

# Testcase 3
# Output: true
# s = "abc"
# t = "ahbgdc"

# Testcase 4
# Output: false
# s = "axc"
# t = "ahbgdc"

# Testcase 5
# Output: true
# s = ""
# t = "abc"

# Testcase 6
# Output: false
# s = "aaaaaa"
# t = "bcaaaa"

# Testcase 7
# Output: true
s = "ab"
t = "baab"
puts is_subsequence(s, t)
