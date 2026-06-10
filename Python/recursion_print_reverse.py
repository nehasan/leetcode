def printReverse (i: int, arr: list):
    # print(f"INDEX: {i}")
    if i < len(arr) - 1:
        print(printReverse(i + 1, arr))
        # print(arr[i])
    
    return arr[i]


arr = [1,2,3,4,5]
print(printReverse(0, arr))