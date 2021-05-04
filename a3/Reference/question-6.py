def roman(letters):
	total = 0
	for letter in list(letters):
		if letter == 'M':
			total += 1000
		elif letter == 'D':
			total += 500
		elif letter == 'C':
			total += 100
		elif letter == 'X':
			total += 10
		elif letter == 'V':
			total += 5
		elif letter == 'I':
			total += 1
	return total

print(roman(input('Input a roman numeral using the letters M, D, C, X, V, and I: ')))