def itoa(value, base):
    res = []
    while value > 0:
        res.append(toString(value % base))
        value = value // base
    #res[i] = '\0'
    return ''.join(reverse(res))

def toString(value):
    #if str and chr operations are not allowed
    #alphabet = ['0','1','2','3','4','5','6','7','8','9','10','A','B','C','D','E','F']
    #return alphabet[value]
    if value < 10:
        return str(value)
    else:
        return chr(ord('A') - 10 + value)

def reverse(value):
    i,j = 0, len(value)-1
    while i <= j:
        value[i],value[j] = value[j],value[i]
        i += 1
        j -= 1
    return value


print(itoa(12345678,16))