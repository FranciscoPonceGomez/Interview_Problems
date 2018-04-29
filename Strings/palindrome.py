def isPalindrome(s):
	return all(s[i] == s[~i] for i in range(len(s)//2))
s = "buttub"
s2 = "but224tub"

def isPalindrome2(s):
	i,j = 0, len(s)-1
	while i < j:
		while not s[i].isalnum() and i < j:
			i = i+1
		while not s[j].isalnum() and i < j:
			j = j-1
		if s[i].lower() != s[j].lower():
			return False
		i,j = i+1, j-1
	return True
print(isPalindrome(s))
print(isPalindrome2(s2))
