from typing import Iterable, List
# from heapq import heapify, heappush, heappop


class HeapTest:

    def __init__(self) -> None:
        _list = []
        _sorted = []

    def heapify(self) -> None:

        def swap(pos1, pos2):
            temp = self._list[pos1]
            self._list[pos1] = self._list[pos2]
            self._list[pos2] = temp

        # i = 0
        print(len(self._list))

        for i in range(len(self._list)):
            # print(f'I: {i}')
            if (2 * i) + 1 <= (len(self._list) - 1) :
                parent = self._list[i]
                lChild = self._list[(2 * i) + 1]
                rChild =  () if (2 * i) + 2 >= len(self._list) else self._list[(2 * i) + 2]

                print(f'Parent: {parent} | lChild: {lChild} | rChild: {rChild}')
                if lChild and parent[1] < lChild[1]:
                    print(f'SWP LEFT CHILD: parent {parent[1]} < lChild {lChild[1]}')
                    swap(i, (2 * i) + 1)
                    self.heapify()
                    # parent = self._list[i]
                    # print(f'after swap : parent {parent}')
                
                if rChild and parent[1] < rChild[1]:
                    print(f'SWP RIGHT CHILD: parent {parent[1]} < rChild {lChild[1]}')
                    swap(i, (2 * i) + 2)
                    self.heapify()
                    # parent = self._list[i]
                    # print(f'after swap : parent {parent}')
        
        print(f'HEAPIFY: {self._list}')
    
    def heapPop(self) -> List:
        temp = self._list[0]
        self._list[0] = self._list[-1]
        self._list = self._list[-len(self._list):-1]
        return temp


    def testHeap(self, input: List) -> None:
        self._list = input.copy()
        self._sorted = []

        while self._list:
            # print(self._list)
            self.heapify()
            self._sorted.append(self.heapPop())
            print(f'AFTER HEAPPOP: {self._list}')
        
        print(f'--- final sorted: {self._sorted}')
    


obj = HeapTest()
# _hash = { 'blue': 2, 'yellow': 5, 'red': 0, 'green': 6, 'brown': 1 }
_hash = { 'blue': 2, 'yellow': 5, 'red': 7, 'green': 6, 'brown': 1 }

obj.testHeap(list(_hash.items()))

# for i in range(0, 5):
#     print(i)