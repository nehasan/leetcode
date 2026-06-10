class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowelPos = []
        vowelArr = []
        
        sArr = [x for x in s]

        i = 0
        for x in sArr:
            if x in vowels:
                vowelArr.append(x)
                vowelPos.append(i)
            
            i += 1
        
        vowelArr.sort()

        i = 0
        for x in vowelPos:
            sArr[x] = vowelArr[i]
            i += 1
        
        print("".join(sArr))

        return "".join(sArr)


soln = Solution()
s = "lEetcOde"
s = "lYmpH"
s = "E"
s = "Ee"
s = "eE"
print(soln.sortVowels(s))