# ubezpieczenie nieruchomosci
# lewis_lu 03/08/2019

MIN_INSURE = 0.8

def min_ubezp(wart_nieruch):
	return wart_nieruch * MIN_INSURE

def main():
	x = float(input('\n Podaj wartosc nieruchomosci: '))
	
	min_ubezp(x)

	print ('\n Wartosc nieruchomosci', format(x,'.1f'), '$')
	print (' Minimalne ubezpieczenie to', format(MIN_INSURE, '.0%'), 'wartosci nieruchomosci - czyli', \
       format(min_ubezp(x), '.1f'), '$\n')
	   
main()
