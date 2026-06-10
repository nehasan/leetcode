from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def stringToNumber(s: str) -> float:
            data = s.split(":")
            data = ".".join(data)
            # print(f"string data {data}")
            return float(data)
        
        start1 = stringToNumber(event1[0])
        end1   = stringToNumber(event1[1])

        start2 = stringToNumber(event2[0])
        end2   = stringToNumber(event2[1])

        data = sorted([[start1, end1], [start2, end2]])
        print(data)

        return data[1][0] <= data[0][1]


obj = Solution()

def test_case_0001():
    event1 = ["01:15","02:00"]
    event2 = ["02:00","03:00"]
    assert(obj.haveConflict(event1, event2)) == True

def test_case_0002():
    event1 = ["01:00","02:00"]
    event2 = ["01:20","03:00"]
    assert(obj.haveConflict(event1, event2)) == True

def test_case_0003():
    event1 = ["10:00","11:00"]
    event2 = ["14:00","15:00"]
    assert(obj.haveConflict(event1, event2)) == False

def test_case_0004():
    event1 = ["14:13","22:08"]
    event2 = ["02:40","08:08"]
    assert(obj.haveConflict(event1, event2)) == False