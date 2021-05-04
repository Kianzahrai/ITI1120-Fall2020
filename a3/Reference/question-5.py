def vote_percentage(list):
	yes = 0
	no = 0
	list = list.split(' ')
	for vote in list:
		if vote == 'yes':
			yes += 1
		elif vote == 'no':
			no += 1
	if no == 0:
		return 'unanimous'
	elif yes / no >= 2:
		return 'clear majority'
	elif yes >= no:
		return 'simple majority'
	else:
		return 'motion failed'

print(vote_percentage(input('Input the votes (yes, no, abstention) seperated by spaces: ')))