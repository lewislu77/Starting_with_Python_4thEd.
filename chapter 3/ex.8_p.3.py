# ile opakowan bulek i parowek na hot-dog
# dla podanej ilosci osob

#lewis_lu 18/06/2019


BOX_PAR = 10
BOX_BUL = 8

osoby = int(input('Podaj ilosc osob: '))

box_p = osoby % BOX_PAR
box_p1 = osoby // BOX_PAR
box_p2 = box_p1 + 1
ext_p = BOX_PAR - box_p

box_b = osoby % BOX_BUL
box_b1 = osoby // BOX_BUL
box_b2 = box_b1 + 1
ext_b = BOX_BUL - box_b


if box_p > 0:
	print('Potrzebujesz', box_p2,'opakowan parowek' )
else:
	print('Potrzebujesz', box_p1, 'opakowan parowek')
	
if box_b > 0:
	print('Potrzebujesz', box_b2,'opakowan bulek' )
else:
	print('Potrzebujesz', box_b1, 'opakowan bulek')
	
if box_p > 0:
	print('Pozostalo jeszcze', ext_p, 'parowki(-ek)')
if box_b > 0:
	print('Pozostalo jeszcze', ext_b, 'bulki(-ek)')
