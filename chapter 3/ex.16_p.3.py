#rok przestepny
# lewis_lu 28/06/2019



year = int(input('Podaj rok: '))



if year % 100 == 0 and year % 400 == 0:
		print('W', year, 'roku luty ma 29 dni')
	
elif year % 100 != 0 and year % 4 == 0:
		print('W', year, 'roku luty ma 29 dni')

else:
	print('W', year, 'roku luty ma 28 dni.')