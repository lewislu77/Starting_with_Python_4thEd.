# swobodny spadek obiektu
# lewis_lu 07/10/2019


def falling_distance(time):
	return 0.5 * 9.8 * time**2

def main():
	
	print('\n\t   SWOBODNY SPADEK OBIEKTU\n')
	
	for t in range(1,10):
		print('\t', t,'sek. \t- ',format(falling_distance(t),'.2f'),'m.' )
		
	print('\n')
		
main()