from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [i for i in rooms[0]]
        visited = [False for i in range(len(rooms))]
        visited[0] = True

        while len(stack) > 0:
            currVisiting = stack.pop()
            visited[currVisiting] = True

            for j in rooms[currVisiting]:
                if visited[j] == False:
                    stack.append(j)
        
        print(visited)
        for i in visited:
            if i == False:
                return False
        
        return True


soln = Solution()
# rooms = [[1],[2],[3],[]]
# rooms = [[1,3],[3,0,1],[2],[0]]
rooms = [[2,3],[],[2],[1,3]]
print(soln.canVisitAllRooms(rooms))