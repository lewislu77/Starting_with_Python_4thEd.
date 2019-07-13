# spalone kalorie
# lewis_lu 13/07/2019

total_cal = 0
cal_per_min = 4.2

print('\n\tProgram podaje ilosc spalonych kalorii na biezni, gdy', format(cal_per_min, '.1f'), 'cal\min.\n')

for n in range(5, 30, 5):
	cal = cal_per_min * 5
	total_cal += cal
	print('\tIlosc spalonych kalorii po', n+5, 'minutach, to', total_cal, 'cal')

print()

