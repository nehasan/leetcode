'''
leetcode 2390 Removing stars from string
Nahid Hasan Khan
Sep 10 2023
'''

class Solution:

    '''
    Returns resultant string after removing stars and closest left characters of a string
    Algorithm used : Stack
    - iterate over the string and read each char
    - if char found other than star then append into a list
    - if star is found then pop (LIFO) the last element of the list
    - return resultant chars left in the list
    @param[String] string that need to be processed according to the rule
    @return[String] resultant processed string
    '''
    def removeStars(self, s: str) -> str:

        list = []
        for char in s:
            if char != '*':
                list.append(char)
            else:
                list.pop()
        
        return ''.join(x for x in list)



obj = Solution()
# str = 'leet**cod*e' # output 'lecoe'
str = 'erase*****' # output ''
print(obj.removeStars(str))
