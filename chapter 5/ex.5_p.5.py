# podatek od nieruchomosci
# lewis_lu 14/08/2019

PROC_WART = 0.6
PODAT_JEDN = 0.72

def wart_szac(wartosc):
	x = wartosc * PROC_WART
	return x
	
def podatek(x):
	return (x // 100) * PODAT_JEDN
	
def main():
	
	n = float(input('\n Podaj wartosc rzeczywista nieruchomosci: '))
	
	wart_szac(n)
	podatek(wart_szac(n))
	
	print('\n Wartosc szacowana, tj.', format(PROC_WART, '.0%' ),'wartosci nieruchomosci, wynosi', format(wart_szac(n), '.2f'), 'PLN')
	print(' Nalezny podatek od nieruchomosci to', format(podatek(wart_szac(n)), '.2f'), 'PLN\n')
	
main()