from typing import List


'''
Algorithm approach recursive dfs, O(n * m) time complexity
For each i, j position start recursive dfs for 4 positions around that. [i, j-1], [i - 1, j], [i, j + 1], [i + 1, j].
Send additional parent info for each of these nodes, such as current node value, ocean flags and visited nodes map etc.
Before starting each i, j mark them visited and also mark the current i, j inside dfs (means these are processed)
Inside the dfs block immediate return if two oceans are marked true (means the water flows to both oceans so further computation is not required), or the node is already visted.
Or the current node value is greater than prev node value (means water cannot flow, because of the higher height)
Mark both oceans true based on the i value and j value if they reach out of boundary
Else continue dfs for another 4 positions around the current i, j
'''


# class Solution:
#     visited = dict()
#     oceans = [False, False]
#     def checkFlowUsingDFS(self, i:int, j:int, rowSize:int, colSize:int, heights: List[List[int]], prevHeight: int, visited: dict, oceans: List[int]) -> None:
#         # print(f"entered into DFS: i:{i}, j:{j}, prevHeight: {prevHeight}")
#         if oceans[0] == True and oceans[1] == True or visited.get((i, j)):
#             return
#         if i < 0 or j < 0:
#             oceans[0] = True
#             return
#         if i >= rowSize  or j >= colSize:
#             oceans[1] = True
#             return

#         currHeight = heights[i][j]
#         if currHeight > prevHeight:
#             return
#         visited[(i, j)] = True
#         # print(f"processing for DFS: i:{i}, j:{j}, prevHeight: {prevHeight}, currHeight: {currHeight}")
#         self.checkFlowUsingDFS(i, j - 1, rowSize, colSize, heights, currHeight, visited, oceans)
#         self.checkFlowUsingDFS(i - 1, j, rowSize, colSize, heights, currHeight, visited, oceans)
#         self.checkFlowUsingDFS(i, j + 1, rowSize, colSize, heights, currHeight, visited, oceans)
#         self.checkFlowUsingDFS(i + 1, j, rowSize, colSize, heights, currHeight, visited, oceans)

#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         res = []
#         rowSize = len(heights)
#         colSize = len(heights[0])
#         for i in range(rowSize):
#             for j in range(colSize):
#                 currHeight = heights[i][j]
#                 self.oceans[0] = False
#                 self.oceans[1] = False
#                 self.visited.clear()
#                 self.visited[(i, j)] = True
#                 # print(f"next i j : {i} {j}")
#                 self.checkFlowUsingDFS(i, j - 1, rowSize, colSize, heights, currHeight, self.visited, self.oceans)
#                 self.checkFlowUsingDFS(i - 1, j, rowSize, colSize, heights, currHeight, self.visited, self.oceans)
#                 self.checkFlowUsingDFS(i, j + 1, rowSize, colSize, heights, currHeight, self.visited, self.oceans)
#                 self.checkFlowUsingDFS(i + 1, j, rowSize, colSize, heights, currHeight, self.visited, self.oceans)
#                 if self.oceans[0] == True and self.oceans[1] == True:
#                     res.append([i, j])

#         return res


