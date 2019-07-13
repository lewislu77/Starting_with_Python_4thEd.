# kolekcjoner owadow
# lewis_lu 13/07/2019

total_ins = 0
days = 5

print('\n\tProgram oblicza ilosc zebranych owadow w', days, 'dni.\n')

for n in range(days):
	print('\tDzien', n+1, end='')
	ins = int(input('. Ile owadow zebrales: ' ))
	total_ins += ins
	
print('\n\tIlosc zebranych owadow po', n+1, 'dniach, to', total_ins, '.\n')
