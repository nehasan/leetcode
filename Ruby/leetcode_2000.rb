# @param {String} word
# @param {Character} ch
# @return {String}
def reverse_prefix(word, ch)
    index = word.index(ch)

    return word if index.nil?
    
    prefix = word[0..index].reverse
    suffix = word[(index + 1)..-1]

    prefix + suffix
end

# Example usage:
puts reverse_prefix("abcdefd", "d")  # Output: "dcbaefd"
puts reverse_prefix("xyxzxe", "z")   # Output: "zxyxxe"
puts reverse_prefix("abcd", "z")     # Output: "abcd"
puts reverse_prefix("hello", "o")   # Output: "olleh"
puts reverse_prefix("hello", "l")   # Output: "lleho"
puts reverse_prefix("a", "a")       # Output: "a"
puts reverse_prefix("a", "b")       # Output: "a"
puts reverse_prefix("", "a")        # Output: ""
