# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1874653565/?envType=study-plan-v2&envId=leetcode-75
'''
Turn the string into array
Read the array and mark the vowel positions
Read the positions and interchange letters of the array with the first position and the last position, then 
Second first position with the second last position and so on
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowelPos = []

        sArr = [x for x in s]

        i = 0
        for x in sArr:
            if x in vowels:
                vowelPos.append(i)
            
            i += 1
        
        # print(vowelPos)
        posLen = len(vowelPos)
        i = 0
        j = posLen - 1

        while i < posLen / 2:
            temp = sArr[vowelPos[i]]
            sArr[vowelPos[i]] = sArr[vowelPos[j]]
            sArr[vowelPos[j]] = temp

            i += 1
            j -= 1

        return "".join(sArr)

soln = Solution()
s = "IceCreAm"
s = "leetcode"
s = "Ic"
s = "IcE"
s = "Ie"
print(soln.reverseVowels(s))