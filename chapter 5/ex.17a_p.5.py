# liczby pierwsze - test
# lewis_lu 07/10/2019


def is_prime(number):
	
	if number < 2:
		return False
		
	for i in range (2, int(number ** .5) + 1):
		if number % i == 0:
			return False
	return True

	
def main():
	
	number = int(input('\n\tPodaj liczbe: '))
	
	if is_prime(number):
		print('\n\tPodana liczba jest liczba pierwsza !!!\n')
	else:
		print('\n\tPodana liczba nie jest liczba pierwsza.\n')
		
main()