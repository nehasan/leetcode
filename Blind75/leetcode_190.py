class Solution:
    def reverseBits(self, n: int) -> int:
        revBits = [0] * 32

        pos = 0
        while n > 0:
            lastBit = n & 1
            n = n >> 1
            # print(f"--- here n : {n}")
            revBits[pos] = lastBit
            pos += 1
        
        print(revBits)

        index = 31
        powRank = 0
        revInt = 0
        while index >= 0:
            revInt += (revBits[index] * pow(2, powRank))

            powRank += 1
            index -= 1
        
        return revInt
    
obj = Solution()
print(obj.reverseBits(2))
print(obj.reverseBits(43261596))
print(obj.reverseBits(2147483644))