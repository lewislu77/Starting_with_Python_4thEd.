# test matematyczny
# lewis_lu 06/10/2019

import random

def main():

	x = random.randint(1, 100)
	y = random.randint(1, 100)
	
	sum = x + y
	
	print('\n\tSUMOWANIE  LICZB')
	
	print('\n\t  ',x,'+',y)
	
	suma = int(input('\n\tPodaj wynik dodawania: '))
	
	if sum == suma:
		print('\n\tGRATULACJE - PODALES PRAWIDLOWY WYNIK\n')
	else:
		print('\n\tWYNIK NIE JEST POPRAWNY\n')
		
		
main()