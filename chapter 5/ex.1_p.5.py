# zamiana kilometrow
# lewis_lu 03/08/2019

def km_to_miles(x):
	
	miles = x * 0.6214
	print('Podana predkosc w milach, to: ', format(miles, '.2f'))
	
def main():
	
	km = float(input('Podaj predkosc w km: '))
	km_to_miles(km)

main()