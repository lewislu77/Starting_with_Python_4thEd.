# wiek osoby
# lewis_lu 16/06/2019

wiek = int(input('Podaj wiek w latach: '))


if wiek <= 1:
	print('NIEMOWLE') 
elif 1 > wiek <= 13:
	print('DZIECKO')
elif 13 > wiek <= 20:
	print('NASTOLATEK')
elif wiek > 20:
	print('DOROSLY')
	