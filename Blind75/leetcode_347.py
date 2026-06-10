'''
https://leetcode.com/problems/top-k-frequent-elements/description/
'''

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = dict()
        for n in nums:
            if freqMap.get(n) == None:
                freqMap[n] = 1
            else:
                freqMap[n] += 1
        
        sortedFreq = sorted(freqMap.items(), key=lambda item: item[1], reverse=True)

        res = []
        for elm in sortedFreq:
            res.append(elm[0])
            k -= 1
            if k == 0:
                break

        return res

soln = Solution()
# nums = [1,1,1,2,2,3]
# k = 2
# nums = [1,2,1,2,1,2,3,1,3,2]
# k = 2
nums = [1]
k = 1
print(soln.topKFrequent(nums, k))