# @param {Integer} num
# @return {String}
def convert_to_base7(num)
    return "0" if num == 0

    digits = []
    n = num.abs
    while n > 0
        digits << n % 7
        n /= 7
    end

    num < 0 ? "-" + digits.reverse.join : digits.reverse.join
end

# Example usage:
puts convert_to_base7(100)  # Output: "202"
puts convert_to_base7(7)    # Output: "10"
puts convert_to_base7(0)    # Output: "0"
puts convert_to_base7(50)   # Output: "101"
puts convert_to_base7(343)  # Output: "1000"
puts convert_to_base7(1)    # Output: "1"
puts convert_to_base7(14)   # Output: "20"
puts convert_to_base7(-100) # Output: "-202"
puts convert_to_base7(-7)   # Output: "-10"
puts convert_to_base7(-50)  # Output: "-101"