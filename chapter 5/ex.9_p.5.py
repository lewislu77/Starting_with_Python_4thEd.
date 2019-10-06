# podatki
# lewis_lu 06/10/2019


def state_tax(sale):
	return sale * 0.05
	
def county_tax(sale):
	return sale * 0.025
	
def main():
	
	s = float(input('\n\tPodaj wartosc miesiecznej sprzedazy: '))
	
	print('\tPodatek stanowy wynosi', format(state_tax(s), '.2f'))
	print('\tPodatek w hrabstwie wynosi', format(county_tax(s), '.2f'))
	print('\tPodatek w sumie wynosi', format(state_tax(s) + county_tax(s),'.2f'), '\n')

main()
