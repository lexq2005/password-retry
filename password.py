password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	ps = input("Enter Password: ")
	if ps == password:
		print('password is correct')
		break #Exit
	else:
		print('Password Error, you have ', i, 'time(s) to try.')
