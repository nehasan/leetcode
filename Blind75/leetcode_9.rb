# 9. Palindrome Number

# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
    return false if x < 0

    original = x
    reversed = 0

    while x > 0
        digit = x % 10
        reversed = reversed * 10 + digit
        x /= 10
    end

    original == reversed
end

# Example usage:
puts is_palindrome(121)  # Output: true
puts is_palindrome(-121) # Output: false
puts is_palindrome(10)   # Output: false
puts is_palindrome(12321) # Output: true