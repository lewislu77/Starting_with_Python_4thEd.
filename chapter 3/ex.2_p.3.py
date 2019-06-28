#pola powierzchni prostokatow
# lewis_lu 16/06/2019

a1 = float(input('Podaj dlugosc boku pierwszego prostokata: '))
b1 = float(input('Podaj dlugosc drugiego boku pierwszego prostokata: '))

a2 = float(input('Podaj dlugosc boku drugiego prostokata: '))
b2 = float(input('Podaj dlugosc drugiego boku drugiego prostokata: '))

pole1_prostokata = a1 * b1
pole2_prostokata = a2 * b2

if pole1_prostokata > pole2_prostokata:
	print('Pole pierwszego prostokata ma wieksza powierzchnie') 
elif pole1_prostokata < pole2_prostokata:
	print('Pole drugiego prostokata ma wieksza powierzchnie')
elif pole1_prostokata == pole2_prostokata:
	print('Pola powierzchni prostokatow sa rowne')
else:
	print('END')