# zliczanie monet; 1 zloty - WYGRANA
# lewis_lu 24/06/2019

gr_1 = int(input('Podaj ilosc monet 1 gr: '))
gr_2 = int(input('Podaj ilosc monet 2 gr: '))
gr_5 = int(input('Podaj ilosc monet 5 gr: '))
gr_10 = int(input('Podaj ilosc monet 10 gr: '))
gr_50 = int(input('Podaj ilosc monet 50 gr: '))

suma_1 = gr_1 * 1
suma_2 = gr_2 * 2
suma_5 = gr_5 * 5
suma_10 = gr_10 * 10
suma_50 = gr_50 * 50

suma_calkowita = suma_1 + suma_2 + suma_5 + suma_10 + suma_50

if suma_calkowita % 100 == 0:
	if suma_calkowita // 100 == 1:
		print('Wygrales. Zebrana kwota to 1 zloty.')

elif suma_calkowita % 100 != 0:
	if suma_calkowita // 100 < 1:
		print('Zebrales kwote mniejsza niz 1 zl, tj.', (suma_calkowita / 100) * 100 , 'grosze(-y).' )
	else:
		print('Zebrales kwote wieksza niz 1 zl, tj.', suma_calkowita / 100, 'zlotych.')