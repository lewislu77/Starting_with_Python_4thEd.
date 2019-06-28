
FOOT_MOD = 43.560

feet = input('Podaj powierzchnie w stopach kwadratowych: ')
feet = float(feet)

akr = feet / FOOT_MOD

print ('Podane pole w akrach wynosi: ', format(akr, '.2f'))
