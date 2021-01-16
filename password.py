password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	ps = input("Enter Password: ")
	if ps == password:
		print('password is correct')
		break #Exit
	else:
		print('Password Error')
		if i > 0:
			print('you have ', i, 'time(s) to try.')
		else:
			print('You have tried 3 times. Your account will be locked.')
