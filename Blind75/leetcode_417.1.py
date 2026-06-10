from typing import List
from collections import defaultdict

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def findAndAddNearestSummit(i: int, j: int, r: int, c: int, heights: List[List[int]], prevHeight: int, visited: defaultdict, coasts: List[tuple], resSet: set):
            if i >= 0 and i < r and j >= 0 and j < c:
                currHeight = heights[i][j]

                if currHeight >= prevHeight and (i, j) not in visited:
                    visited[(i, j)] = True
                    resSet.add((i, j))

                    initiateSearch(i, j, rowSize, colSize, heights, currHeight, visited, pacificCoasts, resSet)

        def initiateSearch(i: int, j: int, r: int, c: int, heights: List[List[int]], currHeight: int, visited: defaultdict, coasts: List[tuple], resSet: set):
            findAndAddNearestSummit(i, j - 1, r, c, heights, currHeight, visited, coasts, resSet)
            findAndAddNearestSummit(i - 1, j, r, c, heights, currHeight, visited, coasts, resSet)
            findAndAddNearestSummit(i, j + 1, r, c, heights, currHeight, visited, coasts, resSet)
            findAndAddNearestSummit(i + 1, j, r, c, heights, currHeight, visited, coasts, resSet)

        rowSize = len(heights)
        colSize = len(heights[0])
        pacificCoasts = []
        atlanticCoasts = []
        setPacific = set()
        setAtlantic = set()

        # left side pacific coasts
        pacificCoasts += [(i, 0) for i in range(rowSize)]

        # up side pacific coasts
        pacificCoasts += [(0, j) for j in range(colSize)]

        # right side atlantic coasts
        atlanticCoasts += [(i, colSize - 1) for i in range(rowSize)]

        # bottom side atlantic coasts
        atlanticCoasts += [(rowSize - 1, j) for j in range(colSize)]

        # print(pacificCoasts)
        # print(atlanticCoasts)

        for i, j in pacificCoasts:
            # print(f"search started for pacific (i, j) {(i, j)}")
            setPacific.add((i, j))
            visited = defaultdict(bool)
            visited[(i, j)] = True
            initiateSearch(i, j, rowSize, colSize, heights, heights[i][j], visited, pacificCoasts, setPacific)
        
        for i, j in atlanticCoasts:
            # print(f"search started for atlantic (i, j) {(i, j)}")
            setAtlantic.add((i, j))
            visited = defaultdict(bool)
            visited[(i, j)] = True
            initiateSearch(i, j, rowSize, colSize, heights, heights[i][j], visited, atlanticCoasts, setAtlantic)
        
        # print(f"final setPacific: {setPacific}")
        # print(f"final setAtlantic: {setAtlantic}")

        # res = list(set(pacificCoasts).intersection(set(atlanticCoasts)))
        return [list(x) for x in list(setPacific.intersection(setAtlantic))]


obj = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
heights = [[1,2],[1,2]]
heights = [[4,5,6],[1,2,3],[3,2,1]]
print(obj.pacificAtlantic(heights))