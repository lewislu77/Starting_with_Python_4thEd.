
print()

km = input('Podaj ilosc pokonanych kilometrow: ')
litr = input('Podaj ilosc zuzytego paliwa: ')

km = float(km)
litr = float(litr)

KNL = (litr * 100) / km

print()

print('Zuzycie paliwa wynosi: ', format(KNL, '.2f'), 'litrow / 100 km.\n')
