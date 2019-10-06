# wartosc max dwoch liczb
# lewis_lu 06/10/2019


def max(x,y):
	if x-y < 0:
		print('\n\tZ podanych liczb wieksza wartoscia jest:', y)
	else:
		print('\n\tZ podanych liczb wieksza wartoscia jest:', x)
	
	
def main():
	
	a = int(input('\n\tPodaj wartosc pierwszej liczby: '))
	b = int(input('\tPodaj wartosc drugiej liczby: '))
	
	max(a,b)
	
	
main()