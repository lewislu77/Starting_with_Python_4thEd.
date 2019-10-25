# sredni wynik ze sprawdzianow
# lewis_lu 07/10/2019

def calc_average(a,b,c,d,e):
	return (a+b+c+d+e)/5
	
def determine_grade(p):
	
	if p in range(90,101):
		return 5
	elif p in range(80, 90):
		return 4
	elif p in range(70, 80):
		return 3
	elif p in range(60, 70):
		return 2
	elif p < 60:
		return 1
		
def main():
	
	a = int(input('\n\tPodaj wyniki z pierwszego sprawdzianu:\t '))
	b = int(input('\tPodaj wyniki z drugiego sprawdzianu:\t'))
	c = int(input('\tPodaj wyniki z trzeciego sprawdzianu:\t'))
	d = int(input('\tPodaj wyniki z czwartego sprawdzianu:\t'))
	e = int(input('\tPodaj wyniki z piatego sprawdzianu:\t'))
	
	print('\n\tOcena z pierwszego sprawdzianu \t- ', determine_grade(a))
	print('\tOcena z drugiego sprawdzianu \t- ', determine_grade(b))
	print('\tOcena z trzeciego sprawdzianu \t- ', determine_grade(c))
	print('\tOcena z czwartego sprawdzianu \t- ', determine_grade(d))
	print('\tOcena z piatego sprawdzianu \t- ', determine_grade(e))
	
	print('\n\tSREDNI WYNIK ZE SPRAWDZIANOW - ', int(calc_average(a,b,c,d,e)), '- OCENA -', 
			determine_grade(int(calc_average(a,b,c,d,e))), '\n')

	
main()