# kalorie
# lewis_lu 14/08/2019

def tluszcz_cal(GrTl):
	return GrTl * 9
	
def cukier_cal(GrCuk):
	return GrCuk * 4
	
def main():
	
	t = float(input('\n Podaj ilosc spozytych tluszczy w gramach: '))
	c = float(input(' Podaj ilosc spozytych cukrow w gramach: '))
	
	tluszcz_cal(t)
	cukier_cal(c)
	
	print('\n Wartosc kaloryczna tluszczy, to:', format(tluszcz_cal(t), '.2f'), 'cal, a cukrow, to:', format(cukier_cal(c), '.2f'), 'cal.\n')
	
main()