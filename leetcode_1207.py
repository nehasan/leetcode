'''
Leet code 1207. Unique Number of Occurrances
Nahid Hasan Khan
Sep 06 2023
'''
from typing import List

class Solution:

    '''
    Returns boolean true or false based on unique number of occurrances of a number in a list
    Algorithm uses hashmap/dictionary to store number -> occurrances as key -> value pair to a dictionary
    And later iterate through the items of the dictionary and with the help of a set library duplication can be checked
    - Create freq map and store number -> occurrances as key -> value
    - Iterate over the items of the map and check occurances duplicacy using set lib

    @param [List] list of numbers to be checked
    @return [Boolen] true or false based on duplicate occurrance value
    '''
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqMap = dict()

        for n in arr:
            if freqMap.get(n) == None:
                freqMap[n] = 1
            else:
                freqMap[n] = freqMap.get(n) + 1
        

        freqSet = set()

        for key, val in freqMap.items():
            if val in freqSet:
                return False
            else:
                freqSet.add(val)
        
        return True

obj = Solution()
# arr = [1,2,2,1,1,3] # output: True
# arr = [1,2] # output: False
arr = [-3,0,1,-3,1,1,1,-3,10,0] # output: True
print(obj.uniqueOccurrences(arr))