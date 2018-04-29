def isPalindrome(s):
	return all(s[i] == s[~i] for i in range(len(s)//2))
s = "buttub"
print(isPalindrome(s))
