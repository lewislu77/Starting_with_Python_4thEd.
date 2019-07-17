# odchudzanie
# lewis_lu 17/07/2019


loss_weight = 2

weight = float(input('\n\t\tPodaj aktualna mase ciala w kg: '))
print('\n\t Aktualna waga', format(weight, '.2f'), 'kg, miesieczny spadek', format(loss_weight, '.2f'), 'kg.')
print('\t\tMiesiac\t\t\tOczekiwana waga')

for n in range(6):
	weight -= loss_weight
	print('\t\t', n+1, '\t\t\t  ', format(weight, '.2f'), 'kg.')
	
print()