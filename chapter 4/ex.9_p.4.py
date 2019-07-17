# poziom oceanu
# lewis_lu 17/07/2019


poz = 0.0

print('\n\t    Poziom oceanu podnosi sie o 1.6 mm na rok')
print(' \tTabela wzrostu poziomu oceanu w nastepnych 25 latach')
print('\t\tRok\t\tPoziom oceanu')

for n in range(25):
	poz += 1.6
	print('\t\t', n+1, '\t\t  ', format(poz, '.1f'), 'mm')
	
print()
	