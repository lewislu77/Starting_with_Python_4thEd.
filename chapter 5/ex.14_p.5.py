# energia kinetyczna
# lewis_lu 07/10/2019

def kinetic_energy(mass, speed):
	return 0.5 * mass * speed**2
	
def main():
	
	print('\n\tENERGIA KINETYCZNA OBIEKTU')
	
	m = float(input('\n\tPodaj mase obiektu w kilogramach: '))
	p = float(input('\tPodaj predkosc obiektu w m/s: '))
	
	print('\n\tEnergia kinetyczna obiektu wynosi', format(kinetic_energy(m,p),'.2f'),'J\n')
	
main()