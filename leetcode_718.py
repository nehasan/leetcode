from typing import List


class Solution:
    
    '''
    Approach 1: Sliding window, but it gets TLE
    '''
    # def findLength(self, nums1: List[int], nums2: List[int]) -> int:
    #     res = 0
    #     indexMap = {}
        
    #     for i, x in enumerate(nums1):
    #         if x in indexMap:
    #             indexMap[x] += [i]
    #         else:
    #             indexMap[x] = [i]
        
    #     i, j = 0, 0
    #     currMax = 0
    #     while j < len(nums2):
    #         if nums2[j] in indexMap:
    #             # print(f"nums2[j]: {nums2[j]}")
    #             indexes = indexMap[nums2[j]]
    #             for startIndex in indexes:
    #                 # print(f"startIndex: {startIndex} for indexes {indexes}")
    #                 i = startIndex
    #                 k = j
    #                 while i < len(nums1) and k < len(nums2) and nums1[i] == nums2[k]:
    #                     currMax += 1
    #                     res = max(res, currMax)
    #                     # print(f"i {i}, j: {k}, res: {res}, currMax: {currMax}")
    #                     i += 1
    #                     k += 1
                    
    #                 currMax = 0
            
    #         j += 1
        
        
    #     return res
    
    '''
    Approach 2: LCS
        0 1 2 3 2 1
    0   0 0 0 0 0 0
    3   0 0 0 1 0 0
    2   0 0 1 0 2 0
    1   0 1 0 0 0 3
    4   0 0 0 0 0 0
    7   0 0 0 0 0 0
    When nums1[i] == nums2[j] then dp[i][j] = 1 + dp[i - 1][j - 1] (prev diagonal)
    '''
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        
        # print(dp)
        maxLen = 0
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                maxLen = max(maxLen, dp[i][j])
        
        return maxLen


sol = Solution()
# nums1 = [1,2,3,2,1]
# nums2 = [3,2,1,4,7] # output 3
# print(sol.findLength(nums1, nums2))
# sol.findLength([], [])

def test_case_0001():
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7] # output 3
    assert sol.findLength(nums1, nums2) == 3

def test_case_0002():
    nums1 = [0,0,0,0,0]
    nums2 = [0,0,0,0,0] # output 5
    assert sol.findLength(nums1, nums2) == 5

def test_case_0003():
    nums1= [1]
    nums2 = [2] # output 0
    assert sol.findLength(nums1, nums2) == 0

def test_case_0004():
    nums1= [3]
    nums2 = [3] # output 1
    assert sol.findLength(nums1, nums2) == 1

def test_case_0005():
    nums1= [1,2]
    nums2 = [2,1] # output 1
    assert sol.findLength(nums1, nums2) == 1
    
def test_case_0006():
    nums1= []
    nums2 = [] # output 0
    assert sol.findLength(nums1, nums2) == 0

def test_case_0007():
    nums1 = [1, 2, 3]
    nums2 = [2, 3, 4, 1, 2, 3, 4] # output 3
    assert sol.findLength(nums1, nums2) == 3

def test_case_0008():
    nums1 = [0, 0, 0, 0, 1]
    nums2 = [1, 0, 0, 0, 0] # output 4
    assert sol.findLength(nums1, nums2) == 4

def test_case_0009():
    nums1 = [0, 1, 1, 1, 1]
    nums2 = [1, 0, 1, 0, 1] # output 2
    assert sol.findLength(nums1, nums2) == 2
    
def test_case_0010():
    nums1 = [0,0,0,0,0,0,1,0,0,0]
    nums2 = [0,0,0,0,0,0,0,1,0,0] # output 9
    assert sol.findLength(nums1, nums2) == 9