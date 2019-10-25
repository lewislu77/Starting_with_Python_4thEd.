# papier, kamien, nozyce
# lewis_lu 13/10/2019

import random

def start():
	
	num = random.randrange(1,4)
	comp = ''
	
	if num == 1:
		comp = 'KAMIEN'
	elif num == 2:
		comp = 'PAPIER'
	else:
		comp = 'NOZYCE'
		
	my_choice = input('\n\tWybierz KAMIEN, PAPIER lub NOZYCE: ')
	
	print('\t',comp)
	return comp, my_choice
	
		
def draw(r,x):
	
	while comp == my_choice:
		comp, my_choice = start()
		
	else:
		if comp == 'KAMIEN' and my_choice == 'NOZYCE':
			print('KOMPUTER wygrywa!!!')
		elif comp == 'NOZYCE' and my_choice == 'KAMIEN':
			print('TY wygrywasz!!!')
		elif comp == 'PAPIER' and my_choice == 'NOZYCE':
			print('TY wygrywasz!!!')
		elif comp == 'NOZYCE' and my_choice == 'PAPIER':
			print('KOMPUTER wygrywa!!!')
		elif comp == 'KAMIEN' and my_choice == 'PAPIER':
			print('TY wygrywasz!!!')
		elif comp == 'PAPIER' and my_choice == 'KAMIEN':
			print('KOMPUTER wygrywa!!!')



def main():

#	again = 't'

#	while again == 't' or again == 'T':

	comp, my_choice = start()
	draw(comp, my_choice)
	
#	again = input('\n\tCzy gramy jeszcze raz ? (t = tak): ')

main()