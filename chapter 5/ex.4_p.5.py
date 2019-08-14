# koszty samochodu
# lewis_lu 14/08/2019

def koszt_mies(rata, ubezp, paliwo, serwis):
	x = rata + ubezp + paliwo + serwis
	return x

def koszt_rok(x):
	return 12 * x
	
def main():
	
	r = float(input('\n Podaj kwote raty kredytu: '))
	u = float(input(' Podaj koszt ubezpieczenia: '))
	p = float(input(' Podaj koszt paliwa: '))
	s = float(input(' Podaj koszt serwisu: '))
	
	koszt_mies(r,u,p,s)
	print('\n Miesieczny koszt wynosi:', format(koszt_mies(r,u,p,s), '.2f'), 'PLN')
	
	koszt_rok(koszt_mies(r, u, p, s))
	print(' Roczny koszt wynosi:', format(koszt_rok(koszt_mies(r,u,p,s)), '.2f'), 'PLN')
	
main()