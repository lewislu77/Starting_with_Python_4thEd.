# stopy na cale
# lewis_lu 06/10/2019

def foot_to_inches(foot):
	return foot * 12

	
def main():
	
	s = int(input('\n\tPodaj liczbe stup: '))
	print('\tPodanej liczbie stup odpowiada', foot_to_inches(s), 'cali.\n')

	
main()