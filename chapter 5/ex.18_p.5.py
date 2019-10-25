# liczby pierwsze - losowanie
# lewis_lu 13/10/2019


def is_prime(number):
	
	if number < 2:
		return False
		
	for i in range (2, int(number ** .5) + 1):
		if number % i == 0:
			return False
	return True	


def main():
	
	n = 0
	
	while n < 100:
		
		n += 1
		is_prime(n)

		if is_prime(n) == True:
			print(n)
			
			
main()
		