'''
Algorithmic approach 2:
Instead of computing for all the position, start computing from each pacific and atlantic coast side.
Mark each height higher than the starting coast position and stop searching if the height is lower than the current one
List all the valid positions for pacific and atlantic sets
Final answer will be the intersection of these two sets
Mark visited after checking the height comparison otherwise will get a wrong answer
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Methods declaration
        def initiateSearch(i: int, j: int, rowSize: int, colSize: int, heights: List[List[int]], currHeight: int, ocean: set, visited: dict):
            findPeakHeight(i, j - 1, rowSize, colSize, heights, currHeight, ocean, visited)
            findPeakHeight(i - 1, j, rowSize, colSize, heights, currHeight, ocean, visited)
            findPeakHeight(i, j + 1, rowSize, colSize, heights, currHeight, ocean, visited)
            findPeakHeight(i + 1, j, rowSize, colSize, heights, currHeight, ocean, visited)

        def findPeakHeight(i: int, j: int, rowSize: int, colSize: int, heights: List[List[int]], prevHeight: int, ocean: set, visited: dict) -> None:
            # print(f"finding for i: {i}, j: {j}")
            if i < 0 or i >= rowSize or j < 0 or j >= colSize or visited.get((i, j)) != None:
                return
            
            currHeight = heights[i][j]
            if prevHeight > currHeight:
                return
            
            # print(f"prevHeight: {prevHeight}, visited: {visited}")
            # List them as valid position from where water can be flown into
            visited[(i, j)] = True
            ocean.add((i, j))
            # print(f"ocean: {ocean}")
            initiateSearch(i, j, rowSize, colSize, heights, currHeight, ocean, visited)
        
        # Main computation
        pacific = set()
        atlantic = set()
        rowSize = len(heights)
        colSize = len(heights[0])
        visited = dict()

        # Computate for left side pacific ocean
        j = 0
        for i in range(rowSize):
            currHeight = heights[i][j]
            visited.clear()
            visited[(i, j)] = True
            pacific.add((i, j))
            print(f'processing (i, j): {i, j}')
            initiateSearch(i, j, rowSize, colSize, heights, currHeight, pacific, visited)
        
        # Compute for top side pacific ocean
        i = 0
        for j in range(colSize):
            currHeight = heights[i][j]
            visited.clear()
            visited[(i, j)] = True
            pacific.add((i, j))
            print(f'processing (i, j): {i, j}')
            initiateSearch(i, j, rowSize, colSize, heights, currHeight, pacific, visited)

        
        # Compute for right side atlantic ocean
        j = colSize - 1
        for i in range(rowSize):
            currHeight = heights[i][j]
            visited.clear()
            visited[(i, j)] = True
            atlantic.add((i, j))
            print(f'processing (i, j): {i, j}')
            initiateSearch(i, j, rowSize, colSize, heights, currHeight, atlantic, visited)
        
        # Compute for bottom side atlantic ocean
        i = rowSize - 1
        for j in range(colSize):
            currHeight = heights[i][j]
            visited.clear()
            visited[(i, j)] = True
            atlantic.add((i, j))
            # print(f'processing (i, j): {i, j}')
            initiateSearch(i, j, rowSize, colSize, heights, currHeight, atlantic, visited)
        
        # print(pacific)
        # print(atlantic)

        return [list(i) for i in pacific.intersection(atlantic)]



soln = Solution()
# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# heights = [[4,5,6],[1,2,3],[3,2,1]]
# heights = [[1,2,3],[8,9,4],[7,6,5]]
# heights = [[1]]
# heights = [[1,2],[1,2]]
# heights = [[1,2],[2,2]]
heights = [[12,7,7,14,6,17,12,17,8,18,9,5],
            [6,8,12,5,3,6,2,14,19,6,18,13],
            [0,6,3,8,8,10,8,17,13,13,13,12],
            [5,6,8,8,15,16,19,14,7,11,2,3],
            [7,18,2,7,10,10,3,14,13,15,15,7],
            [18,6,19,4,12,3,3,2,6,6,19,6],
            [3,18,5,16,19,6,3,12,6,0,14,11],
            [9,10,17,12,10,11,11,9,0,0,12,0],
            [4,13,3,0,4,12,9,5,6,17,10,11],
            [18,3,5,0,8,19,18,4,8,19,1,3],
            [16,2,14,6,4,14,7,2,9,7,13,18],
            [0,16,19,16,16,4,15,19,7,0,3,16],
            [13,8,12,8,2,3,5,18,6,15,18,6],
            [4,10,8,1,16,0,6,0,14,10,11,8],
            [7,1,3,4,11,12,9,0,6,2,17,5],
            [1,16,6,1,0,19,11,1,5,7,8,2],
            [4,1,14,13,14,7,3,7,1,9,15,18],
            [14,11,6,14,14,14,4,0,11,17,1,9],
            [3,14,2,10,3,1,9,16,1,13,0,15],
            [8,9,13,5,5,7,10,1,4,5,0,9],
            [13,16,15,5,17,6,16,13,5,7,3,15],
            [5,1,12,19,3,13,0,0,3,10,6,13],
            [12,17,9,16,16,6,2,6,12,15,14,16],
            [7,7,0,6,4,15,1,7,17,5,2,12],
            [3,17,0,2,4,5,11,7,16,16,16,13],
            [3,7,16,11,2,16,14,9,16,17,10,3],
            [12,18,17,17,5,15,1,2,12,12,5,7],
            [11,10,10,0,11,7,17,14,5,15,2,16],
            [7,19,14,7,6,2,4,16,11,19,14,14],
            [6,17,6,6,6,15,9,12,8,13,1,7],
            [16,3,15,0,18,17,0,11,3,16,11,12],
            [15,12,4,6,19,15,17,7,3,9,2,11]]

# heights = [ [12,7,7,14,6,17,12,17,8,18,9,5],
#             [6,8,12,5,3,6,2,14   ,19,6,18,13],
#             [0,6,3,8,8,10,8,17   ,13,13,13,12],
#             [5,6,8,8,15,16,19,14,7,11,2,3]]
print(soln.pacificAtlantic(heights))