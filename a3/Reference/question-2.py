def two_length_run(list):
	list = list.split(' ')
	list = [float(i) for i in list]
	counter = 0
	for num in range(len(list) - 1):
		if list[counter] == list[counter + 1]:
			return True
		counter += 1
	return False

print(two_length_run(input('Please input a list of numbers seperated by spaces: ')))