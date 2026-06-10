from typing import List


class Solution:
    # def reverseWord(self, word: str):
    #     rev_str = ''
    #     word_length = len(word)
    #     j = word_length - 1
    #     while j >= 0:
    #         rev_str += word[j]
    #         j -= 1
    #     return rev_str
    
    def reverse(self, words: List) -> str:
        words_length = len(words)
        i = 0
        j = words_length - 1
        while i < words_length / 2:
            temp = words[i]
            words[i] = words[j]
            words[j] = temp
            i += 1
            j -= 1
        
        # print(words)
        return " ".join(words)
    
    def reverseWords(self, s: str) -> str:
        i = 0
        res = []
        temp_str = ''
        length = len(s)

        for char in s:
            if char.isalpha() or char.isnumeric():
                temp_str += char
                if i == length - 1:
                    # res.append(self.reverseWord(temp_str))
                    res.append(temp_str)
            elif char.isspace():
                if temp_str != '':
                    # res.append(self.reverseWord(temp_str))
                    res.append(temp_str)
                    temp_str = ''
            i += 1
        
        # print(res)
        # print(" ".join(res))
        # return " ".join(res)
        return self.reverse(res)


soln = Solution()
# s = "  Hello   World "
# s = "   The sky is     blue"
s = "   The sky is    ocean blue    "
soln.reverseWords(s)