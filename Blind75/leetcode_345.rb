def reverse_vowels(s)
  vowels = 'aeiouAEIOU'
  vowelPos = []

  sArr = s.split('')
  #   puts "--- sArr: #{sArr}"

  sArr.each_with_index do |e, i|
    vowelPos << i if vowels.include?(e)
  end

  #   puts "--- vowelPos : #{vowelPos}"

  posLen = vowelPos.length
  i = 0
  j = posLen - 1

  loop do
    break if i >= posLen / 2

    temp = sArr[vowelPos[i]]
    sArr[vowelPos[i]] = sArr[vowelPos[j]]
    sArr[vowelPos[j]] = temp
    # puts "--- current sArr: #{sArr}"

    i += 1
    j -= 1
  end

  sArr.join('')
end

s = 'IceCreAm'
# s = ""
puts "#{reverse_vowels(s)}"
