# zamiana kilometrow
# lewis_lu 03/08/2019

def km_to_miles(km):
	
	return km * 0.6214
	
def main():
	
	x = float(input('Podaj predkosc w km: '))
	km_to_miles(x)
	print('Podana predkosc w milach, to:', format(km_to_miles(x), '.2f'))

main()