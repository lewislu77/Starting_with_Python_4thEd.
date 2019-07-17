# Groszowe wynagrodzenie
# lewis_lu 17/07/2019

wyn_total = 0.0
wyn = 0.01

dni = int(input('\n\tPodaj liczbe dni pracy: '))
print()

print('\tdzien ', dni - (dni - 1), 'wynagrodzenie - ', wyn, 'PLN.')

for n in range(1, dni):
	wyn *= 2
	wyn_total += wyn
	
	print('\tdzien ', n+1, 'wynagrodzenie - ', wyn, 'PLN.')
	
print('\n\tCalkowite wynagrodzenie po', dni, 'dniach, wynosi - ', format(wyn_total, '.2f'), 'PLN.\n')