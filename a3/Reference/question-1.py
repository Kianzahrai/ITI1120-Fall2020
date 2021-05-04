def count_pos(list):
	list = list.split(' ')
	list = [float(i) for i in list]
	positives = 0
	for num in list:
		if num > 0:
			positives += 1
	print('There are ' + str(positives) + ' positive numbers in your list.')

count_pos(input('Please input a list of numbers seperated by a space: '))