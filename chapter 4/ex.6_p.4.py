# konwersja temperatur
# lewis_lu 17/07/2019


print('\n\tTabela konwersji temperatur')
print('\t stopnie C\tstopnie F')
print('\t---------------------------')

for C in range(21):
	F = ((9 * C) / 5) + 32
	print('\t   ', C, '\t\t  ', F)
	
print()	