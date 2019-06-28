# kolory podstawowe CZERWONY, ŻÓŁTY, NIEBIESKI
# lewis_lu 17/06/2019

ZOLTY = 'zolty'
CZERWONY = 'czerwony'
NIEBIESKI = 'niebieski'

kolor_1 = input('Podaj pierwszy kolor podstawowy: ')
kolor_2 = input('Podaj drugi kolor podstawowy: ')


if kolor_1 == ZOLTY and kolor_2 == CZERWONY:
	print('POMARANCZOWY')
elif kolor_2 == ZOLTY and kolor_1 == CZERWONY:
	print('POMARANCZOWY')
elif kolor_1 == CZERWONY and kolor_2 == NIEBIESKI:
	print('FIOLETOWY')
elif kolor_2 == CZERWONY and kolor_1 == NIEBIESKI:
	print('FIOLETOWY')
elif kolor_1 == ZOLTY and kolor_2 == NIEBIESKI:
	print('ZIELONY')
elif kolor_2 == ZOLTY and kolor_1 == NIEBIESKI:
	print('ZIELONY')
else:
	print('NIE PODALES KOLOROW PODSTAWOWYCH !!!')