def revd(word):
	list = []
	a = -len(word)
	b = -1
	while b != a - 1:
		list.append(word[b])
		list.append(word[b])
		b -= 1
	return list

user = input('Please enter a chain of characters: ')

for letter in range(8):
	print(revd(user)[letter], end = '')