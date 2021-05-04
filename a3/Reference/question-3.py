def longest_run(list):
	list = list.split(' ')
	list = [float(i) for i in list]
	most = max(set(list), key=list.count)
	return list.count(most)

print(longest_run(input('Please input a list of numbers seperated by spaces: ')))