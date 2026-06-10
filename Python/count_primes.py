'''
Leet code 204 : Count Primes
Author: Nahid Hasan Khan
'''

import math

class Solution:
    '''
    Returns the number of primes present within the range 0 - n
    It utilizes the algorithm called sieve of eratosthenes
    Initialize an array of range n with True values
    Then the algorithm opt out [False] the resultant multiples multiplied the factors
    - iterate i till to the sqrt of n
    - take each factor j starting from 2 until it reaches i * j > n
    - opt out the multiples primes[i * j] = false

    @param[Int] n, the range within the primes to be counted
    @return[Int] the number of primes within the range of n
    '''
    def countPrimes(self, n: int) -> int:
        num_primes = 0
        primes = [True] * (n + 3)
        primes[0] = False
        primes[1] = False

        # iterate i from 2 to sqrt of n
        for i in range(2, math.isqrt(n) + 1):
            if primes[i] == True:
                for j in range(2, (n + 1)):
                    # break the loop if i * j > n
                    if (i * j) > n : break
                    # opt out the multiples
                    primes[i * j] = False

        # print(primes) to debug
        for k in range(0, n):
            if primes[k] == True:
                num_primes += 1

        return num_primes



obj = Solution()
print(obj.countPrimes(10))
print(obj.countPrimes(10000))
print(obj.countPrimes(499979))