# przebyta odleglosc
# lewis_lu 14/07/2019


predkosc = int(input('\n\tPodaj predkosc pojazdu (w km/h): '))
czas = int(input('\tPodaj czas trwania podrozy (w h): '))



print('\n\tGodzina\t\tPrzebyta odleglosc')
print('\t-----------------------------------')

for n in range(czas):
	odl = (predkosc) * (n+1)
	print('\t',n+1, '\t\t', odl,)
	
print()
	
	
