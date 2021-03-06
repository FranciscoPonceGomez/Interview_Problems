def snake_string(s):
	result = []
	# Output the first row s[1],s[5],s[9]..
	for i in range(1, len(s), 4):
		result.append(s[i])
	# second row s[0], s[2], s[4]..
	for i in range(0, len(s), 2):
		result.append(s[i])
	# third row s[3],s[7],s[11],..
	for i in range(3, len(s), 4):
		result.append(s[i])
	return ''.join(result)

def snake_string_pythonic(s):
	return s[1::4] + s[::2] + s[3::4]

s = "Hello_World"
print(snake_string(s))
print(snake_string(s))
