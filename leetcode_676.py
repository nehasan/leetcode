from typing import List
from collections import defaultdict

class MagicDictionary:

    def __init__(self):
        self.magic_dictionary = defaultdict(list)
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.magic_dictionary[len(word)] += [word]
        

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.magic_dictionary:
            return False
        
        for word in self.magic_dictionary[len(searchWord)]:
            count = 0
            i = 0
            for ch in word:
                if ch != searchWord[i]:
                    count += 1
                if count > 1:
                    break
                i += 1
            
            if count == 1:
                return True
        
        return False

                    
        


# Example usage
obj = MagicDictionary()
# dictionary = ["hello", "leetcode"]
# obj.buildDict(dictionary)
#
# for searchWord in ["hello", "hhllo", "hell", "leetcoded"]:
#     print(obj.search(searchWord))


dictionary = ["hello", "hallo", "leetcode", "judge"]
obj.buildDict(dictionary)

for searchWord in ["hello", "hallo", "hell", "leetcodd", "juage"]:
    print(obj.search(searchWord))