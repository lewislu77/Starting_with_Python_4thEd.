# wartosc przyszla
# lewis_lu 13/10/2019


def future_save(p,i,t):
	
	F = p * ((1+i/100)**t)
	return F
	
def main():
	
	money = float(input('\n\tPodaj aktualne saldo konta: '))
	interest = float(input('\tMiesieczna stopa procentowa: '))
	months = int(input('\tOkres oszczedzania w miesiacach: '))
	
	future_save(money, interest, months)
	
	print('\n\tWartosc przyszla salda wynosi: ', format(future_save(money, interest, months), '.2f'), '\n')
	
main()