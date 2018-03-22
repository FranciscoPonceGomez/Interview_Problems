def stringDiff(source, target):
    count = 0
    i = 0
    print(source)
    while source != target:
        if source[i] != target[i]:
            if len(source) > len(target):
                source.remove(source[i])
                i -= 1
            elif len(source) < len(target):
                source.insert(i, target[i])
            else:
                source[i] = target[i]
            count += 1
            print(source)
        i += 1
    print(source)
    return count

print(stringDiff(['S','a','t','u','r','d','a','y'],['S','u','n','d','a','y','s']))