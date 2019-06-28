# BMI
# lewis_lu 28/06/2019

growth = float(input('Podaj swoj wzrost (w metrach): '))
weight = float(input('Podaj swoja wage(w kilogramach): '))

BMI = weight / (growth * growth)

if BMI >= 18.5 and BMI <= 25:
	print('Twoje BMI wynosi', format(BMI, ',.2f'), '. Masz prawidlowa wage.')
	
elif BMI < 18.5:
	print('Twoje BMI wynosi', format(BMI, ',.2f'), '. Masz niedowage.')
	
elif BMI > 25:
	print('Twoje BMI wynosi', format(BMI, ',.2f'), '. Masz nadwage.')