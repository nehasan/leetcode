from typing import List
from collections import defaultdict

class Solution:
    '''
    Approach: Bucket sort. Map the numbers to their frequency
    Now sort the data based on the frequency value in descending order
    Print first k key from the that sorted data
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ferquencyMapper = defaultdict(int)
        
        for n in nums:
            ferquencyMapper[n] += 1
        
        sortedData = sorted(
            ferquencyMapper.items(),
            key=lambda x: x[1],
            reverse=True
        )
        print(sortedData)
        output = []
        for i in range(k):
            output.append(sortedData[i][0])
        
        return output


obj = Solution()

def test_case_0001():
    nums = [1,1,1,2,2,3]
    k = 2
    assert(obj.topKFrequent(nums, k)) == [1,2]
    
def test_case_0002():
    nums = [1,2,1,2,1,2,3,1,3,2]
    k = 2
    assert(obj.topKFrequent(nums, k)) == [1,2]
    
def test_case_0003():
    nums = [1]
    k = 1
    assert(obj.topKFrequent(nums, k)) == [1]