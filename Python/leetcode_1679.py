from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        algorithm: map the numbers with the occurrances
        now iterate over the numbers and subtract from k, m = k - n
        check if m is avaialble and > 0, reduce both m and n from the map and increase res
        '''
        map = dict()
        for n in nums:
            if n < k:
                if map.get(n) is None:
                    map[n] = 1
                else:
                    map[n] += 1
        
        # print(map)
        res = 0
        # apprach 1
        # for n in nums:
        #     m = k - n
        #     if m == n:
        #         if map.get(m) and map[m] > 1:
        #             map[m] -= 2
        #             res += 1
        #     elif map.get(m) and map[m] > 0 and map[n] > 0:
        #         map[n] -= 1
        #         map[m] -= 1
        #         # print(map)
        #         res += 1

        # approach 2
        for n, val in map.items():
            m = k - n
            while map.get(m):
                # print(f'here map[m]: {map[m]} map[n]: {map[n]}')
                if map[m] < 1 or map[n] < 1:
                    break
                if m == n:
                    if map[m] < 2 or map[n] < 2:
                        break
                    if map.get(m) and map[m] > 1:
                        # print(f"reducing m only: {m}")
                        map[m] -= 2
                        res += 1
                elif map.get(m) and map[m] > 0 and map[n] > 0:
                    # print(f"reducing m: {m}, n: {n}")
                    map[n] -= 1
                    map[m] -= 1
                    res += 1
                # print(map)

        return res


soln = Solution()
# nums = [1,2,3,4]
# k = 5
nums = [3,1,3,4,3]
k = 6
# nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
# k = 3
print(soln.maxOperations(nums, k))