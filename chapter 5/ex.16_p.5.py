# zliczanie liczb parzystych
# lewis_lu 07/10/2019

import random
	
def main():
	
	los = int(input('\n\tPodaj ilosc losowanych liczb: '))
	n_max = int(input('\tPodaj zakres losowanych liczb, od 1 do '))
	
	print('\n')
	
	even = 0
	odd = 0
	idx = 0
	
	while idx < los:
		
		number = random.randrange(1,n_max+1)
		idx += 1
		print('\t',number)
		
		if number % 2 == 0:
			even += 1
		else:
			odd += 1
			
	print('\n\tNa',los,'wylosowanych liczb parzystych bylo', even, ', a nieparzystych', odd, '.\n')
	
main()