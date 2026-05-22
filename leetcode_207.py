from typing import List
from collections import defaultdict

class Solution:
    
    '''
    Approach: Graph traversal and try to find a cycle in a graph.
    An undirected graph does not have any cycle but a directed graph can have a cycle in it.
    For example if the prerequisites are preqs = [[0, 1], [1, 0]] that means course 0 is dependant
    on course 1 and vice versa. This is a cycle.
    To detect a cycle in a directed graph a DFS approach can be introduced.
    In this DFS traversal let's say we picked node 0 and in its current travarsal it reaches to a
    Node let's say 1, and then 1 reaches to again 0 that is already in the current traversal list then it is a cycle.
    Time compltexity O(n + v) 
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfsSearch(node: int, courseMap: defaultdict, trajectoryPath: defaultdict, pathMarker):
            state = trajectoryPath[node]
            
            if state == pathMarker["VISITED"]:
                return True
            
            elif state == pathMarker["VISITING"]:
                return False
            
            trajectoryPath[node] = pathMarker["VISITING"]
            
            for nei in courseMap[node]:
                if dfsSearch(nei, courseMap, trajectoryPath, pathMarker) == False:
                    return False
            
            trajectoryPath[node] = pathMarker["VISITED"]
            return True
        
        
        courseMap = defaultdict(list)
        pathMarker = { "UNVISITED": 0, "VISITING": 1, "VISITED": 2 }
        trajectoryPath = defaultdict(int)
        
        for x in range(numCourses):
            courseMap[x] = []
            trajectoryPath[x] = pathMarker["UNVISITED"]
            
        for [a, b] in prerequisites:
            courseMap[a] += [b]
        
        for k, v in courseMap.items():
            if v:
                if dfsSearch(k, courseMap, trajectoryPath.copy(), pathMarker) == False:
                    return False
        
        return True


obj = Solution()
prerequisites = [[1,0],[1,2],[0,1]]
numCourses = 3
obj.canFinish(numCourses, prerequisites)

def test_case_0001():
    prerequisites = [[1,0], [0,1]]
    numCourses = 2
    assert(obj.canFinish(numCourses, prerequisites)) == False

def test_case_0002():
    prerequisites = [[1,0]]
    numCourses = 2
    assert(obj.canFinish(numCourses, prerequisites)) == True

def test_case_0003():
    prerequisites = [[1,4],[2,4],[3,1],[3,2]]
    numCourses = 5
    assert(obj.canFinish(numCourses, prerequisites)) == True

def test_case_0004():
    prerequisites = [[0,1],[0,2],[1,2]]
    numCourses = 3
    assert(obj.canFinish(numCourses, prerequisites)) == True

def test_case_0005():
    prerequisites = [[1,0],[1,2],[0,1]]
    numCourses = 3
    assert(obj.canFinish(numCourses, prerequisites)) == False

def test_case_0005():
    prerequisites = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
    numCourses = 6
    assert(obj.canFinish(numCourses, prerequisites)) == True