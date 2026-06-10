from ctypes.wintypes import CHAR


class Solution:
    '''
    Not working. Map cannot be used
    Because of the following input/output
    chars = ["a","a","a","b","b","a","a"]
    out: ["a","3","b","2","a","2"]
    def compress(self, chars: list) -> int:
        map = dict()
        res = ""

        # sArr = [x for x in s]

        for x in chars:
            if map.get(x) is None:
                map[x] = 1
            else:
                map[x] += 1
        
        for k, v in map.items():
            if v == 1:
                res += f"{str(k)}"
            else:
                res += f"{str(k)}{str(v)}"
        
        print(res)
        chars = [x for x in res]
        print(chars)

        return len(chars)
    '''

    def compress(self, chars: list) -> int:
        s = ""
        prevChar = chars[0]
        count = 1
        

        def updateString(char: str, cx: int, s: str) -> str:
            if count == 1:
                s += f"{str(prevChar)}"
            else:
                s += f"{str(prevChar)}{str(count)}"

            return s
        
        for x in chars[1:]:
            if x != prevChar:
                s = updateString(prevChar, count, s)
                prevChar = x
                count = 0
            
            count += 1
        
        if count > 0:
            s = updateString(prevChar, count, s)
        
        # print(s)
        i = 0
        for x in s:
            chars[i] = x
            i += 1

        # print(chars)
        return len(s)


soln = Solution()
chars = ["a","a","b","b","c","c","c"]
chars = ["a"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","a","b","b","a","a"]
print(soln.compress(chars))