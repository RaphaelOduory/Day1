#ralph = 23
def data_type(ralph):
	if type(ralph) == str:
		return len(ralph)
	elif type(ralph) == None:
		return "no value"
	elif type(ralph) == bool:
		return ralph
	elif type (ralph) == int:
		if ralph < 100:
			return "less than 100"
		elif ralph == 100:
			return "equal to 100"
		else:
			return "more than 100"
	elif type(ralph) == list:
		if len(ralph) >= 3:
			return ralph[3]
		else:
			return "None"
print(data_type(232))