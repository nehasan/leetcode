from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        index = 0
        for n in nums:
            if map.get(n) is None:
                map[n] = [index]
            else:
                map[n].append(index)
            
            index += 1
        
        for k,v in map.items():
            m = target - k
            if m == k:
                if len(map[m]) > 1:
                    print(map)
                    return [map[m][0], map[m][1]]
            elif map.get(m) is not None:
                print(map)
                return [map[k][0], map[m][0]]
        

soln = Solution()
# nums = [2, 7, 11, 15]
# target = 9
# nums = [3,2,4]
# target = 6
# nums = [3, 3]
# target = 6
# nums = [2, 5, 5, 11]
# target = 10
nums = [-3, 4, 3, 90]
target = 0
print(soln.twoSum(nums, target))