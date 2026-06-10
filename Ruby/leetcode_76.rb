# @param {String} s
# @param {String} t
# @return {String}
def min_window(s, t)
  mapT = {}
  t.split("").each do |elm|
    mapT[elm] = elm
  end
  
  tempStr = ""
  
  # sArr = s.split("")
  sortedT = t.split("").sort().join("")
  finalStr = s
  sLen = s.length
  
  i = 0
  j = 0
  loop do
    tempStr += s[j] if mapT.has_key?(s[j])
    
    puts "tempStr check : #{tempStr}"
    if is_substring(tempStr.split("").sort().join(""), sortedT)
      puts "found str : #{s[i..j]}"
      finalStr = s[i..j] if tempStr.length < finalStr.length
      tempStr = ""
      loop do
        i += 1
        break if mapT.has_key?(s[i]) || i > sLen - 2
      end
    end
    
    j < sLen
    break if (i >= (sLen - 1))
  end
  
  return finalStr
end

def is_substring (sOne, sTwo)
  puts "sOne: #{sOne}"
  puts "sTwo: #{sTwo}"
  i = 0
  j = 0
  
  while i < sOne.length
    if sOne[i] == sTwo[j]
      j += 1
      return true if j == sTwo.length
    end
    i += 1
  end
  
  puts "not sub string, returning false"
  return false
end


# Testcase 1
s = "ADOBECODEBANC"
t = "ABC"

puts min_window(s, t)

