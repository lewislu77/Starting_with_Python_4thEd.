# koszty wysylki
# lewis_lu 24/06/2019


weight = float(input('Podaj wage przesylki w kilogramach: '))


if weight < 2:
	print('Koszt przesylki wynosi 1.50 $')
	
elif weight >= 2 and weight < 6:
	print('Koszt przesylki wynosi 3.00 $')
	
elif weight >= 6 and weight < 10:
	print('Koszt przesylki wynosi 4.00 $')
	
elif weight >= 10:
	print('Koszt przesylki wynosi 4.75 $')