# budzet
# lewis_lu 14/07/2019

wydatki_suma = 0
dalej = 't'


bud = float(input('\n\tPodaj kwote budzetu miesiecznego (w $):'))

while dalej == 't':
	wyd = float(input('\tPodaj koszt wydatku (w $): '))
	wydatki_suma += wyd
	dalej = input('\tCzy chcesz podac nastepny koszt? (Jesli tak, wpisz t): ')
	
	bud_suma = bud - wydatki_suma
	
if bud_suma > 0:
	print('\n\tPozostalo na koncie', format(bud_suma, '.2f'), '$.\n')
	
else:
	print('\n\tPrzekroczyles budzet o', format(bud_suma, '.2f'), '$.\n')
	

