def combinations(arr):
    res = []
    for i in range(1, 2**len(arr)):
        tmp = []
        binary = "{0:b}".format(i).zfill(len(arr))
        for j in range(0, len(binary)):
            if binary[j] == '1':
                tmp.append(arr[j])
        res.append(tmp)
    return res

arr = ['a','b','c']
print(combinations(arr))
