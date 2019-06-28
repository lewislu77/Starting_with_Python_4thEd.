# program lojalnosciowy ksiegarnia
# lewis_lu 24/06/2019

book = int(input('Podaj ilosc zakupionych ksiazek w tym miesiacu: '))

if book == 0:
	print('Przyznano Ci 0 punktow lojalnosciowych')
	
elif book > 0 and book <= 2:
		print('Przyznano Ci 5 punktow lojalnosciowych')
elif book > 2 and book <= 4:
		print('Przyznano Ci 15 punktow lojalnosciowych')
elif book > 4 and book <= 7:
		print('Przyznano Ci 30 punktow lojalnosciowych')

elif book >= 8:
	print('Przyznano Ci 60 punktow lojalnosciowych')