# odgadywanie liczby losowej
# lewis_lu 13/10/2019

import random

def guess(number):

	my_number = int(input('\n\tPodaj wylosowana liczbe (0-100): '))
	
	count = 0

	while number != my_number:

		if number > my_number:
			print('\n\tZbyt mala, sprobuj ponownie')
			count += 1
			my_number = int(input('\n\tPodaj wylosowana liczbe (0-100): '))

		elif number < my_number:
			print('\n\tZbyt duza, sprobuj ponownie')
			count += 1
			my_number = int(input('\n\tPodaj wylosowana liczbe (0-100): '))

	print('\n\t\t\tGRATULACJE')
	print('\tPrawidlowa liczba po', count, 'nieudanych probach.')


def main():

	again = 't'

	while again == 't' or again == 'T':

		number = random.randrange(1,101)
		guess(number)
		again = input('\n\tCzy losowac jeszcze raz ? (t = tak): ')

main()
