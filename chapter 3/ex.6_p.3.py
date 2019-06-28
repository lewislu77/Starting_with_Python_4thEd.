# magiczna data
# lewis_lu 17/06/2019

dzien = int(input('Podaj dzien miesiaca: '))
miesiac = int(input('Podaj miesiac: '))
rok = int(input('Podaj rok (postac dwucyfrowa): '))


if rok == dzien * miesiac:					#magiczna data
	print('Podales magiczna date')
else:
	print('Podana data nie jest magiczna')