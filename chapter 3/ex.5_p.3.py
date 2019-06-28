# ciezar w Newtonach
# lewis_lu 17/06/2019

masa = float(input('Podaj mase obiektu w kilogramach: '))

ciezar = masa * 9.8

if ciezar > 500:
	print('Obiekt jest za ciezki')
elif ciezar < 100:
	print('Obiekt jest za lekki')
else:
	print('Obiekt ma odpowiedni ciezar')