# srednie opady deszczu
# lewis_lu 14/07/2019

print('\n\tProgram oblicza srednie opady deszczu')

ile_lat = int(input('\tPodaj ile lat ma dotyczyc badany okres: '))
print()

opad_total = 0.0
ile_miesiecy = ile_lat * 12

for l in range(ile_lat):
	for m in range(12):
		print('\tMiesac', m+1, end='')
		opad = float(input(' - podaj wielkosc opadow: '))
		opad_total += opad
		opad_sred = opad_total / ile_miesiecy

print('\n\tIle miesiecy\tSuma opadow\t\tSredni opad miesieczny')
print('\t------------------------------------------------------------')
print('\t',ile_miesiecy, '\t\t', format(opad_total, '.2f'), 'mm\t\t', format(opad_sred, '.2f'),'mm')
print()