
# We have different options to handle negative numbers, I am going to consider returning
# the converted number with a '-' prefix
# ---Time complexity---: O(n), n = number of digits in the input 
# ---Space complexity---: O(n), n = number of digits in the input

def itoa(value, base):
    # Add the next line to restrict bases to binary, octal and hexadecimal
    assert base == 2 or base == 8 or base == 16, "Error. Only binary (2), octal(8) and hexadecimal(16) bases are allowed"
    res = []
    while value > 0:
        res.append(toString(value % base))
        value = value // base
    if value < 0:
        return '-' + itoa(-value,base)
    return ''.join(reverse(res))

# For bases larger than 10, this method encode the digits into ASCII ISO 266
# I am assuming that we are allowed to use built in data types conversions like "str", "chr" and "ord", if that is not the case,
# we can substitute add:
# alphabet = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# return alphabet[value]
# We can add more elements to our alphabet for bases larget than 16
def toString(value):
    if value < 10 and value >= 0:
        return str(value)
    else:
        return chr(ord('A') - 10 + value)

# Since we are trying to limit the use of built-in functions, one of the best ways to reverse arrays is by using two indexes
# ---Time Complexity---: O(n/2) ~= O(n), n = number of digits in the input 
# This method doesn't increase the total complexity if itoa since O(2n) ~= O(n)
# ---Space Complexity---: O(1)
def reverse(value):
    i,j = 0,len(value)-1
    while i <= j:
        value[i],value[j] = value[j],value[i]
        i += 1
        j -= 1
    return value