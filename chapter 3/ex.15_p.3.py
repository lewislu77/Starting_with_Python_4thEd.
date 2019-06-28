# Przeliczanie sekund
# lewis_lu 28/06/2019

MIN = 60
HOUR = 3600
DAY = 86400

sec_input = int(input('Podaj liczbe sekund: '))


if sec_input < MIN:
	
	print('To: ', sec_input, 'sec.')

elif sec_input >= MIN and sec_input < HOUR:

	sec = (sec_input % HOUR) % MIN
	mints = (sec_input % HOUR) // MIN

	print('To: ', mints, 'min :', sec, 'sec.')
	
elif sec_input >= HOUR and sec_input < DAY:
	
	sec = (sec_input % HOUR) % MIN
	mints = (sec_input % HOUR) // MIN
	hours = sec_input // HOUR
	
	print('To: ', hours, 'hr :', mints, 'min :', sec, 'sec.')
	
elif sec_input > DAY:
	
	sec = ((sec_input % DAY) % HOUR) % MIN
	mints = ((sec_input % DAY) % HOUR) // MIN
	hours = (sec_input % DAY) // HOUR
	day = sec_input // DAY
	
	print('To: ', day, ' day(s) :', hours, 'hr :', mints, 'min :', sec, 'sec.')