from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Algorithm approach:
        It is all about find and detect a cycle in this graph starting from all edges
        DFS would be the fastest solution in this case
        '''
        # def checkLoopDFS(edge, edgeMap, canFinishMap):
        #     visitedMap = dict()

        #     stack = [edge]

        #     while stack:
        #         currEdge = stack.pop()

        #         if visitedMap.get(currEdge) == True:
        #             return False
        #         if canFinishMap.get(currEdge):
        #             return True
                
        #         for e in edgeMap[currEdge]:
        #             stack.append(e)
                
        #         visitedMap[currEdge] = True

        #     return True

        def dfs(node, graph, finishSet):
            VISITED = set()
            VISITING = set()

            stack = [node]
            
            while stack:
                currNode = stack.pop()
                VISITING.add(currNode)

                if currNode in VISITING:
                    return False
                
                for neighbor in graph[currNode]:
                    if neighbor not in VISITED:
                        stack.append(neighbor)

                VISITED.add(currNode)
            
            return True

        if prerequisites == 1:
            return True
            
        edgeMap = dict()
        graph = dict()
        finishSet = set()

        for i in range(numCourses):
            edgeMap[i] = []

        for c, p in prerequisites:
            edgeMap[c].append(p)
        
        # print(edgeMap)
        for i in range(numCourses):
            if not dfs(i, graph, finishSet):
                return False
            finishSet.add(i)
        
        return True

soln = Solution()
# numCourses = 2
# prerequisites = [[1, 0]]
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
numCourses = 3
prerequisites = [[0,1],[0,2],[1,2]] # True
# prerequisites = [[1,0],[1,2],[0,1]] # False
print(soln.canFinish(numCourses, prerequisites))


