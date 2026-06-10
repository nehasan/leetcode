class Solution:
    def matchDollarPattern(self, s: str) -> bool:
        if len(s) == 1 or s[0] != '$':
            return False
        
        sLength = len(s)
        for i in range(1, sLength):
            if s[i] < '0' or s[i] > '9':
                return False
        
        return True

    def discountPrices(self, sentence: str, discount: int) -> str:
        wordTokens = sentence.split(" ")

        wordsLength = len(wordTokens)

        for i in range(wordsLength):
            if self.matchDollarPattern(wordTokens[i]):
                print(f"valid amount {wordTokens[i]}")
                amount = int(wordTokens[i][1:])
                calculated = amount - (amount * (discount / 100))
                print(f"calculated: {calculated}")

                wordTokens[i] = f"$%.2f" % calculated
        

        return " ".join(wordTokens)


soln = Solution()
# sentence = "there are $1 $2 and 5$ candies in the shop"
# discount = 50
sentence = "f32eir5f6hlmmtnlq$zno3zbl5pr26b1xmet6q3rjzs422zqzsezpgi4jqx3h0olb428pk95qndkfz8hereio$2ewx0cnqlvnb6nl$$8iny7t4aemhnqzz6971rnq7pha97e9lf16227j5l2033pnddk $3513024 $516863 $604 $9128265 $945728 $nbf 5az21pm0tj $"
discount = 26
print(soln.discountPrices(sentence, discount))
