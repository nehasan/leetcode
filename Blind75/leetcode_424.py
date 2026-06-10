'''
algorithm used: sliding window
map the frequency of the characters inside the current window (leftPtr to rightPtr)
within the current window check if we can change k characters except the most freq character
if we can then increase the right pointer and check again for another max window
if not the we increase left pointer and decrease the freq from the map to adjust the max freq character'
res will always between the max of valid window length and last max res
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = dict()
        leftPtr = 0
        rightPtr = 0
        strLen = len(s)
        maxFreqMap = { 'char': 'A', 'len': -1 }
        res = 0

        while leftPtr < strLen and rightPtr < strLen:
            
            if map.get(s[rightPtr]) is None:
                map[s[rightPtr]] = 1
            else:
                map[s[rightPtr]] += 1
            
            # Update the maxFreqMap
            if maxFreqMap['len'] < map[s[rightPtr]]:
                maxFreqMap['char'] = s[rightPtr]
                maxFreqMap['len'] = map[s[rightPtr]]

            currWindowLen = (rightPtr - leftPtr) + 1
            numCharToChange = currWindowLen - maxFreqMap['len']
            print(f"{map}, {maxFreqMap}, {numCharToChange}")
            isValidWindow = True if numCharToChange <= k else False

            if isValidWindow:
                res = max(res, currWindowLen)
                rightPtr += 1
            else:
                map[s[leftPtr]] -= 1

                # Update the maxFreqMap
                for _k, v in map.items():
                    if maxFreqMap['len'] < v:
                        maxFreqMap['char'] = _k
                        maxFreqMap['len'] = v
                
                leftPtr += 1
                rightPtr += 1
        
        return res


soln = Solution()
# s = 'ABAB'
# k = 2
# s = "AABABBA"
# k = 2
s = 'ABAA'
k = 0
print(soln.characterReplacement(s, k))