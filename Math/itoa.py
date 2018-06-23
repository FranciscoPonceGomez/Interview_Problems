from enum import Enum

# We have different options to handle negative numbers, I am going to consider two of them for this problem:
# Default -> returns the converted number with a '-' prefix
# C2 -> Calculates the complement 2 of the number. Complement 2 generates the negative representation of a number
# using three steps:
# 1. Transform to binary. 2. invert bits. 3. convert to target base. 
# ---Time complexity---: O(n), n = number of digits in the input 
# ---Space complexity---: O(n), n = number of digits in the input
Strategy = Enum('Strategy', 'Default C2')

def itoa(value, base, strategy=Strategy.Default):
    # Add the next line to restrict bases to binary, octal and hexadecimal
    assert base == 2 or base == 8 or base == 16, "Error. Only binary (2), octal(8) and hexadecimal(16) bases are allowed"
    res = []
    binary = []
    while value > 0:
        res.append(toString(value % base))
        value = value // base
    if value < 0:
        if strategy == Strategy.Default:
            return '-' + itoa(-value,base)
        # elif strategy == Strategy.C2:
        #     binary = itoa(-value,2)
        #     binary = reverseBits(binary)
        #     binary = addOneBinary(binary) 
        #binary += 1
        #while binary > 0:

        # to hex
    return ''.join(reverse(res))

# For bases larger than 10, this method encode the digits into ASCII ISO 266
# I am assuming that we are allowed to use built in data types conversions like "str", "chr" and "ord", if that is not the case,
# we can substitute lines 33 to 35 to:
# alphabet = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# return alphabet[value]
# We can add more elements to our alphabet for bases larget than 16
def toString(value):
    if value < 10 and value >= 0:
        return str(value)
    else:
        return chr(ord('A') - 10 + value)

# Since we cannot use built in functions, one of the best ways to reverse arrays is by using two indexes
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

def reverseBits(value):
    for i in range(0,len(value)):
        value[i] = 1 - value[i]
    return value

# def addOneBinary(value):
#     for i in range(len(value),-1,-1):
#         if value[i] == '0': 
#             value[i] = '1'
#             return value
#         else:


print(itoa(-39,3))
