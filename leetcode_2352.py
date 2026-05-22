'''
Leet code 2352 Equal row and column pairs
'''

from typing import List
import numpy as np

class Solution:

    '''
    Returns number of equal row and column pairs
    Algorithm utilizes hashmap / dictionary in python
    - Extract each row and push to map with number of occurances
    - Extract each column and push to map with number of occurances
    - Lastly iterate through the row map entries and check if the entry exists
        within the column map
    - Return count += (row map value * col map value)
    '''
    def equalPairs(self, grid: List[List[int]]) -> int:

        rowSize = len(grid[0])
        colSize = len(grid)

        rowMap = dict()
        colMap = dict()

        for row in grid:
            # print(f"--- ROW {row}")
            numStr = '|'.join(str(x) for x in row)
            if rowMap.get(numStr) == None:
                rowMap[numStr] = 1
            else:
                rowMap[numStr] = rowMap.get(numStr) + 1
        
        gridNp = np.array(grid)

        for i in range(colSize):
            col = gridNp[:, i]
            print(f"--- COL {col}")
            numStr = '|'.join(str(x) for x in col)
            if colMap.get(numStr) == None:
                colMap[numStr] = 1
            else:
                colMap[numStr] = colMap.get(numStr) + 1
        

        count = 0
        for k, v in rowMap.items():
            if colMap.get(k) != None:
                count += (rowMap.get(k) * colMap.get(k))
                

        return count


obj = Solution()
# grid = [[3,2,1], [1,7,6], [2,7,7]] # output: 1
grid = [[3,1,2,2], [1,4,4,5], [2,4,2,2], [2,4,2,2]] # output: 3
# grid = [[11,1],[1,11]]

print(obj.equalPairs(grid))