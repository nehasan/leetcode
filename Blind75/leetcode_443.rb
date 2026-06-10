class Solution
  def update_string(s, char, count)
    s += if count == 1
           "#{char}"
         else
           "#{char}#{count}"
         end

    s
  end

  def compress(chars)
    prevChar = chars[0]
    count = 1
    s = ''

    chars.each do |x|
      if x != prevChar
        s = update_string(s, prevChar, count)
        prevChar = x
        count = 0
      end

      count += 1
    end

    s = update_string(s, prevChar, count) if count > 0

    puts s
    s.split('').each_with_index do |x, i|
      chars[i] = x
    end

    puts "--- #{chars}"
    s.length
  end
end

soln = Solution.new
# chars = %w[a a a b b a a]
chars = ['a']
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# chars = ["a","a","a","b","b","a","a"]
puts "#{soln.compress(chars)}"
