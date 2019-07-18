# populacja
# lewis_lu 18/07/2019

org = int(input('\n\tPodaj poczatkowa liczbe organizmow: '))
przyrost = int(input('\tPodaj dzienny przyrost organizmow (w %): '))
dni = int(input('\tPodaj liczbe dni: '))

print('\n\tdzien\tpopulacja')
print('\t ', dni - (dni - 1), '\t ', format(org, '.2f'))


for n in range(1, dni):
	org = org + org * (przyrost / 100)
	print('\t ',n+1, '\t ', format(org, '.2f'))
	
print()
	
