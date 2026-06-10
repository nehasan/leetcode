'''
Problem description is a total mess/trash. Users are not allowed to use `bad` input. Just use `n`
Suppose, the server has all the versions listed with boolean
[False, False, False, True, True] // Total 5 versions
Now we need to find the index 4 as a first bad version.

Algorithm: recursive binary search approach to reduce the time complexity
- Calculate mid
- If mid is bad version then check if mid - 1 is false, that indicates mid is the first bad
- Else
- Check if mid is not bad then adjust beg to mid else adjust end otherwise
'''

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    versions = []
    for i in range(1, 11):
        if i > 5:
            versions.append(True)
        else:
            versions.append(False)
    print(versions)
    return versions[version]

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binarySearch(beg, end, low, high):
            mid = int((beg + end) / 2)

            isMidBad = isBadVersion(mid)
            isPrevMidBad = isBadVersion(mid - 1)
            if isMidBad and isPrevMidBad == False:
                return mid
            else:
                if isMidBad == False:
                    beg = mid + 1 if (mid + 1) <= high else high
                    binarySearch(beg, end, low, high)
                else:
                    end = mid - 1 if (mid - 1) >= low else low
                    binarySearch(beg, end, low, high)
        
        return binarySearch(1, n, 1, n)

soln = Solution()
print(soln.firstBadVersion(10))

