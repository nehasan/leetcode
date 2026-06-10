'''
leet code 264: ugly numbers
author: nahid hasan khan
17-07-2023 
'''
class Solution:

    '''
    Method is responsible for generating ugly numbers by multiplying the factors with smaller
    ugly numbers.
    @param[Int] nth ugly number to be returned
    @return[Int] the ugly number present in nth index
    '''
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        two = three = five = 0

        # fill up the calculated ugly numbers till we get the nth one
        while len(ugly_numbers) < n:

            # increase each pointer untill the recent calcuated one is less than or equal
            #   to the last generated ugly number
            while (ugly_numbers[two] * 2 <= ugly_numbers[-1]):
                two += 1

            while (ugly_numbers[three] * 3 <= ugly_numbers[-1]):
                three += 1

            while (ugly_numbers[five] * 5 <= ugly_numbers[-1]):
                five += 1
            
            # we take the minimum one and inserted into the ugly_numbers array
            ugly_numbers.append(min((ugly_numbers[two] * 2), (ugly_numbers[three] * 3), (ugly_numbers[five] * 5)))
        
        return ugly_numbers[-1]


# obj = Solution()
# print(obj.nthUglyNumber(1352)) // will produce output 402653184