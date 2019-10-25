# liczby pierwsze - test
# lewis_lu 07/10/2019

def is_prime(number):
	
	if number < 2:
		return False
		
	elif number == 2:
		return True
		
	else:
	
		for i in range (2, number):
			if number % i == 0:
				return False
			if i * i > number:
				return True

	
def main():
	
	number = int(input('\n\tPodaj liczbe: '))
	
	if is_prime(number):
		print('\n\tPodana liczba jest liczba pierwsza !!!\n')
	else:
		print('\n\tPodana liczba nie jest liczba pierwsza.\n')
		
main()