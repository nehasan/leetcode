# list1 = [5, 2, 2, 3, 4]

# s1 = set()

def removeDup(arr: list) -> list:

    res = list()
    map = dict()

    for i in list1:
        map[i] = map.get(i, 0) + 1

    for k,v in map.items():
        if (v == 1):
            res.append(k)
    
    return res


list1 = [5, 2, 2, 3, 4]

print(removeDup(list1))

