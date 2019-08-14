# stadion strefy
# lewis_lu 14/08/2019


def str_A(bilety):
	return bilety * 20
	
def str_B(bilety):
	return bilety * 15
	
def str_C(bilety):
	return bilety * 10

def dochod(a,b,c):
	return str_A(a) + str_B(b) + str_C(c)

	
def main():
	
	a = int(input('\n Ilosc sprzedanych biletow w strefie A: '))
	b = int(input(' Ilosc sprzedanych biletow w strefie B: '))
	c = int(input(' Ilosc sprzedanych biletow w strefie C: '))
	
	str_A(a)
	str_B(b)
	str_C(c)
	dochod(a,b,c)
	
	print('\n Laczny dochod ze sprzedazy biletow wyniosl:', dochod(a,b,c), 'PLN\n')
	
main()
	
	