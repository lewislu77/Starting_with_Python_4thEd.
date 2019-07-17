# suma liczb
# lewis_lu 17/07/2019

total = 0

liczba = int(input('\n\tPodaj liczbe dodatnia (gdy ujemna - koniec serii): '))

while liczba >= 0:
	total += liczba
	liczba = int(input('\tPodaj kolejna liczbe z serii: '))
	
print('\n\tSuma podanych liczb wynosi: ', total, '\n')